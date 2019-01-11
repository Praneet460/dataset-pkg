from request_setup import simple_get

from bs4 import BeautifulSoup

def get_links(url: str) -> dict:
    content = simple_get(url)
    soup = BeautifulSoup(content, 'html.parser')
    links = {}
    for link in soup.find_all('a'):
        links[link.text] = link['href']

    return links

def get_image_links(url: str) -> dict:
    image_content = simple_get(url)
    soup_image = BeautifulSoup(image_content, 'html.parser')
    image_links = {}
    for image in soup_image.find_all('img'):
        value = image.get('src')

        key = image.get('alt')
        
        if value[:1] == '/':
            image_links[key] = url+value[1:]

        else:
            image_links[key] = value
        
       
    return image_links



if __name__ == '__main__':
    print(get_links('https://www.google.com'))
    print(get_image_links("https://realpython.com/"))