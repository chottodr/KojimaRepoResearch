#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
#makecorpus.py
##example############################################
#python makecorpus.py hoge.txt #
#####################################################
import re
import sys
import string
import nltk
from pprint import pprint
from gensim import corpora, models, similarities


def calltxt(path):##1要素1コミットメッセージの文書配列を返す
    document = []
    doc = open(path,'r')
    texts = []
    data = doc.read()
    linesl = data.split('\n')
    for line in linesl:
        document.append((line))
    #document.pop()
    #print document
    return document

def cleantxt(documents, path):#不必要な文字を削除
    doc = open(path,'r')
    data = doc.read()
    #ストップワードの設定
    sw = open("stopword.txt",'r').read()
    stoplist = set(sw.split('\n'))

    #取り除くメタ文字の設定
    metaTrans = string.maketrans("`~=.,<>?_{}|*+[]^-;:!\"#$%&'@()\\/","                                ")
    texts = [doc.translate(metaTrans) for doc in documents]
    #print texts
    
    #文書内単語分けと小文字化・ストップワードの削除
    texts = [[word for word in document.lower().split() if word not in stoplist]for document in texts]
    #print texts

    #残った単語に対する語幹の削除（ステミング）
    porter = nltk.PorterStemmer()
    texts = [[porter.stem(word.decode('utf-8')) for word in text]for text in texts]
    #print texts

    #出現回数が1回のトークン作成
    all_tokens = sum(texts, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)

    #出現回数が１回の単語を削除
    texts = [[word for word in text if word not in tokens_once]for text in texts]
    return texts

#コーパスの作成(bag-of-word
def makebowcorpus(texts, path):
    path = path.rstrip(".txt") 

    dictionary = corpora.Dictionary(texts)
    dictionary.save(path+'.dict')
    dictionary.save_as_text(path+'_text.dict')

    corpus = [dictionary.doc2bow(text) for text in texts]
    print corpus
    corpora.MmCorpus.serialize(path+'.mm', corpus)

#コーパスの作成(tfidf
def maketfidfcorpus(corpus, path):
    path = path.rstrip(".txt")
    tfidf = models.TfidfModel(corpus)
    tfidf.save(path+".tfidf")
    corpus_tfidf = tfidf[corpus]

#LDAモデルの作成(bowコーパス
def makeLDA(num, path):
    path = path.rstrip(".txt")
    print path+".dict"
    dictionary = corpora.Dictionary.load(path+'.dict')
    corpus = corpora.MmCorpus(path+'.mm')

    lda = models.LdaModel(corpus=corpus,id2word=dictionary, num_topics=num)
    lda.save(path+"_lda.model")
    logfile = open(path+'_topic.txt', 'w')
    print path+'_topic.txt'
    print 
    n=0
    for i in range(0, lda.num_topics):
        logfile.write(lda.print_topic(i))
        logfile.write("\n")
    corpus_lda = lda[corpus]
    corpora.MmCorpus.serialize(path+'_lda.mm', corpus_lda)

def makeHDP(path):
    path = path.rstrip(".txt")
    print path+".dict"
    dictionary = corpora.Dictionary.load(path+".dict")
    corpus = corpora.MmCorpus(path+".mm")
    hdp = models.HdpModel(corpus=corpus,id2word=dictionary)
    hdp.save(path+"_hdp.model")
    logfile = open(path+'_hdp_topic.txt', 'w')
    hdp.print_topics(topics=20, topn=10)
    for i in hdp.print_topics():
        print i
    corpus_hdp = hdp[corpus]
    corpora.MmCorpus.serialize(path+'_hdp.mm', corpus_hdp)

if __name__=="__main__":
    argvs = sys.argv
    path = argvs[1]
    document = calltxt(path)
    texts = cleantxt(document, path)
    makebowcorpus(texts, path)
    #makeHDP(path)
    makeLDA(3,path)
