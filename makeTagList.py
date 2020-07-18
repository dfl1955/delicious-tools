import pickle

# a pickle example

dictfile = open('bookmarks.pickle','rb')
#dictfile.close()

D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
K=[]; K = D.keys();         # the input dictionary keys
T = {} ;                    # the output dictionary, T for Tags

#for e in [1,2,3,4]:
for e in K:                 # somehow this doesn't work
    #print (e, D[e]['TAGS']); # writes the keyed tag list
    if ( int(D[e]['TAGS'].find(',')) > 0 ):  # if no commas, we have an empty tag iist
        words = D[e]['TAGS'].split(',')
        for w in words:
            if not ( w == [''] ):
                #print (e, w); # writes the inverted list index
                if w in T:          # to see if key w is present in dict T
                # print w, ' found at element ', e
                    T[w] = T[w] + [e]
                else:
                # print w, ' NOT found at element ', e
                    T[w]=[e]
            else:
                print ('Null tag found')
  
print ('word=forum', T.get('forum'))

#for each word in T, make a list holding numbers and anchor text    
#print (T.keys())

# print T

# print (D.keys())
#print D[1]
#print D[2]

        


