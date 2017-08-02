#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2
#import redis

#通过7timer API 拿到北京未来三天天气，返回格式为 Json
weatherURL = urllib2.urlopen('http://202.127.24.18/v4/bin/civillight.php?lon=114.420&lat=30.515&ac=0&unit=metric&output=json&tzshift=0')
weatherData = weatherURL.read()

#print weatherData

#解析 Json数据
WeatherJson = eval(weatherData)

print WeatherJson

#temp today & tomorrow
temp1 = WeatherJson['dataseries'][0]['temp2m']['max']
temp2 = WeatherJson['dataseries'][0]['temp2m']['min']
temp3 = WeatherJson['dataseries'][1]['temp2m']['max']
temp4 = WeatherJson['dataseries'][1]['temp2m']['min']

#wind today & tomorrow
wind1 = WeatherJson['dataseries'][0]['wind10m_max']
wind2 = WeatherJson['dataseries'][1]['wind10m_max']

#tomorrow weather
weather = WeatherJson['dataseries'][0]['weather']

# temp & wind change
temp = temp1-temp3
wind = wind1 -wind2

string = "";
if temp >= 3:
    string = string + u"明天降温%s度，"%temp
if wind1 > 5 and wind <= -3:
    string = string + u"明天风力%s级，"%wind2
if "rain" in weather:
    string = string + u"明天有雨，"
if "snow" in weather:
    string = string + u"明天有雪，"
if "storm" in weather:
    string = string + u"明天有暴风雨，"

print u"今天天气: " + weather
print u"最高温度: %s度" %temp1
if string.strip() != '':
    print string
