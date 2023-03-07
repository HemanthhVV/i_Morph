import spacy_cleaner
import spacy
import pickle
from spacy_cleaner.processing import removers,mutators
from PyPDF2 import PdfReader
def fun(feed):
    read=PdfReader(feed)
    page=read.pages[0]
    text=page.extract_text()
    text=text.lower()
    nlp=spacy.load("en_core_web_md")
    doc = nlp(text)
    Main=[]
    sslc=[]
    hsc=[]
    univrsity=[]
    diploma=[]
    temp=[]
    skills=[]
    INTENT=0
    for each_sents in doc.sents:
        temp.append(each_sents)
    for each_list in temp:
        for each_word in each_list:
            if (each_word.text =="sslc" or each_word.text == "10"):
                sslc.append(str(each_list))
            if ((each_word.text =="hsc" or each_word.text == "12" or each_word.text=="secondary")):
                hsc.append(str(each_list))
            if (each_word.text == "cgpa"):
                univrsity.append(str(each_list))
            if (each_word.text =="diploma" or each_word.text =="polytechnic"):
                diploma.append(str(each_list))
            if(each_word.text == "intentship" or each_word.text == "internship" or each_word.text == "intent" or each_word.text == "intern"):
                INTENT=1
    pipeline=spacy_cleaner.Pipeline(
        nlp,
        removers.remove_stopword_token,
        removers.remove_punctuation_token,
        mutators.mutate_lemma_token,
    )
    univrsity=set(univrsity)
    sslc=set(sslc)
    hsc=set(hsc)
    diploma=set(diploma)
    temp2=[sslc,hsc,diploma,univrsity]
    for entities in range(0,len(temp2)):
        temp2[entities]=pipeline.clean(temp2[entities])

    for each_sen in temp2:
        if (len(each_sen)==0):
            Main.append(0)
            pass
        else:
            text_t=nlp(each_sen[0])
            for each_word in text_t:
                if(each_word.pos_ == "NUM"):
                    if(float(each_word.text) > 30 and float(each_word.text)<100):
                        Main.append(float(each_word.text))
                    if(float(each_word.text)< 10 and float(each_word.text)>0):
                        c=float(each_word.text)
                        Main.append(c)
    Main2=[]
    for each_items in Main:
        if each_items not in Main2:
            Main2.append(each_items)
    nlp2=spacy.load("en_core_web_lg")
    skills="jz_skill_patterns.jsonl"
    ruler=nlp2.add_pipe("entity_ruler",before="ner")
    ruler.from_disk("C:/Users/vvhem/Downloads/jz_skill_patterns.jsonl")
    doc2=nlp2(text)
#     from spacy import displacy
#     displacy.render(doc2, style="ent", jupyter=True)
    s=[]
    for each_labels in doc2.ents:
            if(each_labels.label_=="SKILL"):
                s.append(each_labels.text)
    skill=set(s)
# print(len(skill))
    Main2.append(len(skill))
    if(INTENT==1):
        Main2.append(1)
    else:
        Main2.append(0)
    dept=['mechanical', 'civil', 'computer', 'instrumentation', 'mechatronics', 'information technology']
    dept_val=[5,1,0,2,4,3]
    index=0
    for each_sents in doc.sents:
        for each_word in each_sents:
            if str(each_word) in dept:
                index=dept.index(str(each_word))
                break;
    Main2.append(dept_val[index])
    count=0
    for each_sents in doc.sents:
        for each_token in each_sents:
            if(each_token.text == "projects"):
                count=1
    Main2.append(count)
    with open('data_model_1','rb') as f:
        model=pickle.load(f)
    predicticed_value=model.predict([Main2])
    return(predicticed_value[0])

