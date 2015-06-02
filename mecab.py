#!/usr/bin/env python
# -*- coding: utf-8 -*-
#mecab.py

import MeCab

rc = open('repotxt/repo_comments','r')
f = open('mecabtxt/keyword','w')
m = MeCab.Tagger("-Ochasen")
for comment in rc:
    node = m.parseToNode(comment) 
    while node:
        if node.feature.split(",")[0] == "名詞":
            print node.surface
            f.write(node.surface)
            f.write("\n")
        node = node.next 
rc.close()
f.close()
