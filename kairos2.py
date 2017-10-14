import urllib2
import json
response = urllib2.urlopen("https://api.openaq.org/v1/latest")
html = response.read()
drawss=json.loads(html)["results"]
for d in drawss:
    print "polh:",d["city"],"topo8esia:",d["location"]
x=raw_input("dwse onoma prwths polhs: ")
y=raw_input("dwse topo8esia prwths polhs: ")
k=raw_input("dwse onoma deuterhs polhs: ")
l=raw_input("dwse topo8esia deuterhs polhs: ")
for d in drawss:
    if(d["city"]==x):
        if(d["location"]==y):
            z=d["measurements"]
            print "prwth polh: "
            for i in z:
                print i["parameter"], i["value"]
    if(d["city"]==k):
        if(d["location"]==l):
            z=d["measurements"]
            print "deuterh polh: "
            for i in z:
                print i["parameter"], i["value"]
