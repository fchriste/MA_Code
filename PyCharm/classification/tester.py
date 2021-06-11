# Importing the required libraries
import pandas as pd



#either 'rhb' or 'lavaux'
topic="rhb"

#read in csv and fill empty values with "" s.t. no nan are present
data_df = pd.read_csv('data/%s.csv' % (topic), sep=",").fillna("")


print(data_df)

count=0

# Creating an empty Dataframe with column names only
dfObj = pd.DataFrame(columns=['id', 'articles', 'journalTitle', 'volYear', 'fulltext'])

# get number of articles containing the term landschaft
for i in range(0,len(data_df)):
    print(data_df['fulltext'][i])
    if 'landschaft' in data_df['fulltext'][i]:
        count+=1
        dfObj = dfObj.append({'id': data_df['id'][i], 'articles': data_df['articles'][i], 'journalTitle': data_df['journalTitle'][i], 'volYear': data_df['volYear'][i], 'fulltext':data_df['fulltext'][i]}, ignore_index=True)


print('Number of articles containing the term landschaft:')
print(count)

print(dfObj)

#write results to csv
dfObj.to_csv('data/articles_landschaft_%s.csv' %topic, encoding='utf-8')

