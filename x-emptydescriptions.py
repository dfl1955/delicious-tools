import pickle

D = {};                     # the input dictionary
dictfile = open('bookmarks.pickle','rb')
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

K=[]; K = D.keys();         # the input dictionary keys
i=0
X=[]

for key in K:
    if D[key]['STATUS'] == 'OK':
        #print(key, D[key])
        try:
            s=D[key]['DESCRIPTION']
        except:
            #print(key, 'no description',D[key]['HREF'])
            X.append(key)
            i = i + 1
        else:
            pass

print ('%s bookmarks without description, to be deleted' %(str(i)))

for dead in X:
    del D[dead]
    print(dead,' deleted')


dictfile = open('bookmarks.pickle','wb')
pickle.dump(D,dictfile)
dictfile.close()

