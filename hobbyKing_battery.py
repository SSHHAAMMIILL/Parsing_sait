import fake_useragent
import requests
from bs4 import BeautifulSoup as BS
import unicodedata
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

def get_source_html(url):
    array = fake_useragent.UserAgent()

    headers = {
        "User-Agent": array.random
    }

    req = requests.get(url, headers=headers)
    src = req.text
    # print(src)

    with open("battery_LiFe.html", "w") as file:
        file.write(src)

def get_source_html_array(url,name,n):
    array = fake_useragent.UserAgent()

    headers = {
        "User-Agent": array.random
    }

    req = requests.get(url, headers=headers)
    src = req.text
    # print(src)

    with open(f"link_battery/{n}_{name}.html", "w") as file:
        file.write(src)


def motors(name, d):
    print(name)
    with open(f"link_battery/{d}_{name}.html") as file:
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

    un = unicodedata.normalize
    count = soup.find("div", {"id": "tab-description"}).find_all("p")

    dictionary = ["Технические характеристики", "Specs", " Технические характеристики", " Specs", " Характеристики.",
                  "Спекуляция"]

    for m in count:
        m = [un("NFKD", ele.text.replace(":", "").strip()) for ele in m]
        answer = any(item in m for item in dictionary)  # ответом является True или False
        list_of_characteristics = m
        if answer:
            f = 0
            f = selection(dictionary, list_of_characteristics, f)

            a = m[f:len(m)]
            try:
                while True:
                    a.remove("")
            except ValueError:
                pass

            print(a)

    p = 0

    try:
        for m in a[0:len(a)]:
            p = p + 1
            if p % 2 == 0:
                value_array.append(m)
            else:
                title_array.append(m)
        print(title_array)
        print(value_array)

    except:
        print(title_array)
        print(value_array)


def main():
    # get_source_html("https://hobbyking.com/ru_ru/batteries-chargers/batteries/life.html")
    with open("battery_LiFe.html") as file:
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
        motors(projects_title[i],i)

if __name__ == "__main__":
    main()
