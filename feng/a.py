#!
# coding: UTF-8

import codecs

f = codecs.open("p.txt", "r", "utf-8")
con = f.readlines()

temp = "<dl class='dl-horizontal left-margin'>"
for index in range(0, len(con)):
    line = con[index].strip()
    if( line == "" ):
        temp += "</dl>\n"
        print(temp)
        temp = "<dl class='dl-horizontal left-margin'>"
    else:
        str = line[1: line.find(']')]
        temp += "<dt>[" + str + "]</dt>\n"
        p = line[line.find(']')+2: len(line)]
        temp += "<dd>" + p + "</dd>\n"
temp += "</dl>\n"
print(temp)