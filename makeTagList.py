import pickle

# a pickle example

dictfile = open('bookmarks.pickle','rb')
#dictfile.close()

D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

del D[3251]
del D[3382]
del D[3477]

K=[]; K = D.keys();         # the input dictionary keys
T = {} ;                    # the output dictionary, T for Tags

for e in K:                 # for all keys in K
    if D[e]['STATUS'] == 'OK':
        #print (e, D[e]['TAGS']); # writes the keyed tag list
        if ( int(D[e]['TAGS'].find(',')) > 0 ):  # if no commas, we have an empty tag iist
            words = D[e]['TAGS'].split(',')
            for w in words:
                if not ( w == [''] ):
                    if w in T:     # to see if key w is present in dict T
                        T[w] = T[w] + [e]
                    else:
                        T[w]=[e]
                else:
                    print ('Null tag found')

# dict T holds the tags and their associated keys from K

for s in ['uru','html','London','brussels','bruxelles']:
    print (s,T[s])


output_db = open("tags.pickle","wb")
pickle.dump(T,output_db)
output_db.close()
print ("file ./tags.pickle created")

# i could save this to another pickle db or write out the RSS files I want

# rss <item><title><link><description></item>

  


        


