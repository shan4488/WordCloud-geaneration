from wordcloud import *


# Text file location in the pc with the extension .txt
# The text file is taken from "Alice in the wonderland" book.
# Add your file location
# Add your stopword_list
file_object = open(r"C:\Users\HARSHITHA-SHETTY\wordcloud.txt", "r+")

# function to remove special characters like !@#$%^&*


def special_char_remover(file_object):
    my_file_list = []
    for line in file_object:
        lst = line.split()
        for word in lst:
            strings = ""
            for character in word:
                if character.isalpha():
                    strings += character
            my_file_list.append(strings)
    return my_file_list

# function to remove unwanted words
# This function combines inbuilt STOP WORD list with our list of stop word


def stopword_remover(processed_list, stopword_list):
    pure_words = []
    stopword_list.extend(list(STOPWORDS))
    for word in processed_list:
        if word not in stopword_list:
            pure_words.append(word)
    return pure_words

# This generates a dictionary which contains the count of the words in the text file


def frequency_dictionary(processed_text_list):
    frequencies = {}
    for word in processed_text_list:
        if word not in frequencies.keys():
            frequencies[word] = 1
        else:
            frequencies[word] += 1
    return frequencies


stopword_lists = ["Alice", "suddenly", "Rabbit", "In", "The", "went", "never", "across", "nothing",
                  "took", "oh", "Oh", "I", "much", "So", "without"]
textlist = special_char_remover(file_object)
pure_text = stopword_remover(textlist, stopword_lists)
dictionary = frequency_dictionary(pure_text)
cloud = WordCloud(background_color="black")
cloud.generate_from_frequencies(dictionary)
cloud.to_file("shannew.png")
file_object.close()
