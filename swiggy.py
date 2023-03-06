# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 23:42:30 2022

This script fetches restaurant data for Mumbai from Swiggy's API
and saves it to a CSV file named "mumbai1.csv".

The script uses the requests and json libraries to make HTTP requests
to the Swiggy API and process the response data. The CSV file is created
using the io library.

The script fetches data for all pages of restaurant listings and saves
the data to the CSV file in the following format:

type,id,name,uuid,city,area,avgRating,totalRatingsString,cuisines,tags,costForTwoStrings,deliveryTime,minDeliveryTime,
maxDeliveryTime,address,locality,unserviceable,veg

@author: Aniruddha
"""

import json
import requests
import sys
import io
with io.open('mumbai1.csv','w',encoding='utf-8') as f1:
    f1.write('type,id,name,uuid,city,area,avgRating,totalRatingsString,cuisines,tags,costForTwoStrings,deliveryTime,minDeliveryTime,maxDeliveryTime,address,locality,unserviceable,veg'+'\n')
    f1.close()
import requests

headers = {
    'authority': 'www.swiggy.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'content-type': 'application/json',
    '__fetch_req__': 'true',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.swiggy.com/delhi?page=2',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__SW=JEA9haTvNpqQwpHVXC64cwfNsX7pR67U; _guest_tid=31c8b65b-9c93-4cd5-9e8e-90172624d87f; _device_id=1ea90e1f-f071-0cca-4d04-272d1edcc99e; _sid=xvx57d2a-8748-491b-a265-349982a810b8; fontsLoaded=1; WZRK_G=7cf4a4a02dbd44a3bae9c7eb90b3c490; _gcl_au=1.1.371536962.1641313648; _ga=GA1.2.1618782198.1641313648; _gid=GA1.2.945968703.1641313648; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A8%2C%22s%22%3A1641313647%2C%22t%22%3A1641314486%7D; _gat_UA-53591212-4=1',
}

params = (
    ('page', '0'),
    ('ignoreServiceability', 'true'),
    ('lat', '19.0760'),
    ('lng', '72.8777'),
    ('pageType', 'SEE_ALL'),
    ('sortBy', 'RELEVANCE'),
    ('page_type', 'DESKTOP_SEE_ALL_LISTING'),
)

response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', headers=headers, params=params)
response=response.text
data1=json.loads(response)
page_no=data1['data']['pages']
print(page_no)
dd=0
for i in range(page_no):
    headers = {
        'authority': 'www.swiggy.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'content-type': 'application/json',
        '__fetch_req__': 'true',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.swiggy.com/delhi?page=2',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '__SW=JEA9haTvNpqQwpHVXC64cwfNsX7pR67U; _guest_tid=31c8b65b-9c93-4cd5-9e8e-90172624d87f; _device_id=1ea90e1f-f071-0cca-4d04-272d1edcc99e; _sid=xvx57d2a-8748-491b-a265-349982a810b8; fontsLoaded=1; WZRK_G=7cf4a4a02dbd44a3bae9c7eb90b3c490; _gcl_au=1.1.371536962.1641313648; _ga=GA1.2.1618782198.1641313648; _gid=GA1.2.945968703.1641313648; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A8%2C%22s%22%3A1641313647%2C%22t%22%3A1641314486%7D; _gat_UA-53591212-4=1',
    }
    
    params = (
        ('page', dd),
        ('ignoreServiceability', 'true'),
        ('lat', '19.0760'),
        ('lng', '72.8777'),
        ('pageType', 'SEE_ALL'),
        ('sortBy', 'RELEVANCE'),
        ('page_type', 'DESKTOP_SEE_ALL_LISTING'),
    )
    
    response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', headers=headers, params=params)
    response=response.text
    dd=dd+1
    print('Page No is '+str(dd))
    data1=json.loads(response)
    data1=data1['data']['cards']
    #print(data1)
    for i in range(len(data1)):
        type=data1[i]['data']['data']['type']
        id=data1[i]['data']['data']['id']
        name=data1[i]['data']['data']['name']
        name=str(name)
        name=name.replace(',','')
        uuid=data1[i]['data']['data']['uuid']
        city=data1[i]['data']['data']['city']
        area=data1[i]['data']['data']['area']
        area=str(area)
        area=area.replace(',',' ')
        avgRating=data1[i]['data']['data']['avgRating']
        avgRating=avgRating
        totalRatingsString=data1[i]['data']['data']['totalRatingsString']
        cuisines=data1[i]['data']['data']['cuisines']
        cuisines=str(cuisines)
        cuisines=cuisines.replace(',',' ')
        tags=data1[i]['data']['data']['tags']
        costForTwoString=data1[i]['data']['data']['costForTwoString']
        deliveryTime=data1[i]['data']['data']['deliveryTime']
        minDeliveryTime=data1[i]['data']['data']['minDeliveryTime']
        maxDeliveryTime=data1[i]['data']['data']['maxDeliveryTime']
        address=data1[i]['data']['data']['address']
        address=str(address)
        address=address.replace(',',' ')
        locality=data1[i]['data']['data']['locality']
        locality=str(locality)
        locality=locality.replace(',',' ')
        unserviceable=data1[i]['data']['data']['unserviceable']
        veg=data1[i]['data']['data']['veg']
        scrapped_data=(str(type) +","+ str(id) +","+ str(name) +","+ str(uuid) +","+ str(city) +","+ str(area) +","+str(avgRating)+","+str(totalRatingsString) +","+ str(cuisines)+","+
              str(tags) +","+ str(costForTwoString) +","+ str(deliveryTime) +","+ str(minDeliveryTime) +","+ str(maxDeliveryTime) +","
              + str(address) +","+ str(locality) +","+ str(unserviceable) +","+ str(veg))
        with io.open('mumbai1.csv','a',encoding='utf-8') as f2:
            f2.write(scrapped_data + "\n") 
            f2.close()
        
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5?page=1&ignoreServiceability=true&lat=22.5867&lng=%2088.4171&pageType=SEE_ALL&sortBy=RELEVANCE&page_type=DESKTOP_SEE_ALL_LISTING', headers=headers)