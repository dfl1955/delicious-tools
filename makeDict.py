
# DFL 15 Jul 2020

from html.parser import HTMLParser
# import urllib
import pickle

#
# This program reads a delicious output file and loads the elements into a dictionary

html = HTMLParser()

linksfile = open("deliciouslinks.html","r")
linkasstring = linksfile.read()
linkaslist = linkasstring.split('<DT>')
numelements = len(linkaslist) - 2

linkdict={}     # this mut be declared before the loop

attributes=["HREF","ADD_DATE", "PRIVATE", "TAGS", "ANCHOR TEXT", "DESCRIPTION", "STATUS"]

o = 1           # this will be the dictionary index primary key
linkdict = {}
linkdict[0] = {} # needs two statements to create a 2D dictionary

print ("delicious link dictionary builder ... starts")

for element in linkaslist[1:numelements]:
    linkdict[o]={}
    # print o
    for ao in 0,1,2,3:
        i = element.index(attributes[ao],0)
        try:
            j = element.index(" ",i)
        except:
            pass
        else:
            # somehow this permits the passing of ' ' as a tag
            thisatt=element[i:j].split('"')
            # if ao = 0 then test for url ok
            linkdict[o][attributes[ao]]=thisatt[1]
    ao=4;                   # Now we do the anchortext
    i=j; j=element.index('</A>')
    linkdict[o][attributes[ao]]=element[i:j].strip()
    ao=5                    # Now we do the description
    # this doesn't seem to be handling missing descriptions well
    try:
        i=element.index('<DD>') + 4
    except:
        pass
    else:
        description=element[i:].strip()
        #d=html.unescape(description)
        linkdict[o][attributes[ao]]=description # do I hold the html or ascii
    o = o + 1

print (o, "cases processed.")
del linkdict[0]

#print linkdict

output_db = open("bookmarks.pickle","wb")
pickle.dump(linkdict,output_db)
output_db.close()
print ("file ./bookmarks.pickle created")




 



