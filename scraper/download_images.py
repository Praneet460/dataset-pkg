from scrap_links import get_image_links
from requests import get


def download_images(url):
    images = get_image_links(url)
    i = 1
    total = len(images)
    for key, value in images.items():
        response = get(value, stream = True)
        print("Images left to download are {}".format(total-1))
        total = total -1

        if response.status_code == 200:
            filename = 'img_' + str(i)
            i = i + 1
            with open(filename + ".jpeg", 'wb') as f:
                f.write(response.content)
    
            
            
            
        
   

if __name__ == '__main__':
    print(download_images("https://realpython.com/"))