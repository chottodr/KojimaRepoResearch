#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
#makecorpus.py

from gensim import corpora, models, similarities

doc = open('repotxt/repo_files.txt','r')
documents = []
datal = doc.read()

linesl = datal.split('\n')
for line in linesl:
    documents.append((line))

stoplist = set('for a of the and to in'.split())

texts = [[word for word in document.lower().split() if word not in stoplist]for document in documents]

all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]for text in texts]
#print texts

dictionary = corpora.Dictionary(texts)
dictionary.save('repotxt/deerwester.dict')

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('repotxt/deerwester.mm', corpus)
print corpus
