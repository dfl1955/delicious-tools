# DFL 16/07/2020

# this version 1.1 and did most of the work

from html.parser import HTMLParser
import urllib.request
import pickle

# open the dictionary file and assign to a dictionary

dictfile = open('bookmarks.pickle','rb')
D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

K=[]; K = D.keys();         # the input dictionary keys

# needs to use the checkpoint code, in chunks of 50

successunit=5;  # success unit definition
g = open('ctr.txt','r')
d = int(g.read())
g.close()

e = d + successunit
counter = e
print(d, e)

for element in range(d,e):
    #for element in 1,2,3:
    print (element)
    try:
        site=D[element]['HREF']
    except:
        print('Skipping key code. ',element)
    else:
        site=D[element]['HREF']
        #print (site)
        # if STATUS unset, fetch the URL and set a STATUS depending on result
        try:
            t=D[int(query)]['STATUS']
        except:
            try:
                u=urllib.request.urlopen(site)
            except:
                D[element]['STATUS']="N/A"
            else:
                D[element]['STATUS']="OK"
        else:
            pass
        print (D[element]['STATUS'], site)

f = open('ctr.txt','w')
f.write(str(counter))
f.close()

# writes out the amended dictionary

dictfile = open('bookmarks.pickle','wb')
pickle.dump(D,dictfile)
dictfile.close()
    
    

