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

def main():
    name = "0_Turnigy Trackstar 1 | 8th Sensored безщеточный 2400KV"
    with open(f"link/{name}.html") as file:
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
    # n = count[2].text деление текста
    # print(n)
    # print(n.split("  "))

    dictionary = ["Технические характеристики:","Specs:"," Технические характеристики:"," Specs:"," Характеристики.", " Спекуляция", "В стоимость входит"]

    for m in count:
        answer = any(item in m.text.split("  ") for item in dictionary) # ответом является True или False dictionary
        list_of_characteristics = m.text.split("  ")
        # print((m.text))
        # print(list_of_characteristics)
        if answer:
            f = 0
            f = selection(dictionary, list_of_characteristics,f)

            #     for i in list_of_characteristics:
            #         if j != i:
            #             q = q + 1
            #         print(q)
            #         if q == len(list_of_characteristics):
            #             q = 0
            #         if j == i:
            #             f = q
            #             break



            n = m.text.split("  ",f)
            a = n[f:len(n)]
            n = re.split("  |:", a[0])
            last = selection(dictionary, n, f)-1
            n = n[0:last]


    p=0

    try:
        for m in n[0:len(n)]:
            p = p + 1
            if p % 2 == 0:
                value_array.append(m)
            else:
                title_array.append(m)

    except:
        p = 0

    print(title_array)
    print(value_array)


if __name__ == "__main__":
    main()