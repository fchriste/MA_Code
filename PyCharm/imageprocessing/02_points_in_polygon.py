import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import shapely.speedups
import matplotlib.pyplot as plt

#define which data to use
topic="rhb"

#read in unesco shapefile
polygon = gpd.read_file("data/01_filter_regions/%s/%s_polygon.shp" % (topic, topic))

#plot the polygon
#fig, ax = plt.subplots()

#rhb.plot(ax=ax, facecolor='gray');

#plt.tight_layout();
#plt.show()

#read in csv
flickr_df = pd.read_csv('data/02_points_in_polygon/flickr/data100m_Switzerland.csv', sep=";")

#show first lines
print(flickr_df.head())

#define point geometry
geometry = [Point(xy) for xy in zip(flickr_df.lng, flickr_df.lat)]

#define geodataframe
flickr_geo_df = gpd.GeoDataFrame(flickr_df, crs="EPSG:4326", geometry=geometry)


#enable speedups for faster spatial queries
shapely.speedups.enable()

#union of buffer geometry and region geometry
polygon_union = polygon.geometry.unary_union

#point in polygon calculation, result: booleans
pip_mask = flickr_geo_df.within(polygon_union)

#find points in polygon
pip_data = flickr_geo_df.loc[pip_mask]
print(pip_mask)
print(pip_data)


#plot data with points in polygon
fig, ax = plt.subplots()
polygon.plot(ax=ax, facecolor='gray');
pip_data.plot(ax=ax, color='gold', markersize=2);
plt.tight_layout();
plt.show()

#save data to shapefile
pip_data.to_file(driver='ESRI Shapefile', filename='data/02_points_in_polygon/flickr/%s_flickr.shp' %topic)

