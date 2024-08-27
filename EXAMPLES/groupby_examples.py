
from itertools import groupby

with open('../DATA/words.txt') as words_in:  # open file for reading
    # create generator of all words, stripped of the trailing '
    all_words = (w.rstrip() for w in words_in)  

    # create a groupby() object where the key is the first character in the word
    g = groupby(all_words, key=lambda e: e[0])  


    # for key, group
    for letter, group_of_words in g:
        print(letter, len(list(group_of_words)))
