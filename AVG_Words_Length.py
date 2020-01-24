# Python 2.7
# Average list of words
# Test cases
  # My name is antonio

# Solution 1
def avg_word_length(str):
    str = raw_input("Please enter a sentence: ")
    words = str.split()
    len_word = []
    for word in words:
        len_word.append(len(word))
    avg_len = float(sum(len_word)) / float(len(words))
    return avg_len

print(avg_word_length(str))

# Solution 2
from __future__ import division
def avg_word_length(sentence):
    sentence = raw_input("Please enter a sentence: ")
    words_list = sentence.split()
    avg = sum(len(word) for word in words_list) / len(words_list)
    print avg


avg_word_length()