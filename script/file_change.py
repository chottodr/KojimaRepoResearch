#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

##変更ファイルの名前と行数を出力
def file_change(repo):
    dir_name = repo.replace("/","_")
    os.chdir("repositories/"+dir_name)##今は相対パス,本番環境は絶対パスにすること
    os.system('git log --reverse --date=short --no-merges --numstat --pretty=format:"%cd" > FileChange.txt')

if __name__ =="__main__":
    argvs = sys.argv
    repo = argvs[1]
    file_change(repo)
