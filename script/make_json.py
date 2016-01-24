#! usr/bin/env python
import os 
import sys
import json 

def type_json(path):
    files = os.listdir(path)
    json_data = []
    for FILE in files:
        #print "file unko"
        txt = open(path+"/"+FILE,"r")
        line = txt.read().split("\n")
        line.pop()
        #print line
        #print "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
        d = {}#data
        d['name'] = FILE.rstrip("_time.txt")
        d['dates'] = []
        for l in line:
            #print "line unko"
            date = l.split("[TIME]")[1].replace("-","/")
            date = date.rstrip(date[-5:]).strip(" ")
            print date
            d['dates'].append(date)
        json_data.append(d)
        txt.close()
    f = open("eventdata.json","w")
    json.dump(json_data,f)

    #json_data = {"name":"unko.py","total_line_changed":[[20150411,12]],"total_commit":[[20150411,1]],"line":[[20150411,12]]}
    #with open('test.json')
    

if __name__ =="__main__":
    path = sys.argv[1]
    type_json(path)


