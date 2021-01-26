import geopandas as gpd
import pandas as pd


#define which data to use
topic="rhb"

#read in unesco shapefile
flickr_data = gpd.read_file("data/02_points_in_polygon/flickr/%s_flickr.shp" %  topic)

#show all columns of head
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(flickr_data.download_u[0])

for i in range(0,len(flickr_data.download_u)):
    print(flickr_data.download_u[i])
