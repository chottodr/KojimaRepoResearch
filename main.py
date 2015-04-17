#!/usr/bin/env python
# -*- coding: utf-8 -*-

def help():
    print "command--------detail"
    print "myrepos        show your repository"
    print "exit           exit"
def myrepos():
    import myrepo

def exit():
    import sys
    sys.exit()

if __name__ == "__main__":
    menu = ""
    print"how to use ->help"
    while menu != "exit":
        menu = raw_input(">")
        if menu == "help":
            help()
        elif menu == "myrepos":
            myrepos()
        elif menu =="exit":
            exit()


