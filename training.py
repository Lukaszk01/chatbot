import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD


lemmatizer = WordNetLemmatizer
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
intents = json.loads(open('intents').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in self.intents['intents']:
    for pattern in intent['patterns']:
        word = nltk.word_tokenize(pattern)
        self.words.extend(word)
        documents.append((word, intent['tag']))
        if intent['tag'] not in self.classes:
            self.classes.append(intent['tag'])

print(documents)

