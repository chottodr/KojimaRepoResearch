#!/usr/bin/env python
# -*- coding: utf-8 -*-
#mecab.py

import MeCab
import pickle
text = raw_input("text>")
m = MeCab.Tagger("-Ochasen")
node = m.parseToNode(text)

f = open('mecabtxt/keyword','a')
norm = []
while node:
    if node.feature.split(",")[0] == "名詞":
        print node.surface
        f.write(node.surface)
        f.write("\n")
        #norm.append(node.surface)
    node = node.next        
f.close()
