import json
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


# define topic
topic="lavaux"

# define directories and paths
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/03_language_year/%s' % topic
input_path = "data/03_language_year/%s/" % topic
output_path= "data/05_stop_words_tokenization/%s/" % topic


#set stop words to german
stop_words = set(stopwords.words('german'))

#set count for logging
count=0

landschaft_counter=0

for filename in os.listdir(directory):
    #logging number of loops
    print(count)
    count+=1
    #open file
    if filename.endswith(".json"):
        f = open(input_path+filename)
        data=json.load(f)
        fulltext=data['fulltext']
        articles = data['articles']
        journalTitle = data['journalTitle']
        volYear = data['volYear']

        #convert text to lower case
        fulltext=fulltext.lower()
        #tokenize text
        tokenized_text = word_tokenize(fulltext)

        #tester: list[str] = nltk.word_tokenize(fulltext)
        fd = nltk.FreqDist(tokenized_text)
        landschaft_counter+=fd['Landschaft']

        new_file = {}
        new_fulltext =""

        #removing stop words
        for r in tokenized_text:
            if not r in stop_words:
                new_fulltext+=" "+r

        # save relevant data in dictionary
        new_file['articles'] = articles
        new_file['journalTitle'] = journalTitle
        new_file['volYear'] = volYear
        new_file['fulltext'] = new_fulltext

        # save new file
        with open(output_path + filename, "w", encoding='utf-8') as outfile:
            json.dump(new_file, outfile, ensure_ascii=False)


print("tell me")
print(landschaft_counter)


