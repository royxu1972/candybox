# coding=utf-8

from export import paper

# do export
p = paper()
p.get_first_author()

'''
import os

path = "C:\\Users\\Huayao\\Desktop\\All"
for root, dir, list in os.walk(path):   
	# root遍历路径，dirs当前遍历路径下的目录，list当前遍历目录下的文件名  
    for i in list:
    	pos = i.index('.')
    	name = i[pos+1:]
    	
    	print(name)
    	os.rename(path+"\\"+i, path+"\\"+name)
'''