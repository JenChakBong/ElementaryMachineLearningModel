import math
import string
import nltk
import os
from collections import Counter
from nltk.stem.porter import *


def str_replace(str_source,char,*words):
    str_temp = str_source
    for word in words:
        str_temp = str_temp.replace(word,char)
    return str_temp

def str_split(str_source):
    str_temp = str_source.lower()
    str_list = str_temp.split(' ')
    return str_list


def tf(word,unfiltered):
    return unfiltered[word]/sum(unfiltered.values())

def n_containing(word,count_list):
    return sum(1 for unfiltered in count_list if word in unfiltered)

def idf(word,count_list):
    return math.log(len(count_list)/(1+n_containing(word,count_list)))

def tfidf(word,unfiltered,count_list):
    return tf(word,unfiltered)*idf(word,count_list)

dic={}
dirs = 'C:/Users/cs/Desktop/新建文件夹'
os.chdir(dirs)
file_list = os.listdir(dirs)
for i, filename in enumerate(file_list,1):
    f = open(filename,'r')
    str_source = f.read()
    str_temp = str_replace(str_source,' ','\t','\n',',','.','?','!')#符号按需求调整
    dic[i] = str_temp
    del str_source
content = list(dic.values())
for key,value in dic.items():
    str_source = value
    str_list = str_split(str_source)
    unfiltered = Counter (str_list)
    scores = {word :tfidf(word,unfiltered,content) for word in unfiltered}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print (unfiltered)
    for word, score in sorted_words[:5]:
        print('\tWord: {}, TF-IDF: {}'.format(word, round(score, 5)))
    print('--------------------------')
