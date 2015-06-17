#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from pymongo import Connection

#generate DB instance
connect = Connection('localhost',27017)
db = connect.test
col = db.commit
for doc in col.find():
    print "{",
    print "\n".join("%s: %s" % i for i in doc.items()),
    print "}\n"
