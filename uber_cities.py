"""
What cities does Uber Support across the globe?
Reference : 'https://www.uber.com/en-IN/cities/'
"""

from scraper.request_setup import simple_get

from bs4 import BeautifulSoup

import json

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
        

def data_json(url: str, filename: str):
    """
    convert the dictionay data to the json format
    """
    json_data = json.dumps(uber_cities_global(url))
    with open(filename + ".json", 'w') as f:
        f.write(json_data)
    return json_data




    
if __name__ == '__main__':
    print(data_json("https://www.uber.com/en-IN/cities/", filename="uber_cities"))
