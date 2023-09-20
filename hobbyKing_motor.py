import fake_useragent
import requests
from bs4 import BeautifulSoup as BS
import re

def selection(dictionary, list_of_characteristics,f):
    for j in dictionary:
        q = 0
        while list_of_characteristics[q] != j:
            q = q + 1
            f = len(list_of_characteristics)+1
            if q == len(list_of_characteristics):
                q = q - 1
                break
        if list_of_characteristics[q] == j:
            f = q + 1
            print(f)
            break
    return f

def get_source_html_array(url,name,n):
    array = fake_useragent.UserAgent()

    headers = {
        "User-Agent": array.random
    }

    req = requests.get(url, headers=headers)
    src = req.text
    # print(src)

    with open(f"link/{n}_{name}.html", "w") as file:
        file.write(src)


def motors(name, d):
    print(name)
    with open(f"link/{d}_{name}.html") as file:
        src = file.read()

    soup = BS(src, "lxml")
    count = soup.find("ul", {"class" : "list-attribute-product"}).find_all("div")

    title_array = []
    value_array = []

    for m in count:
        title = m.find("span", {"class" : "label"}).text
        value = m.find("span", {"class" : "data"}).text
        title_array.append(title)
        value_array.append(value)
    # print(title_array)
    # print(value_array)

    count = soup.find("div", {"id": "tab-description"}).find_all("p")

    dictionary = ["Технические характеристики:", "Specs:", " Технические характеристики:", " Specs:"," Характеристики."," Спекуляция"]

    dictionary = ["Технические характеристики:", "Specs:", " Технические характеристики:", " Specs:",
                  " Характеристики.", " Спекуляция", "В стоимость входит"]

    for m in count:
        answer = any(item in m.text.split("  ") for item in dictionary)  # ответом является True или False dictionary
        list_of_characteristics = m.text.split("  ")
        # print((m.text))
        # print(list_of_characteristics)
        if answer:
            f = 0
            f = selection(dictionary, list_of_characteristics, f)

            n = m.text.split("  ", f)
            a = n[f:len(n)]
            n = re.split("  |:", a[0])
            last = selection(dictionary, n, f) - 1
            n = n[0:last]

    p = 0

    try:
        for m in n[0:len(n)]:
            p = p + 1
            if p % 2 == 0:
                value_array.append(m)
            else:
                title_array.append(m)
        print(title_array)
        print(value_array)
        print('\n')
    except:
        print(title_array)
        print(value_array)
        print('\n')


def main():
    # get_source_html("https://hobbyking.com/ru_ru/power-systems/electric-motors/brushless-motors.html#q=&idx=hbk_live_magento_ru_ru_products&dFR%5Bwarehouses%5D%5B0%5D=Global&dFR%5Bwarehouses%5D%5B1%5D=EU&dFR%5Bwarehouses_stock_data%5D%5B0%5D=Global%7C1&dFR%5Bwarehouses_stock_data%5D%5B1%5D=Global%7C2&dFR%5Bwarehouses_stock_data%5D%5B2%5D=Global%7C3&dFR%5Bwarehouses_stock_data%5D%5B3%5D=EU%7C1&dFR%5Bwarehouses_stock_data%5D%5B4%5D=EU%7C2&dFR%5Bwarehouses_stock_data%5D%5B5%5D=EU%7C3&hFR%5Bcategories.level0%5D%5B0%5D=%D0%AD%D0%BD%D0%B5%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B%20%2F%2F%2F%20%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B3%D0%B0%D1%82%D0%B5%D0%BB%D0%B8%20%2F%2F%2F%20%D0%91%D0%B5%D1%81%D1%89%D0%B5%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B5%20%D0%B4%D0%B2%D0%B8%D0%B3%D0%B0%D1%82%D0%B5%D0%BB%D0%B8&is_v=1")
    with open("образец.html") as file:
        src = file.read()

    soup = BS(src, "lxml")
    count = soup.find_all("a", {"itemprop":"url"})#.find_all("div", {"class":"ais-infinite-hits--item"})

    projects_link = []
    projects_title = []
    for item in count:
        all_basic_link = item.get("href")
        title_basic_link = item.find("span").text.replace('/', '|')  # название ссылок
        projects_link.append(all_basic_link)
        projects_title.append(title_basic_link)
        # projects_title.append(title_basic_link)
    print(projects_title) #массив с именами продуктов
    print(projects_link) #массив с ссылками


    n = len(projects_link)  # длина массива
    print(n)
    for i in range(0,n):
        get_source_html_array(projects_link[i],projects_title[i],i)
        # motors(projects_title[i],i)

if __name__ == "__main__":
    main()


