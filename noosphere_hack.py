import urllib
from urllib import request
import requests

#====data====#

link_without_number = "https://acomics.ru/~the-noosphere-comics/"
image_links = []

#====functions====#

def get_image_link(number):
    link = link_without_number + number
    page = urllib.request.urlopen(link).read()
    page_txt = str(page)
    part = page_txt.split("mainImage")[1].split('"')
    image_link = part[2]
    full_image_link = "https://acomics.ru"+image_link
    return full_image_link

for i in range(228, 229):
    print("page number:", i)
    print(get_image_link(str(i)))
    p = requests.get(get_image_link(str(i)))

    file_path = "noosphere\page_"+str(i)+".jpg"
    out = open(file_path, "wb")
    out.write(p.content)
    out.close()
    print("page is ready!")


   







