# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:08:57 2020

@author: ealegre

Word Cloud Generator
"""

import numpy as np
import pandas as pd
import nltk

# nltk.download('wordnet')

from wordcloud import WordCloud
from nltk.corpus import wordnet

import matplotlib.pyplot as plt

# Color function (H = 21 which gives orange)
def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 21.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

# Key word that will stop the user input prompt
SENTINEL = ""

# Instantiate the dictionary and synonym list
lst = dict()
synonym = []
prompt = "Please input the key words. Press the Enter key to stop: "

raw_input = input(prompt)

# Keep user input active until sentinel key is applied
while raw_input != SENTINEL:
    # Assign a fequency weight of 5 for the input values
    """
    This is still an issue that needs to be fixed. When the two dictionaries are merged into 
    word_lst, the weightings on the key word are still being overwritten. Please fix when 
    you have time
    """
    lst[raw_input] = 5
    
    # Pull all the synonyms from WordNet. Currently pulling literally any word with
    # a semblance of similarity.
    """
    Find a better approach that can be used to make the synonyms more
    relevant to the situation. Las time, we used raw_input.n.01 which is the first noun. Since
    the uses for these words are all adjectives, possibly try and incoroporate that
    """
    for syn in wordnet.synsets(raw_input):
        for l in syn.lemmas():
            synonym.append(l.name().lower())
    
    # Replace the _ in some of the words with a space, since that's how WordNet symbolizes space
    synonym = [w.replace('_', ' ') for w in synonym]
    
    # Give a frequency value to the new synonyms in their own dictionary
    add_syn = {key: 2 for key in synonym}
    

    # Compare the keywords with synonyms and pop off those words in the add_syn
    # dict if they exist there
    for key in lst.keys():
        if key in add_syn:
            add_syn.pop(key)
       
    # Merge the two dictionaries and capitalize the first letter
    word_lst = {**lst, **add_syn}
    word_lst = {k.title(): v for k,v in word_lst.items()}
    raw_input = input(prompt)




wordcloud = WordCloud(width=1000, height=500, prefer_horizontal=1, background_color="rgba(255,255,255,0)",mode='RGBA',relative_scaling=1, min_font_size=5, colormap="ocean").generate_from_frequencies(word_lst)

plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()