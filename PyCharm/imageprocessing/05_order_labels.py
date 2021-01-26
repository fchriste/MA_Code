import os
import json
import geopandas as gpd
import pandas as pd



# define topic
topic="lavaux"

# define directories and paths
input_file = "data/04_googlevision/%s.json" % topic
output_file= "data/05_order_labels/%s.json" % topic

# open json file
f1=open(input_file)
data1=json.load(f1)

# sort dictionary according to occurences
sorted_labels = sorted(data1.items(), key = lambda kv: kv[1], reverse=True)



#write dictionary in json
with open(output_file, "w", encoding='utf-8') as outfile:
    json.dump(sorted_labels, outfile, ensure_ascii=False)


print(sorted_labels)
f1.close()