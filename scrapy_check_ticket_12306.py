#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import requests
import time
import datetime


url_city='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002'
city=requests.get(url_city,verify=False)
cities=city.content
citieslist=cities.split('|')
city_code=[]
for i in xrange(len(citieslist)/5):
    city_code.append(citieslist[5*i:5*(i+1)])
city_code[0][0]='@bjb'
city_dict={}
for i in city_code:
    city_dict[i[0]] = i[2]
    city_dict[i[1]] = i[2]
    city_dict[i[2]] = i[2]
    city_dict[i[3]] = i[2]
    city_dict[i[4]] = i[2]
fcity=raw_input('From city:')
while city_dict.has_key(fcity)==False:
    fcity = raw_input('please reenter the from city:')
tcity=raw_input('To city:')
while city_dict.has_key(tcity)==False:
    tcity = raw_input('please reenter the to city:')
fcity_code=city_dict[fcity]
tcity_code=city_dict[tcity]
endDay = (datetime.datetime.now() + datetime.timedelta(days = 30))
timeStamp = int(time.mktime(endDay.timetuple()))
timeStyle = endDay.strftime("%Y-%m-%d")
date=raw_input('Date(yyyy-mm-dd) must before '+str(timeStyle)+':')
query_url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+str(date)+'&leftTicketDTO.from_station='+str(fcity_code)+'&leftTicketDTO.to_station='+str(tcity_code)+'&purpose_codes=ADULT'
information=requests.get(query_url,verify=False)
ticket=information.json()
results=[]
G=0
D=0
Z=0
T=0
K=0
if ticket['data']!=[]:
    for i in ticket['data']:
        result=[]
        result.append(i['queryLeftNewDTO']["station_train_code"])
        result.append(i['queryLeftNewDTO']['from_station_name'])
        result.append(i['queryLeftNewDTO']['to_station_name'])
        result.append(i['queryLeftNewDTO']['start_time'])
        result.append(i['queryLeftNewDTO']['arrive_time'])
        result.append(i['queryLeftNewDTO']['lishi'])
        result.append(i['queryLeftNewDTO']['zy_num'])
        result.append(i['queryLeftNewDTO']['ze_num'])
        result.append(i['queryLeftNewDTO']['rw_num'])
        result.append(i['queryLeftNewDTO']['yw_num'])
        result.append(i['queryLeftNewDTO']['zy_num'])
        result.append(i['queryLeftNewDTO']['wz_num'])
        results.append(result)
        type=list(result[0])[0]
        if type=='G':
            G=G+1
        elif type=='D':
            D=D+1
        elif type=='K':
            K=K+1
        elif type=='T':
            T=T+1
        elif type=='Z':
            Z=Z+1
    print '共有车次'+str(len(results))+'班,其中高铁'+str(G)+'班，动车'+str(D)+'班，直达'+str(Z)+'班，特快'+str(T)+'班，快速'+str(K)+'班。'
    for i in xrange(len(results)):
        print '车次:'+str(results[i][0])+' 乘车车站:'+str(results[i][1])+' 乘车到站:'+str(results[i][2])+' 开车时间:'+str(results[i][3])+' 到站时间:'+str(results[i][4])+' 历时:'+str(results[i][5])+' 一等座:'+str(results[i][6])+' 二等座:'+str(results[i][7])+' 软卧:'+str(results[i][8])+' 硬卧:'+str(results[i][9])+' 硬座:'+str(results[i][10])+' 无座:'+str(results[i][11])
else:
    print '无直达车'



