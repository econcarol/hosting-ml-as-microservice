# Import libraries
import pickle
from flask import escape
from string import punctuation
from nltk import download
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download corpuses
download('punkt')
download('stopwords')

# Define feature extractor and bag-of-words converter
stopwords_eng = stopwords.words('english')

def extract_features(words):
    return [w for w in words if w not in stopwords_eng and w not in punctuation]

def bag_of_words(words):
    bag = {}
    for w in words:
        bag[w] = bag.get(w,0)+1
    return bag

# Import your pickled model file
model_file = open('sa_classifier.pickle', 'rb')
model = pickle.load(model_file)
model_file.close()

# Define a method for prediction
def get_sentiment(review):
    words = word_tokenize(review)
    words = extract_features(words)
    words = bag_of_words(words)
    return model.classify(words)

