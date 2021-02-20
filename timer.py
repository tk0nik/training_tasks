import discord
from discord.ext import commands
import time
import datetime

#link for add to server: https://discord.com/api/oauth2/authorize?client_id=811552622951137290&permissions=1140980816&scope=bot
token = 'ODExNTUyNjIyOTUxMTM3Mjkw.YCz3Rw.qICg8ZRt8I6Dzlt1R33Q2Tp8b6Y'

#===============DATA================#
groups = {
    "1": {"Среда":"09:00",
          "Суббота":"09:00"},
    "2": {"Среда":"10:50",
          "Суббота":"10:50"},
    "3": {"Среда":  "16:20",
          "Суббота":"16:20"},
    "4": {"Понедельник":  "16:20",
          "Пятница":"16:20"},
    "5": {"Понедельник":  "09:00",
          "Пятница":"09:00",
          "Суббота":"14:30"},
    }

schedule = {
        "Понедельник": ["5", "4"],
        "Вторник": [],
        "Среда": ["1", "2", "3"],
        "Четверг": [],
        "Пятница": ["5", "4"],
        "Суббота": ["1","2","5", "3"],
        "Воскресенье": []
    }

weekdays = list(schedule.keys())

def time_now():
    time = datetime.datetime.now().strftime("%H:%M")
    return time
        
def weekday_now():
    today = datetime.datetime.today()
    return weekdays[today.weekday()]

def schedule_today():
    for day in weekdays:
        if day == weekday_now():
            print("сегодня", weekday_now())
            return schedule[day]
        
#=================== main ========================#
groups_today = schedule_today()
weekday = weekday_now()

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("------")
    guild = bot.guilds[0]
    category = guild.categories[0] # выбирает первую категорию из сервера, к которому подключился
    while True:
        hours = int(time_now()[0:2])
        minutes = int(time_now()[3:5])
        
        j = 0 #int(input('::'))
        channel = category.channels[j] # получает первый канал в первой категории
        #text = input(': ')
        for i in groups_today:
            group = groups[i]
            class_hours = int(group[weekday][0:2])
            class_minutes = int(group[weekday][3:5])
            print(class_hours, class_minutes)

            #!!!!!!!! БАГ: НЕ РАБОТАЕТ С МИНУТАМИ! Н-р, 16:20! 
            while hours <= class_hours:
                text = "для занятия группы"+str(i)+ "ещё рано"
                time.sleep(10)
                await channel.send(text) # отправка самого сообщения

            if hours == class_hours and minutes ==0:
                text = str(time_now())
                print("О! Начало занятия группы", i)
                await channel.send(text)
                time.sleep(60*30)   #30 минут
                
                print("О! Начало перемены у группы", i)
                #TO DO: добавить таймер обратного отсчёта
                time.sleep(60*10)   #10 минут
                
                print("О! Конец перемены у группы", i)
                time.sleep(60*30)   #30 минут
                #TO DO: добавить проверку, что ничего не сбилось
                print("О! Конец занятия у группы", i)
        print("Конец рабочего дня!")
        break
bot.run(token)
