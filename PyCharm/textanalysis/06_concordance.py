import json
import os
from nltk.tokenize import word_tokenize
from nltk.text import Text


# define topic, either 'rhb' or 'lavaux'
topic="rhb"

#define concondance search query
query="landschaft"

# define directories and paths
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/05_stop_words_tokenization/%s' % topic
input_path = "data/05_stop_words_tokenization/%s/" % topic
output_path= "data/06_concordance/%s_%s.json" % (topic,query)



#set count for logging
count=0


# create dictionary to count number of entries
concordance_dictionary={}

for filename in os.listdir(directory):
    #logging number of loops
    print(count)
    count+=1
    #open file
    if filename.endswith(".json"):
        f = open(input_path+filename)
        data=json.load(f)
        fulltext=data['fulltext']

        tokens = word_tokenize(fulltext)
        textlist = Text(tokens)

        #query concordance analysis
        #textlist.concordance(query)

        #concordance query for respective query
        con_list = textlist.concordance_list(query, width=250)


        for results in con_list:
            #get results of left side
            print(results.line)

            f = open("data/06_concordance/%s.txt" % topic, "a")


            f.write(results.line)
            f.write('\n')
            f.close()

            for i in results[0]:
                if i in concordance_dictionary:
                    concordance_dictionary[i]+=1
                else:
                    concordance_dictionary[i]=1
            #get results of right side
            for j in results[2]:
                if j in concordance_dictionary:
                    concordance_dictionary[j]+=1
                else:
                    concordance_dictionary[j]=1



# sort dictionary according to occurences
sorted_concordance = sorted(concordance_dictionary.items(), key = lambda kv: kv[1], reverse=True)

with open(output_path, "w", encoding='utf-8') as outfile:
    json.dump(sorted_concordance, outfile, ensure_ascii=False)

print(sorted_concordance)

