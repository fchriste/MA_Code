import pandas as pd
import sklearn
from sklearn.metrics import cohen_kappa_score

#either 'rhb' or 'lavaux'
topic="lavaux"
#either 'landschaft' for text analysis or 'flickr' for image analysis
analysis = "landschaft"
# level of granularity, 'category' or 'subcategory'
level = 'subcategory'

# number of entries taken for comparison
sample_limit = 80




#read in csv and fill empty values with "" s.t. no nan are present
data_df = pd.read_csv('data/%s_%s.csv' % (topic, analysis), sep=";").fillna("")

data_df=data_df.drop_duplicates(subset=['word'])


#read in csv
data_fabian_df = pd.read_csv('data/fabian/%s_%s_f.csv' % (topic, analysis), sep=";").fillna("")
# drop duplicate entries
data_fabian_df=data_fabian_df.drop_duplicates(subset=['word'])


#get first entries
subset_fabian=(data_fabian_df[level][0:sample_limit])

subset=(data_df[level][0:sample_limit])

#compute cohens kappa
kappa=sklearn.metrics.cohen_kappa_score(subset_fabian,subset)

print(subset)
print(subset_fabian)
print(kappa)
