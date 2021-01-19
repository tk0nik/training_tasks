import vk_api
import requests
from random import *
from vk_api.longpoll import VkLongPoll, VkEventType

database = {
    "гейтс": "Аккуратный программист — быстрый программист",
    "джоббс":"Сегодня ты делаешь код, завтра код делает тебе деньги",
    "московиц":"Не экономьте на дизайне: конечный пользователь ровным счётом ничего не понимает в программировании"
    }


our_token = '037419f916d0e28f96f4ca78bdade87fa171d16392ed964797f254a3e87257da2b532e2fb403e1b835bd4'
vk_session = vk_api.VkApi(token=our_token)
rid = 12345
def write_msg(i, user_id, message):
    print("Запущена функция write_msg")
    print("Пишу", user_id, ":",message)
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, "random_id": i})

longpoll = VkLongPoll(vk_session)
flag = True

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        print("Получено новое сообщение от", event.user_id)
        print(type(event.user_id))
        if event.user_id == 444600269 and flag:
            i = randint(0,100)
            write_msg(i, event.user_id, "А я тебя знаю, ты - Полина! А ещё ты лапушка!")
            flag = False
     
        
        # Обработка сообщения
        request = event.text
        print("Текст сообщения:", request)
        request = request.lower()
        print("После обработки:", request)
            
        # Каменная логика ответа
        if request == "привет" or request == "Привет":
            print("подходит под случай <привет>")
            i = randint(0,100)
            write_msg(i, event.user_id, "Привет!")
        elif request == "пока":
            print("подходит под случай <привет>")
            i = randint(0,100)
            write_msg(i, event.user_id, "Пока!")
        elif request in database:
            i = randint(0,100)
            write_msg(i, event.user_id, database[request])
        else:
            write_msg(randint(100,200), event.user_id, "Сообщения <"+ str(request) + "> нет у меня в базе ответов(( так что игого, наверное. Попробуй написать <привет>")




            



            

