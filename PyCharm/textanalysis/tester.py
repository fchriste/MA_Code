from nltk.corpus import stopwords
import pandas as pd
import nltk
import spacy.cli



# define topic
topic="lavaux"

#define concondance search query
query="landschaft"

# define directories and paths
input_file = "data/08_texts_per_magazine/%s.csv" % topic
input_file2 = "data/07_save_as_txt/rhb/hoc-001%3A2005%3A18%3A%3A.json.txt"
output_file= "data/10_concordance/%s_%s.csv" % (topic,query)


#set count for logging
count=0

#set stop words to german
stop_words = set(stopwords.words('german'))

# set language to german for lemmatization
spacy.cli.download("de_core_news_md")
nlp = spacy.load('de_core_news_md')

# create dictionary to count number of entries
concordance_dictionary={}
#read file into dataframe
f = open(input_file2, 'r')
text=f.read()

tokenized_text = nltk.word_tokenize(text)
alpha_tokenized = [w.lower() for w in tokenized_text if w.isalpha()]
# initiate empty list
new_fulltext = []
# iterate through tokenized text to remove stopwords
for i in alpha_tokenized:
    if i not in stop_words:
        # lemmatize tokens
        doc = nlp(i)
        y = ' '.join([x.lemma_ for x in doc])
        # write lemmas in new fulltext
        new_fulltext.append(y)




# get some further information about the data like most common words
fd = nltk.FreqDist(new_fulltext)
#count how many times landschaft appears in this text
print(fd["landschaft"])
#show 3 most common words in this text
print(fd.most_common(3))



#convert new full text into text for concordance analysis
fulltext_Text = nltk.Text(new_fulltext)
con_list = fulltext_Text.concordance_list("landschaft", width=79, lines=1)


print('+++++++++++')
print(con_list)
print('++++++++')

for entry in con_list:
    print("-------")
    print(str(entry.left))
    print(str(entry.right))
    print(entry.line)

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



