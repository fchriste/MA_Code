import json
import os

#set topic of data, either 'rhb' or 'lavaux'
topic="rhb"

# define directories
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/01_get_data/%s' % topic
input_path = "data/01_get_data/%s/" % topic
output_path= "data/02_joined_files/%s/" % topic


# create empty dictionary
dict = {}
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # substring to compare the files, if this substring is the same, put them in the same list
        file_id = filename[:-8]
        # if file_id already in dictionary, add it to the list
        if file_id in dict.keys():
            dict[file_id].append(filename)
            # sort the list such that it is in the correct order
            dict[file_id].sort()
        # if file_id not in dictionary, add a new entry
        else:
            dict[file_id]=[filename]


    else:
        continue


print(dict)

#iterate through dictionary
for key in dict:
    #get list of respective articles for each key
    article_list=dict[key]
    print(article_list)
    #initiate counter to get first element of list
    counter=0
    for item in article_list:
        # open JSON file
        f = open(input_path+item, )
        # return data as dictionary
        data = json.load(f)
        # if first item in list, include metadata
        if counter ==0:
            # extract metadata to keep from article
            articles = data['articles']
            journalTitle = data['journalTitle']
            volYear = data['volumeNumYear']
            fulltext = data['fulltext']
            # close file
            f.close()
            # increase counter
            counter+=1
        # if further item in list, only append fulltext
        else:
            to_append = data['fulltext']
            fulltext = fulltext+to_append

        new_file={}
        # save relevant data in dictionary
        new_file['articles'] = articles
        new_file['journalTitle'] = journalTitle
        new_file['volYear'] = volYear
        new_file['fulltext'] = fulltext

    # create json file per key with the text of all items combined
    with open(output_path+key+".json", "w", encoding='utf-8') as outfile:
        json.dump(new_file, outfile, ensure_ascii=False)





