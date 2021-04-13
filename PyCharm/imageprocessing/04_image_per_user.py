import geopandas as gpd
import pandas as pd
import json

#define which data to use, either 'rhb' or 'lavaux'
topic="rhb"

#define max. contributions per user
max_contributions = 100

#read in unesco shapefile
flickr_data = gpd.read_file("data/02_points_in_polygon/flickr/%s_flickr.shp" % topic)

#define output path
output_path= "data/03_image_per_user/%s.json" % topic

#show all columns of head
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#print(flickr_data.download_u[0])
print(flickr_data.head())

#initiate dictionary for count
dict_user={}

for i in range(0,len(flickr_data.user_nsid)):
   #print(flickr_data.user_nsid[i])
   if flickr_data.user_nsid[i] in dict_user:
       dict_user[flickr_data.user_nsid[i]]+=1

   else:
       dict_user[flickr_data.user_nsid[i]]=1

print(dict_user)
#save file as json for visualization with r
with open(output_path, "w", encoding='utf-8') as outfile:
    json.dump(dict_user, outfile, ensure_ascii=False)

#get users with more than 100 images
frequent_user = dict((k, v) for k, v in dict_user.items() if v >= max_contributions)

#get list with frequent users
freq_list=[]

for i in frequent_user:
    freq_list.append(i)

# get subset of data without frequent users
flickr_res = flickr_data[~flickr_data.user_nsid.isin(freq_list)]

#iterate through every frequent user nto add random rows
for user in frequent_user:
    #get data
    user_data = flickr_data[flickr_data.user_nsid == user]
    #print(user_data)
    #returns random rows of dataframe
    limited_flickr = user_data.sample(max_contributions)
    #append dataframe with random rows
    flickr_res=flickr_res.append(limited_flickr)

print(len(flickr_res))

#save data to shapefile
flickr_res.to_file(driver='ESRI Shapefile', filename='data/03_image_per_user/%s_flickr.shp' %topic)