import pickle

duff=3477

# deletions = 2846, 3251, 3382, 3466

corrections={}
corrections[3088]={}
corrections[3088]['TAGS'] = 'Technology,software,UNIX,programming,linux'
corrections[3088]['ANCHOR TEXT'] = 'KornShell'
corrections[3088]['DESCRIPTION'] = ''
corrections[3110]={}
corrections[3110]['TAGS'] = 'Technology,software,Tools,linux,opensource,UNIX,solaris,opensolaris,openssh'
corrections[3110]['ANCHOR TEXT'] = 'OpenSSH'
corrections[3110]['DESCRIPTION'] = ''
# need to show 3251
corrections[3477]={}
corrections[3477]['TAGS'] = 'World,Europe,economics,politics,author,academic'
corrections[3477]['ANCHOR TEXT'] = 'Jeremey Rifkin'
corrections[3477]['DESCRIPTION'] = ''
#print('all keys',corrections.keys)
#print('3088', corrections[duff])

dictfile = open('bookmarks.pickle','rb')

D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
K=[]; K = D.keys();         # the input dictionary keys
dictfile.close()


print (D[duff])
#print (D[duff]['TAGS'])

D[duff]['TAGS']= corrections[duff]['TAGS']
D[duff]['ANCHOR TEXT']= corrections[duff]['ANCHOR TEXT']

#print (D[duff])
#print (D[duff]['TAGS'])

#print (D[duff])

dictfile = open('bookmarks.pickle','wb')
pickle.dump(D,dictfile)
dictfile.close()

