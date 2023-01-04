#bilibili热搜 (首页搜索栏)
#time interval : 1h everyday
#output : txt

import datetime
import requests
import os

url = "https://api.bilibili.com/x/web-interface/search/square?limit=30"

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
data = res.json()["data"]["trending"]["list"]

#print(data)
hot_list = []
for item in data:
    item_key = item["keyword"]
    item_show = item["show_name"] 
    hot_list.append("{}: {}".format(item_key, item_show))

output = "\n".join(hot_list)
if os.path.exists("./hotpoint/{}_{}_{}".format(year, month, day))==False:
    os.mkdir(r"./hotpoint/{}_{}_{}".format(year, month, day))

with open("./hotpoint/{}_{}_{}/{}_{}_{}_{}.txt".format(year, month, day, year, month, day, hour), mode="w") as f:
    f.write(output)
#log
with open("../log/{}_{}_{}.txt".format(year, month, day), "a",encoding="utf8") as f:
    f.write("{}_{}_{}_{} bilibili hot hot research list rec. \n".format(year, month, day, hour))