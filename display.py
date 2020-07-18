import pickle

duff=2846
#907, 885, 924,946, 947,965, 1047,1170, 1454,1457,1493,1593,1581,1582,1588,1806, 3242
queries=['3419']

dictfile = open('bookmarks.pickle','rb')
D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

K=[]; K = D.keys();         # the input dictionary keys

noofkeys=len(D)
print("No of entries", noofkeys)


for query in queries:
    print(int(query))
    print(int(query),D[int(query)])
    try:
        t=D[int(query)]['STATUS']
    except:
        print('Status Unset',D[int(query)]['HREF'])
    else:
        print(D[int(query)]['STATUS'],D[int(query)]['HREF'])



#print (D[duff])
#print (D[duff]['HREF'])

#pickle.dump(D,dictfile)

