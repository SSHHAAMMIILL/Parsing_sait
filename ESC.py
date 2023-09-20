import fake_useragent
import requests
from lxml import html
import unicodedata
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

def main():
    name = "0_AeroStar WiFi Connect ESC Programming Device"
    with open(f"link_ESC/{name}.html") as file:
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


    dictionary = ["Технические характеристики","Specs"," Технические характеристики"," Specs"," Характеристики.", "Спекуляция"]

    for m in count:
        m = [un("NFKD", ele.text.replace(":", "").strip()) for ele in m]
        print(m)
        answer = any(item in m for item in dictionary) # ответом является True или False
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

    p=0

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


if __name__ == "__main__":
    main()