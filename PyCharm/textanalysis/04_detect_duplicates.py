
import json
import os

#function to create shingles with default ngram=5
def get_shingles(text, char_ngram=5):
    return set(text[head:head + char_ngram] for head in range(0, len(text) - char_ngram))

#function to calculate jaccard similarity
def jaccard(set_a, set_b):
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)

# define topic
topic="lavaux"

#define similarity percentage
similarity = 0.8

# define directories and paths
directory = r'/Users/fab/switchdrive/UZH/MA/Code/PyCharm/textanalysis/data/03_language_year/%s' % topic
input_path = "data/03_language_year/%s/" % topic
output_path= "data/04_duplicates/%s/" % topic



#inititate counter

count=0
result=[]

list=[]

#create list with all filenames

for filename in os.listdir(directory):
    # maybe hidden files in the folder, so only consider json
    if filename.endswith(".json"):
        list.append(filename)
    else:
        continue

print("This was the first loop")

# initiate two loops to get all pairings of files
for i in range(len(list)):
    for j in range(i+1, len(list)):
        result.append([list[i], list[j]])

print("this was the second loop")


print("----------------------------------------")


#logging: get how many loops there will be
print(len(result))

for i in range(len(result)):
    f1_name=result[i][0]
    f2_name=result[i][1]
    #print counter for logging
    print(count)
    #open first file
    f1=open(input_path+f1_name)
    data1=json.load(f1)
    #access text of first file
    f1_str = data1['fulltext']
    f1.close()
    #open secod file
    f2=open(input_path+f2_name)
    data2=json.load(f2)
    #access text of second file
    f2_str=data2['fulltext']
    #get shingles of first file
    a=(get_shingles(f1_str.lower()))
    #get shingles of second file
    b=(get_shingles(f2_str.lower()))
    #calculate jaccard similarity
    jaccard_similarity = jaccard(a, b)
    count+=1
    #put file on list if jaccard similarity higher than 0.8
    if jaccard_similarity>similarity:
        print("oh no!")
        print(jaccard_similarity)
        print(result[i])

        # create dictionary with duplicate files as key and score as value
        print(result[i])

        f = open("%s/duplicates.txt" % output_path, "w")
        # map out entries to include tabs tp get a more visible entry
        result[i] = map(lambda x: x + '\t', result[i])
        f.writelines(result[i])
        f.write(str(jaccard_similarity) + '\n')
        f.close()



