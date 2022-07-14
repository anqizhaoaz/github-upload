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
#http://api.map.baidu.com/traffic/v1/around?ak=L2REKE9wvZpLZ3xqrhbUASaFTpPl6bez&center=22.553644,113.959078&radius=1500&coord_type_input=gcj02&coord_type_output=gcj02

#南山外国语 113.959078,22.553644
#广州北站：113.210362,23.383175


# input your lat and long
x_cor = ["23.383175"] #latitue of the center
y_cor = ["113.210362"] #longitude of the center

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

