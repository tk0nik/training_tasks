import urllib
from urllib import request
import requests

#====data====#

link_without_number = "https://acomics.ru/~the-noosphere-comics/"
catalog_path = "noosphere"

#====functions====#

def get_count_of_pages():
    link_about = link_without_number + "about"
    #print(link_about)
    #костыли подъехали
    p_list = str(urllib.request.urlopen(link_about).read()).split("about-summary")[1].split("<p>")  #ага, сплит по тегу <p>
    result = p_list[4].split("</p>")[0].split("</b>")[1].strip()
    
    return int(result)


def get_image_link(number):
    link = link_without_number + number
    page = urllib.request.urlopen(link).read()
    page_txt = str(page)
    part = page_txt.split("mainImage")[1].split('"')
    image_link = part[2]
    full_image_link = "https://acomics.ru"+image_link
    
    return full_image_link

#====main====#

for i in range(1, get_count_of_pages() + 1):
 
    #print(get_image_link(str(i)))
    p = requests.get(get_image_link(str(i)))

    file_path = catalog_path+"\page_"+str(i)+".jpg"
    out = open(file_path, "wb")
    out.write(p.content)
    out.close()
    print("page", i, "is in<"+ catalog_path+"> path")
    
print("all pages downloaded!") 


   







