
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sn

#define which data to use, either 'rhb' or 'lavaux'
topic="lavaux"

#read in unesco shapefile
polygon = gpd.read_file("data/01_filter_regions/%s/%s_polygon.shp" % (topic, topic))

#read in csv
pip_data = gpd.read_file('data/02_points_in_polygon/flickr/%s_flickr.shp' % topic)



#find points in polygon



print(pip_data)

#for index, row in pip_data.iterrows():
    #print(row.geometry.centroid.x)
    #print(row.geometry.centroid.y)


#plot data with points in polygon
fig, ax = plt.subplots()
polygon.plot(ax=ax, facecolor='gray');
pip_data.plot(ax=ax, color='gold', markersize=2);
plt.tight_layout();

plt.show()

fig, ax = plt.subplots()
sn.kdeplot(pip_data.geometry.centroid.x, pip_data.geometry.centroid.y,color='blue',shade=True, cbar=True)
polygon.plot(ax=ax, facecolor=(0.1,0.1,0.1,0), edgecolor='black');
plt.xlabel('Northing [°]')
plt.ylabel('Easting [°]')
#pip_data.plot(ax=ax, color='gold', markersize=0.1);
#plt.show()

#save plot to png
plt.savefig('data/07_kde_plots/kde_%s.png' %topic)