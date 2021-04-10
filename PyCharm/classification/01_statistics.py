import pandas as pd
import sklearn
from sklearn.metrics import cohen_kappa_score

#either 'rhb' or 'lavaux'
topic="lavaux"
#either 'landschaft' for text analysis or 'flickr' for image analysis
analysis = "flickr"
sample_limit = 10



#read in csv and fill empty values with "" s.t. no nan are present
flickr_df = pd.read_csv('data/%s_%s.csv' % (topic, analysis), sep=";").fillna("")


#read in csv
flickr_fabian_df = pd.read_csv('data/fabian/%s_%s.csv' % (topic, analysis), sep=";").fillna("")

flickr_fabian_df=flickr_fabian_df.drop_duplicates(subset=['word'])


#get first entries
subset_fabian=(flickr_fabian_df['subcategory'][0:sample_limit])

subset=(flickr_df['subcategory'][0:sample_limit])

#compute cohens kappa
kappa=sklearn.metrics.cohen_kappa_score(subset_fabian,subset)

print(subset)
print(subset_fabian)
print(kappa)