from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.text import Text
import pandas as pd


# define topic
topic="rhb"

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

texts_df = pd.read_csv(input_file)

#print dataframe
text=texts_df.loc[10]['fulltext']
print(texts_df.loc[0]['fulltext'])

new_fulltext =""
#removing stop words
print(text)
print("--------")
splited_text=text.split()
for r in splited_text:
    print(r)
    if not r in stop_words:
        new_fulltext+=" "+r
print(new_fulltext)
print(len(text))
print(len(new_fulltext))
print(stop_words)

tokens = word_tokenize(new_fulltext)
print("!!!!!!!")

textlist = Text(tokens)

con_list = textlist.concordance_list(query, width=250)
print(con_list)



