

from html.parser import HTMLParser
#import urllib.request
import pickle

# open the dictionary file and assign to a dictionary

dictfile = open('bookmarks.pickle','rb')
D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

bsckeys=[]

K=[]; K = D.keys();         # the input dictionary keys

for key in K:
    #if HREF contains bsc report else pass
    site=D[key]['HREF']
    try:
        site.index('blogs.sun.com')
    except:
        pass
    else:
        #print(key, site)
        bsckeys.append(key)

print (bsckeys)

ofile = open('bsckeys.pickle','wb')
pickle.dump(bsckeys,ofile)
ofile.close()

    
