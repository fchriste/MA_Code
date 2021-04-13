import json
import pandas as pd
import os

# define topic, either 'rhb' or 'lavaux'
topic="rhb"

#define limit of articles / journal
limit = 25

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

#print("Dataframe Contens ",df,sep='\n' )


#group articles by journal
grouped_df = (df.groupby(['journalTitle']).count())
print(grouped_df)
#show most common journals
print(grouped_df.sort_values(by=['id'], ascending=False))

#iterate through rows of dataframe
for i, row in grouped_df.iterrows():
    #get number of articles per journal as integer
    article_count=int(row['id'])
    if article_count > limit:
        #get subset of articles of journal with high contribution rate
        limiting_df=df[df.journalTitle==i]
        #get random sample out of these articles
        limited_df = limiting_df.sample(limit)
        #drop all rows of the journal in the orginal dataframe
        df=df[df.journalTitle != i]
        #append dataframe with random sample
        df=df.append(limited_df, ignore_index=True)
        print(df)



#write results to csv
df.to_csv(output_file, encoding='utf-8')