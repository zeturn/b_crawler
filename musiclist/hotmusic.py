#bilibili music list (哔哩哔哩音乐榜)
#time interval : everyweek- Saturday 8:00
#output : txt

import datetime
import time
import requests
import os
import json
import sys

os.chdir(sys.path[0])
headers = {
  #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}


now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day
hour = now_time.hour



t = time.time()


url1 = "https://api.bilibili.com/x/copyright-music-publicity/toplist/all_period?list_type=1"

idsess= requests.Session()
idres = idsess.get(url1, headers=headers)
iddata = idres.json()["data"]["list"]

#print (iddata)
listidlist=[]
for yearid in iddata:
    listidlist.append(yearid)
    
curid=iddata[yearid][0]
curid=curid["ID"]
#print(curid)

url2 = "https://api.bilibili.com/x/copyright-music-publicity/toplist/music_list?list_id={}".format(curid)

sess = requests.Session()
res = sess.get(url2, headers=headers)
data = res.json()["data"]["list"]

json_output = []#json

#print(data)
hot_list = []
for item in data:
    item_music_title = item["music_title"]
    item_creation_title = item["creation_title"] 
    hot_list.append("music_title:{}#-#video_title:{}".format(item_music_title, item_creation_title))
    json_output.append({"music_title": item_music_title, "creation_title": item_creation_title})

output = "\n".join(hot_list)

with open("./hotmusic/{}_{}_{}_{}.txt".format(year, month, day, hour), "w",encoding="utf8") as f:
    f.write(output)

with open("./json/{}_{}_{}_{}.json".format(year, month, day, hour), "w", encoding="utf-8") as f:
    json.dump(json_output, f, ensure_ascii=False)

#log

with open("../log/{}_{}_{}.txt".format(year, month, day), "a",encoding="utf8") as f:
    f.write("{}_{}_{}_{} bilibili hot music list rec. \n".format(year, month, day, hour))
