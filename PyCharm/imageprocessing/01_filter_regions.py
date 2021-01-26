import geopandas as gpd

#read in unesco shapefile
unesco = gpd.read_file("data/01_filter_regions/unesco_sites.shp/unesco_sites.shp")

#change coordinate system to wgs84
unesco_wgs84 = unesco.to_crs("EPSG:4326")

unesco_wgs84.to_file("data/01_filter_regions/unesco_sites.shp/unesco_polygons_wgs84.shp")

#check file and columns
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#print(unesco.head())

#filter rhb
rhb=unesco_wgs84[unesco_wgs84.bgdi_name == "Rhätische Bahn in der Landschaft Albula/Bernina"]

#filter lavaux
lavaux=unesco_wgs84[unesco_wgs84.bgdi_name == "Lavaux, Weinberg-Terrassen"]


#save geometry to shapefile
rhb.to_file("data/01_filter_regions/rhb/rhb_polygon.shp")
lavaux.to_file("data/01_filter_regions/lavaux/lavaux_polygon.shp")


