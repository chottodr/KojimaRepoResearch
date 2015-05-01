#!/usr/bin/env python
# -*- coding: utf-8 -*-
#main.py

def help():
    print "command--------detail"
    print "myrepos        show your repository"
    print "repo_info      show repository's infomation"
    print "mecab          use mecab. you will type string "
    print "exit           exit"

def myrepos():
    import myrepo

def exit():
    import sys
    sys.exit()

def repo_info():
    import repo_info

def mecab():
    import mecab

if __name__ == "__main__":
    menu = ""
    print"How to use ->help"
    while menu != "exit":
        menu = raw_input(">")
        if menu == "help":
            help()
        elif menu == "myrepos":
            myrepos()
        elif menu == "repo_info":
            repo_info()
        elif menu == "mecab":
            mecab()
        elif menu =="exit":
            exit()
        elif menu == "":
            pass #何もコマンドを入力しなければ何も起こらない
        else:
            print menu,"command is not exist."
            print "How to use ->help"

