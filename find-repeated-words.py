#!/usr/bin/env python

from string import punctuation
from operator import itemgetter

N = 10
words = {} # Dict of word frequencies
pos = {} # Dict of word positions
scores = [] # List of word repeatedness scores
articles = ['the', 'a', 'of', 'and', 'in', 'et', 'al'] # Common articles to ignore

# Build lists

words_gen = (word.strip(punctuation).lower() for line in open('test')
                                             for word in line.split())

i = 0
for word in words_gen:
    words[word] = words.get(word, 0) + 1

    # Build a list of word positions
    if words[word] == 1:
        pos[word] = [i]
    else:
        pos[word].append(i)

    i += 1

# Calculate scores

words_gen = (word.strip(punctuation).lower() for line in open('test')
                                             for word in line.split())

i = 0
for word in words_gen:
    scores.append(0)
#    scores[i] = -1 + sum([pow(2, -abs(d-i)) for d in pos[word]]) # The -1 accounts for the 2^0 for self words
    if word not in articles and len(word) > 2:
        for d in pos[word]:
            if d != i and abs(d-i) < 50:
                scores[i] += 1.0/abs(d-i)
    i += 1

scores = [score*1.0/max(scores) for score in scores] # Scale from 0 to 1

# Write colored output

f = open('test.html', 'w');
i = 0
for line in open('test'):
    for word in line.split():
        f.write('<span style="background: rgb(%i, 255, 255)">%s</span> ' % ((1-scores[i])*255, word))
        i += 1
    f.write('<br /><br />')
f.close()
