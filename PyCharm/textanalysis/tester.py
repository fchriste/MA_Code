import json
import pandas as pd
from IPython.display import display
import os

# define topic
topic="lavaux"

# define directories and paths
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/03_language_year/%s' % topic
input_path = "data/03_language_year/%s/" % topic
output_file = "data/08_texts_per_magazine/%s.csv" % topic

#initiate counter
count=0

#initiate empty dataframe
df = pd.DataFrame(columns=['id','articles', 'journalTitle', 'volYear', 'fulltext'])

#iterate through files
for filename in os.listdir(directory):
    #logging number of loops
    print(count)
    count+=1
    #open file
    if filename.endswith(".json"):
        f = open(input_path + filename)
        data = json.load(f)
        articles = data['articles']
        journalTitle = data['journalTitle']
        volYear = data['volYear']
        fulltext = data['fulltext']
        #append rows of dataframe with entries
        df=df.append({'id':filename,'articles': articles, 'journalTitle':journalTitle, 'volYear':volYear, 'fulltext':fulltext}, ignore_index=True)


#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', -1)

print("Dataframe Contens ",df,sep='\n' )
#print(df.groupby(['journalTitle']).count())

#write results to csv
df.to_csv(output_file, encoding='utf-8')