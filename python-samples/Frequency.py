__author__ = 'ssinghal'

import nltk
import operator
from nltk.corpus import stopwords


# compute frequence distribution of a data set

file = open("data.txt")
sentence = file.read().lower()

word_list = sentence.split()

#remove stop words
filtered_words = [word for word in word_list if word not in stopwords.words('english')]

freq = nltk.FreqDist(filtered_words)

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))

for (k, v) in sorted_freq:
    print k , ":", v

