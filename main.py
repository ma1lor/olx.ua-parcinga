import json

import requests
from bs4 import BeautifulSoup

price = '10000'


list = []

def get():
    i = 1
    while(i<28):
        page = f'&page={i}'
        url = f'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/?search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye&search%5Bfilter_enum_number_of_rooms_string%5D%5B1%5D=dvuhkomnatnye&search%5Bdistrict_id%5D=17&{page}'



        headers = {
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64"
        }
        r = requests.get(url=url, headers=headers)
        with open("page.html", "w") as file:
            file.write(r.text)
        with open("page.html") as file:
            info = file.read()
        soup = BeautifulSoup(info, "lxml")



        for room in soup.find_all(class_='offer-wrapper'):
            title = room.find("h3" ,class_='lheight22 margintop5').find('strong').text
            link = room.find("h3" ,class_='lheight22 margintop5').find('a').get('href')
            price = room.find('div', class_='space inlblk rel').find('strong').text

            list.append({
                'title' : title,
                'link' : link,
                'price' : price
            })
        i+=1


    with open('list.json', 'w') as file:
        json.dump(list, file, ensure_ascii=False, indent=4)
def main():
    get()

if __name__ == '__main__':
    main()
