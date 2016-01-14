#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


dic = [{"name":"test1","commits":[{"x":"kojima","y":"kumoi","z":"segawa"}]}]
##新しいファイルが出現した時

dic.append({"name":"test2","commits":[{"x":"tsujiura","y":"itou","z":"saitou"}]})

##すでに登録されているファイルがある場合for:if(txt内のファイル名=db内のファイル名)
dic[1]["commits"].append({"x":"kazushi","y":"naoto","z":"taka**"})
##print dic[1]["name"]##1番目の要素のnameを取得
print dic
