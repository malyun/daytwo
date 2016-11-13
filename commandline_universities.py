#Program that searches for  universities in a country and returns the country, name and domain of the university utilising the hipolabs university API

import requests
import json

def uni_search(query):
    url = 'http://universities.hipolabs.com/search?country='
    country = query.replace(' ', '%20')
    final_url = url + country
    json_obj = requests.get(final_url)
    data = json_obj.json()
    
    for item in data:
        for uni in item:
        	print (uni , " : ", item[uni],)