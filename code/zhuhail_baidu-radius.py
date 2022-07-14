# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
import urllib
import time
import sched, time
import csv
import string
from urllib.parse import quote


####### 根据设置半径查询 ########

# 网页查询例子
#http://api.map.baidu.com/traffic/v1/around?ak=L2REKE9wvZpLZ3xqrhbUASaFTpPl6bez&center=22.231961,113.552123&radius=1500&coord_type_input=gcj02&coord_type_output=gcj02

#烟台山公园 113.552123,22.231961

# input your lat and long
x_cor = ["22.553644"] #latitue of the center
y_cor = ["113.959078"] #longitude of the center

r = "1500" #radius

#input your own key
ak="5UK6Um2nRBqID8cTTgYblTbGQREW8DtC"
# 5UK6Um2nRBqID8cTTgYblTbGQREW8DtC
# L2REKE9wvZpLZ3xqrhbUASaFTpPl6bez

#full_page = "http://api.map.baidu.com/traffic/v1/around?ak="+ak+"&center="+coord1+"&radius="+r+"&coord_type_input=gcj02&coord_type_output=gcj02"
#data = json.load(urlopen(full_page)) #Receive JSON response from url

# 准备结果存入的variable list
result_overall = []
result_scale= []
result_time = []
result_time2 = []
result_name = []
result_congestion = []
result_xi = []
result_yi = []
result_congestion_distance = []
result_speed = []
result_status = []
result_trend= []
result_section = []


for xi, yi in zip(x_cor, y_cor):
    full_page = "http://api.map.baidu.com/traffic/v1/around?ak=" + ak + "&center=" + xi + "," + yi + "&radius="+r+ "&coord_type_input=gcj02&coord_type_output=gcj02"
    data = json.load(urlopen(full_page)) #Receive JSON response from url
    print(data)
    overall = data['description']
    result_overall.append(overall)
    #overall
    scale = data['evaluation']
    result_scale.append(scale)
    #scale
    from datetime import datetime
    catch_time = time.asctime( time.localtime(time.time()) )
    result_time.append(catch_time)
    #current time
    for i in data['road_traffic']:
        #print(len(i))
        if (len(i)) > 1:
            for j in i['congestion_sections']:
                road=i['road_name']
                print(road)
                print(j)
                result_name.append(road)
                result_congestion_distance.append(j['congestion_distance'])
                result_speed.append(j['speed'])
                result_status.append(j['status'])
                result_trend.append(j['congestion_trend'])
                result_section.append(j['section_desc'])
                catch_time2 = time.asctime( time.localtime(time.time()) )
                result_time2.append(catch_time2)


import pandas as pd
dataframe = pd.DataFrame({'x':x_cor,'y': y_cor, 'time': result_time,'evaluation':result_overall, 'scale':result_scale})
dataframe.to_csv("school_1.csv",index=False, header=False,mode='a', sep=',', encoding='utf_8_sig')

import pandas as pd
dataframe = pd.DataFrame({'时间': result_time2,'路名':result_name, '拥堵距离':result_congestion_distance,  '平均通行速度':result_speed, '路段拥堵评价':result_status, '较10分钟前拥堵趋势':result_trend, '拥堵路段':result_section})
dataframe.to_csv("school_2.csv",index=False, header=False, mode='a', sep=',', encoding='utf_8_sig')



###### 根据路名查询 ######
## 一次查询 http://api.map.baidu.com/traffic/v1/road?road_name=九洲大道中&city=珠海市&ak=5UK6Um2nRBqID8cTTgYblTbGQREW8DtC
road = ['桂花南路','粤海中路','粤华路','桂花北路','九洲大道中','科发路','文华路','金铜路','大冲六路']
key = "5UK6Um2nRBqID8cTTgYblTbGQREW8DtC"

result_name2 = []
result_time3 = []
result_overall2 = []
result_status2 = []
result_status_desc2 = []
result_road_traffic = []



for i in road:
    result_name2.append(i)
    full_page = "http://api.map.baidu.com/traffic/v1/road?road_name="+i+"&city=珠海市&ak="+key
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
