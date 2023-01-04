#bilibili precious
#time interval : every month
#output : txt

import datetime
import requests
import os

url = "https://api.bilibili.com/x/web-interface/popular/precious?page_size=100&page="

headers = {
  #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}


now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day
hour = now_time.hour


sess = requests.Session()
res = sess.get(url, headers=headers)
data = res.json()["data"]["list"]

hot_list = []
for item in data:
    item_title = item["title"]
    item_name = item["owner"]['name']
    item_view = item["stat"]['view']
    hot_list.append("title:{}#-#up:{}#-#view:{}".format(item_title, item_name,item_view))

output = "\n".join(hot_list)
if os.path.exists("./hotpoint/{}_{}_{}".format(year, month, day))==False:
    os.mkdir(r"./hotpoint/{}_{}_{}".format(year, month, day))

with open("./hotpoint/{}_{}_{}/{}_{}_{}_{}.txt".format(year, month, day, year, month, day, hour), "w",encoding="utf8") as f:
    f.write(output)

#log
with open("../log/{}_{}_{}.txt".format(year, month, day), "a",encoding="utf8") as f:
    f.write("{}_{}_{}_{} bilibili hot precious list rec. \n".format(year, month, day, hour))
