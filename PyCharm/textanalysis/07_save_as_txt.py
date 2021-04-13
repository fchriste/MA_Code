import json
import os


# define topic, either 'rhb' or 'lavaux'
topic="rhb"
#get year of unesco heritage nomination
unesco_year=2008

# define directories and paths
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/03_language_year/%s' % topic
input_path = "data/03_language_year/%s/" % topic
output_path= "data/07_save_as_txt/%s/" % topic


#inititate counter
de=0
other=0
count=0
older=0
newer=0

#this is a test whether the git repository now works


for filename in os.listdir(directory):
    #logging number of loops
    print(count)
    count+=1
    if filename.endswith(".json"):
        f = open(input_path+filename)
        data=json.load(f)
        #detect language
        print((data['fulltext']))
        #continue when language == german
        f = open("%s/%s.txt" % (output_path,filename), "w")
        f.write((data['fulltext']))


    else:
        continue

