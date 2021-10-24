"""
Created on Sun Jun 28 15:15:42 2020
@author: grace
"""
import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import pandas as pd
from os import path
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    
    #list of words without punctuations
    
    newstring = '' #create new empty string to store string w/o punctuation
    lowercase = []
    
    list_words = file_contents.split()
    
    for word in list_words:
        word = word.lower()
        lowercase.append(word)
    
    for word in lowercase:
        for char in word:
            if char.isalpha() == True:
                continue
            elif char in punctuations:
                    word = word.replace(char,"")
                #print(word)
        newstring += word + ' '
        
    newlist1 = newstring.split()         

    #list of words without uninteresting words
    newlist2 = []
    for word in newlist1:
        if word in uninteresting_words:
            continue
        else:
            newlist2.append(word)
            
    #generate dictionary
    freq_dictionary = {} #define empty dictionary
    
    for word in newlist2:
        if word not in freq_dictionary: #add words into the dictionary
            freq_dictionary[word] = 1
        else:
            freq_dictionary[word] += 1
    


  
    #wordcloud
    emoji_mask = np.array(Image.open("wordcloud.py/netflix.png"))

    #def transform_format(val):
    #    if val == 0:
   #         return 255
  #      else:
 #           return val
    
#    transformed_emoji_mask = np.array((emoji_mask.shape[0],emoji_mask.shape[1]), np.int32)

    #for i in range(len(emoji_mask)):
     #   transformed_emoji_mask[i] = list(map(transform_format, transformed_emoji_mask[i]))

    cloud = wordcloud.WordCloud(background_color = 'white')
    
    cloud.generate_from_frequencies(freq_dictionary)
    return cloud.to_array()
    #.to_array()
    #return freq_dictionary


#file_contents = input('Enter text: ')
file_contents = input('Enter your file contents')



myimage = calculate_frequencies(file_contents)

plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
plt.savefig("new_wordcloud.png", format="png")

