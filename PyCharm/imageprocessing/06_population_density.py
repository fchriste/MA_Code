import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import shapely.speedups
import matplotlib.pyplot as plt

#define which data to use, either 'rhb' or 'lavaux'
topic="lavaux"

#read in unesco shapefile
polygon = gpd.read_file("data/01_filter_regions/%s/%s_polygon.shp" % (topic, topic))

#plot the polygon
#fig, ax = plt.subplots()

#rhb.plot(ax=ax, facecolor='gray');

#plt.tight_layout();
#plt.show()

#read in csv
pop_df = pd.read_csv('data/01_filter_regions/STATPOP2019.csv', sep=",")

#show first lines
print(pop_df.head())

#define point geometry
geometry = [Point(xy) for xy in zip(pop_df.E_KOORD, pop_df.N_KOORD)]

#define geodataframe
pop_geo_df = gpd.GeoDataFrame(pop_df, crs="EPSG:2056", geometry=geometry)

pop_geo_df=pop_geo_df.to_crs("EPSG:4326")



#enable speedups for faster spatial queries
shapely.speedups.enable()

#union of buffer geometry and region geometry
polygon_union = polygon.geometry.unary_union

#point in polygon calculation, result: booleans
pip_mask = pop_geo_df.within(polygon_union)

#find points in polygon
pip_data = pop_geo_df.loc[pip_mask]
print(pip_mask)
print(pip_data)


#plot data with points in polygon
fig, ax = plt.subplots()
polygon.plot(ax=ax, facecolor='gray');
pip_data.plot(ax=ax, color='gold', markersize=2);
plt.tight_layout();

plt.show()

total_pop = pip_data['B19BTOT'].sum()

print("this is the total population in the region")
print(total_pop)