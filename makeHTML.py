
# DFL 20/7/2020

# This program generates the HTL from the pickle stored dictionary

from html.parser import HTMLParser
import pickle

# open the dictionary file and assign to a dictionary

dictfile = open('bookmarks.pickle','rb')
D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

# set the working storage variables

K=[]; K = D.keys(); s=''; i=0

elementhtml='<div>\n<p><a href="%s">%s</a></p>\n<p>%s</p>\n<p>Tags: %s.</p>\n</div>\n'

print('Bookmark HTML Generator ... starts')
for key in K:
    if D[key]['STATUS'] == 'OK':
        print(key, D[key])
        tagline=D[key]['TAGS'].replace(',',', ')
        # do I need to HTMLise the ASCII code
        s=s+((elementhtml %(D[key]['HREF'],D[key]['ANCHOR TEXT'],D[key]['DESCRIPTION'],tagline)))
        i = i + 1

#print (s)

print ('%s bookmarks printed' %(str(i)))
print('Bookmark HTML Generator ... ends')
      
f = open('delicious-bookmarks.htm','w')
f.write(s)
f.close()
