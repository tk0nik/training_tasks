import requests

# ==== data ==== #
url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '', # только текущая погода
    'T': '', # отключить терминальные последовательности (без цветов)
    'M': '', # показывать скорость ветра в м/с
}

request_headers = {
    'Accept-Language': 'ru'
}

# ==== main ==== #
response = requests.get(url, params = weather_parameters, headers=request_headers)  
print(response.text)
