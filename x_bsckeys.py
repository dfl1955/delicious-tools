# this program deltes the entired defined in bsckeys

from html.parser import HTMLParser
#import urllib.request
import pickle

dictfile = open('bookmarks.pickle','rb')
D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

ifile = open('bsckeys.pickle','rb')
K = []
K = pickle.load(ifile)
ifile.close()

for key in K:
    #print ('as found',key,D[key])
    del D[key]

dictfile = open('bookmarks.pickle','wb')
pickle.dump(D,dictfile)
dictfile.close()
