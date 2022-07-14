# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
import urllib
import time
import sched, time
import csv
import string
from urllib.parse import quote


###### 根据路名查询 ######
#road = ['青梧路','科技路','铜鼓路','大冲二路','沙河西路','科发路','文华路','金铜路','大冲六路']
road = ['云山大道','建设路','秀全大道','站前路']
#road = ['站前路']
key = "5UK6Um2nRBqID8cTTgYblTbGQREW8DtC"

result_name2 = []
result_time3 = []
result_overall2 = []
result_status2 = []
result_status_desc2 = []
result_road_traffic = []



for i in road:
    result_name2.append(i)
    full_page = "http://api.map.baidu.com/traffic/v1/road?road_name="+i+"&city=广州市&ak="+key
    full_page = quote(full_page, safe=string.printable)
    json_data = json.load(urlopen(full_page)) #Receive JSON response from url
    print(json_data)
    overall = json_data['description']
    status = json_data['evaluation']['status']
    status_desc = json_data['evaluation']['status_desc']
    road_traffic = json_data['road_traffic']
    from datetime import datetime
    catch_time = time.asctime( time.localtime(time.time()) )
    result_time3.append(catch_time)
    result_overall2.append(overall)
    result_status2.append(status)
    result_status_desc2.append(status_desc)
    result_road_traffic.append(road_traffic)



import pandas as pd
dataframe = pd.DataFrame({'road': result_name2, 'time': result_time3, 'overall': result_overall2, 'status': result_status2, 'description': result_status_desc2, 'road_traffic': result_road_traffic})
dataframe.to_csv("school_result.csv",index=False, header=False, mode='a', sep=',', encoding='utf_8_sig')


