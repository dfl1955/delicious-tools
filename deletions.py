import pickle

D = {};                     # the input dictionary
dictfile = open('bookmarks.pickle','rb')
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

K=[]; K = D.keys();         # the input dictionary keys

duff=3466
duffkey = [duff]
#duffhref=['http://www.consultantsboard.com/']

deletions=[885,907]
deletions=[924]; deletions=[946] ; deletions=[947]
deletions=[965]; deletions=[1047]; deletions=[1170]
deletions=[1454]
deletions=[1457]
deletions=[1493]
deletions=[1593]
deletions=[1581]
deletions=[1582]
deletions=[1588]
deletions=[1806]
deletions=[3242]
deletions=[3353]
deletions=[3419]
deletions=[3425]




for task in deletions:
    print (task)  
    print ('as found',D[task])
    del D[task]

dictfile = open('bookmarks.pickle','wb')
pickle.dump(D,dictfile)
dictfile.close()

