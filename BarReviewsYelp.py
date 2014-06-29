import os
from os import listdir
from os.path import isfile, join
import re
file = "C:/Users/Rebecca/Desktop/oda/Bar/counts"
counts = open(file,"w+")
os.chdir("C:/Users/Rebecca/Desktop/oda/BI Class")
files=listdir("C:/Users/Rebecca/Desktop/oda/BI Class")
for file in files:
    bar = open(file,'r')
    date = "1/1/2011"
    pricey=0
    expensive=0
    for bline in bar: 
        if "datePublished" in bline:
            with open("C:/Users/Rebecca/Desktop/oda/Bar/counts",'a') as counts:
                counts.write("\n"+str(file)+"\t"+str(date.rstrip())+"\t "+str(pricey)+"\t "+str(expensive))
            print(str(file)+"\t"+str(date.rstrip())+"\t pricey:"+str(pricey)+"\t expensive:"+str(expensive))
            pricey=0
            expensive=0
            bline=bar.readline()
            bline=bar.readline()
            date=bline
        if "pricey" in bline:
            pricey = pricey+1
        if "expensive" in bline:
            expensive = expensive+1
