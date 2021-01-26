import json
import os
from langdetect import detect
import re

# define topic
topic="suonen"
#get year of unesco heritage nomination
unesco_year=2020

# define directories and paths
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/02_joined_files/%s' % topic
input_path = "data/02_joined_files/%s/" % topic
output_path= "data/03_language_year/%s/" % topic


#inititate counter
de=0
other=0
count=0
older=0
newer=0


for filename in os.listdir(directory):
    #logging number of loops
    print(count)
    count+=1
    if filename.endswith(".json"):
        f = open(input_path+filename)
        data=json.load(f)
        #detect language
        detected_language = detect(data['fulltext'])
        #continue when language == german
        if detected_language=='de':
            de+=1
            #find year of article in metadata
            volYear=data['volYear']
            volYear_split=volYear.split(" ")
            # extract part of string which contains year
            year_str=volYear_split[-1]
            print(filename)
            print(year_str)
            #use regex to extract number from entry
            year = re.findall("\d+", year_str)[0]
            #change type of year from str to int
            year=int(year)
            #save articles from before unesco nomination
            if year < unesco_year:
                older+=1
                with open(output_path + filename, "w", encoding='utf-8') as outfile:
                    json.dump(data, outfile, ensure_ascii=False)
            else:
                newer+=1

        else:

            other+=1
    else:
        continue




print("german articles: %d" % de)
print("other languagues: %d" % other)
print("articles before unesco: %d" %older)
print("articles after unesco: %d" %newer)