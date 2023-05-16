import spacy
from spacy.lang.en import STOP_WORDS
from string import punctuation
from heapq import nlargest

nlp= spacy.load('en_core_web_sm')

def summarizer(rawdocs):
    stopwords=list(STOP_WORDS)
    doc=nlp(rawdocs)
    #print(doc)

    tokens=[token.text for token in doc]
    word_freq={}
    for w in doc:
        if w.text.lower() not in stopwords and w.text.lower() not in punctuation:
            if w.text not in word_freq.keys():
                word_freq[w.text]=1
            else:
                word_freq[w.text]+=1
    #print(word_freq)
    max_freq=max(word_freq.values())
    #print(max_freq)
    for w in word_freq.keys():
        word_freq[w]=word_freq[w]/max_freq
        #Normalized frequencies
    #print(word_freq)
    sent_tokens=[sent for sent in doc.sents]
    #print(sent_tokens)
    sent_scores={}
    for sent in sent_tokens:
        for w in sent:
            if w.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[w.text]
                else:
                    sent_scores[sent]+=1

    #print(sent_scores)

    select_len=int(len(sent_tokens)*0.3)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    #print(summary)
    final_summary=[w.text for w in summary]
    summary=' '.join(final_summary)
    #print(summary)
    #print(len(text.split(' ')))
    #print(len(summary.split(' ')))
    return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))