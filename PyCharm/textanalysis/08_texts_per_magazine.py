import json
import os
import pandas as pd



# define topic, either 'rhb' or 'lavaux'
topic="rhb"

# define directories and paths
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/03_language_year/%s' % topic
input_path = "data/03_language_year/%s/" % topic
output_file= "data/08_texts_per_magazine/count_%s.csv" % topic

count=0
dict_journals={}

for filename in os.listdir(directory):
    #logging number of loops
    print(count)
    count+=1
    #open file
    if filename.endswith(".json"):
        f = open(input_path+filename)
        data=json.load(f)
        #print(data)
        #print(data['journalTitle'])
        #print(data['authors'])
        if data['journalTitle'] in dict_journals:
            dict_journals[data['journalTitle']]+=1
        else:
            dict_journals[data['journalTitle']]=1



#convert dictionary into panda dataframe
journals_df=pd.DataFrame(dict_journals.items(), columns=["journals", "freq"])

print(journals_df)

#write results to csv for visualization with r
journals_df.to_csv(output_file, encoding='utf-8')

#save file as json for visualization with r
#with open(output_path, "w", encoding='utf-8') as outfile:
   # json.dump(dict_journals, outfile, ensure_ascii=False)

