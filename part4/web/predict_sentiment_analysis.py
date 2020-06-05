# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import pickle
from string import punctuation
from flask import escape
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

# Import your pickled model file (non-Colab version)
if not 'google.colab' in sys.modules:
    model_file = open('sa_classifier.pickle', 'rb')
    model = pickle.load(model_file)
    model_file.close()

# Define a method for prediction
# This is the function to deploy
def get_sentiment(review):
    #request_json = request.get_json(silent=True)
    #request_args = request.args
    
    #if request_json and 'name' in request_json:
    #    review = request_json['name']
    #elif request_args and 'name' in request_args:
    #    review = request_args['name']
    #else:
    #    review = 'Great movie!'

    words = word_tokenize(review)
    words = extract_features(words)
    words = bag_of_words(words)

    return model.classify(words)

