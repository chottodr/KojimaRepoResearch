#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys
import os
import os.path
import linecache

def make_topicDirectory(path):#hoge_lda.mm
    target_line = linecache.getline(path,2)
    linecache.clearcache()
    commitnum = target_line.split(" ")[0]#コミット数の読み込み
    topicnum = target_line.split(" ")[1]#トピック数の読み込み
#    print topicnum
    int_topicnum = int(topicnum)
    int_commitnum = int(commitnum)
    dirpath1 = path.rstrip("_lda.mm")+"_perTopic"
    dirpath2 = path.rstrip("_lda.mm")+"_perTopic_Time"
    if os.path.exists(dirpath1) == False:
        os.mkdir(dirpath1)

    if os.path.exists(dirpath2) == False:
        os.mkdir(dirpath2)
    
#_lda.mmのはじめの2行を除いて,topicnumずつ占有率を見てゆく
    data = []
    startline = 3
    num = 0
    while num < int_commitnum:
        for linenum in range(startline,startline+int_topicnum):
            data.append(linecache.getline(path,linenum).rstrip("\n").split(" ")[2])
            linecache.clearcache()
        result_topicnum = data.index(max(data))+1
        num = num + 1
        print result_topicnum
        if os.path.exists(dirpath1+"/Topic"+str(result_topicnum)+".txt") == False:
            f = open(dirpath1+"/Topic"+str(result_topicnum)+".txt","w")
        else:
            f = open(dirpath1+"/Topic"+str(result_topicnum)+".txt","a")

        if os.path.exists(dirpath2+"/Topic"+str(result_topicnum)+"_time.txt") == False:
            ft = open(dirpath2+"/Topic"+str(result_topicnum)+"_time.txt","w")
        else:
            ft = open(dirpath2+"/Topic"+str(result_topicnum)+"_time.txt","a")
        #print linecache.getline(path.rstrip("_lda.mm")+".txt",num)
        #トピックごとに文書を分類
        f.write(linecache.getline(path.rstrip("_lda.mm")+".txt",num))
        linecache.clearcache()
        f.close()
        #トピックごとに時間付き文書を分類
        ft.write(linecache.getline(path.rstrip("_lda.mm")+"_time.txt",num))
        linecache.clearcache()
        ft.close()

        startline = startline + int_topicnum
        #print data
        data = []


    ##要素の中で最も大きい数字のトピックディレクトリに文章を打ち込む

if __name__=="__main__":
    argvs = sys.argv
    path = argvs[1]
    make_topicDirectory(path)
