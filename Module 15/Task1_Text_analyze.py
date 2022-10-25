# Write a program that receives a file name from the user, opens this file in the current directory,
# reads it and outputs two words: the most common of those that have a size of more than three characters,
# and the longest word in English.
# The file is expected to contain mixed text in two languages — Russian and English.

import string

#file_name = input('Type a name of a text file to open in current directory: ')

file_name = 'Into_the_Unknown.txt' # Let's try with this particular file

with open(file_name, encoding='utf8') as f:
    text = f.read() # Reading the text from file to string

text = text.lower() # Replace all the uppercase letters
for c in text: # Getting rid of punctuation
    if c in string.punctuation:
        text = text.replace(c, "")

text_list = text.split() # Convert the text to a list of words

words_set = set(text_list) # Make a set of unique words
words_counter = dict.fromkeys(words_set, 0) # Make a dictionary to further count the occurrence of each word

longest_english_word = '' # First step to find the largest word.

for word in text_list: # Move through the text from word to word
    if len(word) <= 3:
        if word in words_counter.keys():
            words_counter.pop(word) # Remove from the dictionary words shorter than 3 letters
        else: pass
    else:
        words_counter[word] += 1 # Add 1 to a counter for a word in dictionary

print(words_counter)

sorted_list = sorted(words_counter.items(), key=lambda x: -x[1]) # Sort the dictionary items by the values

i = 0
while sorted_list[i][1] == sorted_list[0][1]: # Print the words with the biggest number of occurrence.
    print(f"""The most common word longer then 3 letters is '{sorted_list[i][0]}'. It occurs {sorted_list[0][1]} times.""")
    i += 1
