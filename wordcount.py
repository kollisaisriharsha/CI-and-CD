file = open(r"/home/harsha/Downloads/test","r")
wordcount={}
for word in file.read().split():
	if word not in wordcount:
        	wordcount[word] = 1
    	else:
        	wordcount[word] += 1


for key in wordcount.keys():
    print [wordcount[key]].sort();
for key in wordcount.keys():
    print ("%s comes %s times" %(key , wordcount[key]))


print wordcount.keys()
