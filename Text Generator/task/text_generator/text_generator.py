# Write your code here
import random
from re import match

import nltk
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter

# f = open("corpus.txt", "r", encoding="utf-8")
f = open(str(input()), "r", encoding="utf-8")

wt = WhitespaceTokenizer()
tokens = wt.tokenize(f.read())
bigrm = list(nltk.trigrams(tokens))

dictionary = {}
for el in bigrm:
    dictionary.setdefault(' '.join([el[0], el[1]]), []).append(el[2])

for k, v in dictionary.items():
    dictionary[k] = dict(Counter(v))

head = ''
for i in range(10):
    while not match(r'^[A-Z].*[^.?!] .+[^.?!]$', head):
        head = list(dictionary.keys())[random.randint(0, len(dictionary))]
    sentence = head.split()

    while True:
        try:
            tails = []
            weights = []
            for k, v in dictionary[head].items():
                tails.append(k)
                weights.append(v)
            tail = ''.join(random.choices(tails, weights))
            sentence.append(tail)

            head = ' '.join(sentence[-2:])

            if len(sentence) >= 5 and sentence[-1][-1] in '.?!':
                break

        except KeyError:
            print('Key Error. The requested word is not in the model. Please input another word.')
            break

    print(' '.join(sentence))

