#bilibili ranking list
#time interval : 1h everyday
#output : txt

import datetime
import requests
import os
import json
import sys

os.chdir(sys.path[0])


url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all"

headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}


now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day
hour = now_time.hour


sess = requests.Session()
res = sess.get(url, headers=headers)
data = res.json()["data"]["list"]

#print(data)
hot_list = []
json_list=[]
for item in data:
    item_title = item["title"]
    item_name = item["owner"]["name"]
    item_view=item['stat']['view']
    hot_list.append("title:{}#-#auth:{}#-#view:{}".format(item_title,item_name,item_view))
    json_list.append({"title": item_title, "owner": item_name, "view": item_view})

output = "\n".join(hot_list)
if os.path.exists("./hotlist/{}_{}_{}".format(year, month, day))==False:
    os.mkdir(r"./hotlist/{}_{}_{}".format(year, month, day))
if not os.path.exists("./json"):
    os.makedirs("./json")


with open("./hotlist/{}_{}_{}/{}_{}_{}_{}.txt".format(year, month, day, year, month, day, hour),"w",encoding='utf8') as f:
    f.write(output)

with open("./json/{}_{}_{}_{}.json".format(year, month, day, hour), "w", encoding="utf-8") as f:
    json.dump(json_list, f, ensure_ascii=False)

#log
with open("../log/{}_{}_{}.txt".format(year, month, day), "a",encoding="utf8") as f:
    f.write("{}_{}_{}_{} bilibili ranking list rec. \n".format(year, month, day, hour))
