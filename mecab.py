#!/usr/bin/env python
# -*- coding: utf-8 -*-
#mecab.py

import MeCab


text = raw_input("text>")
m = MeCab.Tagger("-Ochasen")

node = m.parseToNode(text)
while node:
    if node.feature.split(",")[0] == "名詞":
        print node.surface
    node = node.next
        
    #f = open('mecabtxt/mtxt','a')
    #f.write(mtxt)
    #f.close()
