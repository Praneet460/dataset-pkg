
from scraper.request_setup import simple_get

from bs4 import BeautifulSoup

import json
import os
import errno

###########
# Problem 1
###########
"""
What cities does Uber Support across the globe?
Reference : 'https://www.uber.com/en-IN/cities/'
"""

def uber_cities_global(url: str) -> dict:
    resp = simple_get(url)
    soup = BeautifulSoup(resp, 'html.parser')
    data = {}
    for region in soup.find_all('div', class_ = "_style_VRmHw"):
        region_name = region.h3.text
        cities_name = []
        for city in region.find_all('a'):
            cities_name.append(city.text)
        data[region_name] = cities_name
    return data

"""
convert the dictionay data to the json format
"""
def data_json(url: str, filename: str):
    json_data = json.dumps(uber_cities_global(url))
    with open(filename + ".json", 'w') as f:
        f.write(json_data)
    return json_data

"""
function to fetch out all the cities in the txt file
"""

def data_cities(url):
    city_names = uber_cities_global(url)
    cities_data = []
    all_cities_list = []
    for cities_list in city_names.values():
        all_cities_list.append(cities_list)
    
        for cities in all_cities_list:
            for city in cities:
                cities_data.append(city)
    """
    Store data inside a text file
    """
    with open("uber_only_cities.txt", 'w') as f:
        for name in cities_data:
            f.write(name + "\n")
    return cities_data
        

   



###########
# Problem 2
###########

"""
What countries does Uber Support across the globe?
Reference : 'https://www.uber.com/en-IN/country-list/'
"""
def uber_countries(url):
    resp = simple_get(url)
    soup = BeautifulSoup(resp, 'html.parser')
    countries_data = []
    for sites in soup.find_all('div', class_ = "desk-wrapper"):
        for country in soup.find_all('div', class_ = "layout__item"):
            countries_data.append(country.text)
    """
    Clean the output list with only countries name
    """
    all_countries = []
    for name in countries_data:
        country_name = name.split('|')
        all_countries.append(country_name[0]) 

    """
    Write data to a file
    """
    with open('uber_countries.txt', 'w') as f:
        for name in all_countries:
            f.write(name + "\n")
        
    return len(all_countries)







    
if __name__ == '__main__':
    print(data_json("https://www.uber.com/en-IN/cities/", filename="uber_cities"))
    # print(uber_countries("https://www.uber.com/en-IN/country-list/"))
    # print(data_cities("https://www.uber.com/en-IN/cities/"))
