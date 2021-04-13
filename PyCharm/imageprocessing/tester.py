import os
import geopandas as gpd
import pandas as pd

# Imports the Google Cloud client library
from google.cloud import vision



#set environement variable for google vision api
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="data/My First Project-a3b8caea496a.json"

# define topic, either 'rhb' or 'lavaux'
topic="rhb"

# define directories and paths
input_file = "data/03_image_per_user/%s_flickr.shp" % topic
output_file= "data/04_googlevision/%s.csv" % topic

#read in flickr data of unesco region
#flickr_data = gpd.read_file(input_file)

#set url where image is found
uri="https://farm5.staticflickr.com/4074/4806172815_4dba9d34c2.jpg"

#open empty dictionary for labels
labels_dict={}

counter=0



# Instantiates a client
client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = uri

response = client.label_detection(image=image)
# get labels for images
labels = response.label_annotations
print('Labels:')

print(counter)
counter+=1
#count occurences of labels
for label in labels:
    print(label.description)
    if label.description in labels_dict:
        labels_dict[label.description]+=1
    else:
        labels_dict[label.description]=1


#create empty df
col_names = ['word', 'count']
labels_df = pd.DataFrame(columns=col_names)


#write dictionary in df
for key in labels_dict:
    new_row = {'word': key, 'count': labels_dict[key]}
    labels_df = labels_df.append(new_row, ignore_index=True)


#write results to csv
labels_df.to_csv(output_file, encoding='utf-8')



