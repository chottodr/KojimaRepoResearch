#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
#makecorpus.py

import sys
from pprint import pprint
from gensim import corpora, models, similarities
argvs = sys.argv
doc = open(argvs[1],'r')
path=argvs[1].rstrip(".txt")
documents = []
data = doc.read()
#コメントファイルの準備
linesl = data.split('\n')
for line in linesl:
    documents.append((line))
documents.pop()

sw = open("stopword.txt",'r').read()
#print sw
stoplist = set(sw.split('\n'))

#小文字化とストップワードの削除
texts = [[word for word in document.lower().split() if word not in stoplist]\
        for document in documents]

all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
#出現回数が１回の単語を削除
texts = [[word for word in text if word not in tokens_once]for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save_as_text(path+'.dict')

#コーパスの作成(bag-of-word
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(path+'.mm', corpus)
#コーパスの作成(tfidf
tfidf = models.TfidfModel(corpus)
tfidf.save(path+".tfidf")
corpus_tfidf = tfidf[corpus]

#index = similarities.SparseMatrixSimilarity(corpus,num_features=len(dictionary))
#index.save(path+".index")
num = 5
lda = models.LdaModel(corpus_tfidf,id2word=dictionary, num_topics=num)
lda.save(path+"_lda.model")
logfile = open(path+'_topic.txt', 'w')
n=0
for i in range(0, lda.num_topics):
    logfile.write("topic")
    logfile.write(str(n))
    logfile.write("#")
    logfile.write(lda.print_topic(i))
    logfile.write("\n")
    n=n+1

corpus_lda = lda[corpus_tfidf]
corpora.MmCorpus.serialize(path+'_lda.mm', corpus_lda)
