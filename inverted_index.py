from html.parser import HTMLParser
from nltk.corpus import stopwords
import string
import html2text
import os
import re
import nltk
from nltk.stem import PorterStemmer
print("start")
temp=open(r"C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\termid.txt" , errors='ignore')
temp1=temp.read().split()
a={}
theFile=open(r'C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\term_index.txt')
mapping=theFile.read().split()

##--------------------------------with hashmaps
start=0
end=len(mapping)
for i in range (start,end):
    if start==end:
        break
    key = mapping[start]
    a.setdefault(key, [])
    start=start+1
    a[key].append(mapping[start])
    total=int(mapping[start])
    start=start+1
    a[key].append(mapping[start])
    for j in range (total):
        start=start+1
        a[key].append(mapping[start])
    start=start+1
print("end")
print("start")

porter = PorterStemmer()
txt = input("Enter the term for its inverted index\n")
txt=porter.stem(txt)
print("The entered term is : ", txt)
if txt in temp1:
    pos=temp1.index(txt)  
    print("Listing for term : ", txt)
    print("TermID : " ,temp1[pos-1])
    print("Number of documents containing term : ", a[temp1[pos-1]][1])
    print("Term frequency in corpus : " , a[temp1[pos-1]][0])
else:
    print("Sorry can't find such term")
print("end")
