import json
import pandas as pd
import requests


# define topic
topic="rhb"

# define directories and paths
input_file = "data/04_googlevision/%s.json" % topic
output_file= "data/05_order_labels/%s.csv" % topic

#create empty df
col_names = ['word', 'count']
labels_df = pd.DataFrame(columns=col_names)



# open json file
f1=open(input_file)
data1=json.load(f1)

print(data1)

for key in data1:
    print(key[0])
    print(key[1])
    new_row = {'word': key[0], 'count': key[1]}
    concordance_df = labels_df.append(new_row, ignore_index=True)


#write results to csv
labels_df.to_csv(output_file, encoding='utf-8')

#for key in sorted_labels:
    #print(key)


f1.close()