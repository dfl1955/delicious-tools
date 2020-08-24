
# V1.1 DFL makes filtered RSS files

import pickle
import datetime
import htmle

dictfile = open('bookmarks.pickle','rb')

D = {};                     # the input dictionary
D = pickle.load(dictfile) ; # loads a dictionary
dictfile.close()

K=[]; K = D.keys();

tags = open('tags.pickle','rb')

tagindex = {};
tagindex = pickle.load(tags) ; # loads a dictionary
tags.close()

T=[]; T = tagindex.keys();         # the tagindex dictionary keys

today = datetime.datetime.now()
builddate = today.strftime('%a, %d %b %Y %H:%M:%S %z')
#print (builddate)

rsshead='<?xml version="1.0" encoding="UTF-8" ?>\n<rss version="2.0">\n<channel>\n<title>old delicious faves, "%s"</title>\n<description>delicious bookmarks filtered on tag "%s"</description>\n<link>xxxx to be inserted</link>\n<lastBuildDate>%s</lastBuildDate>\n<pubDate>%s</pubDate>\n'
rssitem='<item>\n\t<title>%s</title>\n\t<link>%s</link>\n\t<description>%s</description>\n</item>\n'
rsstail='</channel>\n</rss>'

for s in ['uru','html','London','bruxelles']:
    ofilename=s + '-bookmarks.rss'
    ofilestr=''
    ofilestr = ofilestr + ((rsshead %(s,s,builddate, builddate)))
    for i in tagindex[s]:
        atext = htmle.tr(D[i]['ANCHOR TEXT'])
        dtext = htmle.tr(D[i]['DESCRIPTION'])
        ofilestr = ofilestr + ((rssitem %(atext,D[i]['HREF'],dtext)))
    ofilestr = ofilestr + rsstail
    rssfile = open(ofilename,'w')
    rssfile.write(ofilestr)
    rssfile.close()



