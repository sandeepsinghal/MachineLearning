__author__ = 'ssinghal'

import nltk
import operator
# compute frequence distribution of a data set

file = open("data.txt")
sentence = file.read()
words = sentence.split()
freq = nltk.FreqDist(words)

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))

for (k, v) in sorted_freq:
    print k , ":", v


#for key in sorted_freq.keys():
#    print key , ":", sorted_freq[key]

