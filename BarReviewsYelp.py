import os
from os import listdir
from os.path import isfile, join
import re
file = "C:/Users/Rebecca/Desktop/oda/Bar/counts"
counts = open(file,"w+")
os.chdir("C:/Users/Rebecca/Desktop/oda/BI Class")
#this folder contains text files of downloaded source code 
files=listdir("C:/Users/Rebecca/Desktop/oda/BI Class")
with open("C:/Users/Rebecca/Desktop/oda/Bar/counts",'a') as counts:
counts.write("date \t Bar \t comment")
for file in files:
print(file)
bar = open(file,'r')
date = "1/1/2011"
marker=0
for bline in bar: 
if "datePublished" in bline:
with open("C:/Users/Rebecca/Desktop/oda/Bar/counts",'a') as counts:
counts.write("\n"+str(date.rstrip())+"\t "+str(file)+"\t "+str(marker))
print("\n"+str(date.rstrip())+"\t "+str(file)+"\t "+str(marker))
marker=0
bline=bar.readline()
bline=bar.readline()
date=bline
lookfor = ["pricey","expensive","costly","cost","price"]
for match in lookfor:
if match in bline:
marker = marker+1
#this file is prepped for the BarReviewsYelp.R file in the R repository
