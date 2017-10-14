import urllib2
import json
onoma=raw_input("dwse onoma prwths polhs: ")
onoma2=raw_input("dwse onoma deuterhs polhs: ")
response = urllib2.urlopen("https://api.teleport.org/api/urban_areas/slug:%s/scores/"%onoma)
response2 = urllib2.urlopen("https://api.teleport.org/api/urban_areas/slug:%s/scores/"%onoma2)
html = response.read()
html2 = response2.read()
drawss=json.loads(html)["categories"]
drawss2=json.loads(html2)["categories"]
x=[]
y=[]
for i in drawss:
    x.append(i["score_out_of_10"])
for i in drawss2:
    y.append(i["score_out_of_10"])
sum=0
sum2=0
for i in range(17):
    if(x[i]>y[i]):
        sum=sum+1
    if(x[i]<y[i]):
        sum2=sum2+1
if(sum>sum2):
    print "uperexei h prwth ths deuterhs kata ", sum-sum2
if(sum<sum2):
    print "uperexei h deuterh ths prwths kata ", sum2-sum
else:
    print "einai idies se olous tous tomeis "
