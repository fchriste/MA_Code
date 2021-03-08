from nltk.corpus import stopwords
import pandas as pd
import nltk


# define topic
topic="lavaux"

#define concondance search query
query="landschaft"

# define directories and paths
input_file = "data/08_texts_per_magazine/%s.csv" % topic
output_file= "data/10_concordance/%s_%s.csv" % (topic,query)


#set count for logging
count=0

#set stop words to german
stop_words = set(stopwords.words('german'))


# create dictionary to count number of entries
concordance_dictionary={}
#read file into dataframe
texts_df = pd.read_csv(input_file)

for text in texts_df.fulltext:
    print(text)
    # tokenize text
    tokenized_text = nltk.word_tokenize(text)
    # turn all the words in lower case and only keep text
    alpha_tokenized = [w.lower() for w in tokenized_text if w.isalpha()]
    #initiate empty list
    new_fulltext = []
    #iterate through tokenized text to remove stopwords
    for i in alpha_tokenized:
        print(i)
        if i not in stop_words:
            print(i)
            new_fulltext.append(i)
    # get some further information about the data like most common words
    fd = nltk.FreqDist(new_fulltext)
    #count how many times landschaft appears in this text
    print(fd["engadin"])
    #show 3 most common words in this text
    print(fd.most_common(3))

    #convert new full text into text for concordance analysis
    fulltext_Text = nltk.Text(new_fulltext)
    con_list = fulltext_Text.concordance_list("landschaft", lines=5)

    for entry in con_list:
        print(entry)
        print(str(entry.left))
        # write respective lines in text file for check
        f = open("data/10_concordance/%s.txt" % topic, "a")
        f.write(entry.line)
        f.write('\n')
        f.close()

        # create empty df
        col_names = ['word', 'count']
        concordance_df = pd.DataFrame(columns=col_names)

        for i in entry.left:
            if i in concordance_dictionary:
                concordance_dictionary[i] += 1
            else:
                concordance_dictionary[i] = 1
        # get results of right side
        for j in entry.right:
            if j in concordance_dictionary:
                concordance_dictionary[j] += 1
            else:
                concordance_dictionary[j] = 1


#convert dictionary to df
for key in concordance_dictionary:
    print(key,'  :  ', concordance_dictionary[key])
    print('---')
    new_row = {'word': key, 'count': concordance_dictionary[key]}
    concordance_df = concordance_df.append(new_row, ignore_index=True)


#write results to csv
concordance_df.to_csv(output_file, encoding='utf-8')