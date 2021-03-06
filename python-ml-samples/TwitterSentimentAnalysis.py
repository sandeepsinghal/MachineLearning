# http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

import nltk

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

# For each tweet, check if the word is contained in feature list or not
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('I was very pretty', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('It was pretty annoying','negative')]

tweets = []

for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]

#array of all words in the tweet, sr
words_in_tweets = get_words_in_tweets(tweets)

# Distinct words with atleast 3 characters sorted by number of occurrences (frequency distribution of each word)
word_features = get_word_features(words_in_tweets)

# tweets has the important words in the tweet along with the sentiment
training_set = nltk.classify.apply_features(extract_features, tweets)

print training_set

classifier = nltk.NaiveBayesClassifier.train(training_set)

#print classifier.show_most_informative_features(32)


tweet = 'Larry is my friend'

print classifier.classify(extract_features(tweet.split()))


tweet = 'Your song is annoying'

print classifier.classify(extract_features(tweet.split()))
