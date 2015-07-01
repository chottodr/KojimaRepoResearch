#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from pymongo import Connection

#generate DB instance
connect = Connection()
db = connect.test
col = db.commit
for doc in col.find({ "message": "first commit" }):
    print "{",
    print doc.values()
    #print "\n".join("%s: %s" % i for i in doc.items()),
    print "}\n"
