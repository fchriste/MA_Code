
from nltk.tokenize import word_tokenize
from nltk.text import Text
import pandas as pd


# define topic
topic="lavaux"

#define concondance search query
query="landschaft"

# define directories and paths
input_file = "data/08_texts_per_magazine/%s.csv" % topic
output_file= "data/10_concordance/%s_%s.csv" % (topic,query)


#set count for logging
count=0
landschaft_count=0


# create dictionary to count number of entries
concordance_dictionary={}
texts_df = pd.read_csv(input_file)

#print dataframe
print(texts_df)

#loop over articles
for text in texts_df.fulltext:
    tokens = word_tokenize(text)
    textlist = Text(tokens)
    con_list = textlist.concordance_list(query, width=250)
    print('now--------')
    print(con_list)
    if con_list!=[]:
        landschaft_count+=1
    count+=1



    for results in con_list:
        # get results of left side
        #print(results.line)
        #write respective lines in text file for check
        f = open("data/10_concordance/%s.txt" % topic, "a")
        f.write(results.line)
        f.write('\n')
        f.close()



        #create empty df
        col_names = ['word', 'count']
        concordance_df = pd.DataFrame(columns=col_names)

        for i in results[0]:
            if i in concordance_dictionary:
                concordance_dictionary[i] += 1
            else:
                concordance_dictionary[i] = 1
        # get results of right side
        for j in results[2]:
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

print('vorkommen landschaft')
print(landschaft_count)