import datetime
import time
from tkinter import *

#время начала занятий

groups = {
    "1": ["09:00"],
    "2": ["10:50"],
    "3": ["16:20"],
    "4": ["16:20"],
    "5": ["09:00" , "14:30"] 
    }


weekdays = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
        ]

#расписание
#мб стоит потом сделать генератор под это дело
#типа keys - дни недели, values - группы по этим дням
#ну или хуй
schedule = {
        "Понедельник": ["5", "4"],
        "Вторник": [],
        "Среда": ["1", "2", "3"],
        "Четверг": [],
        "Пятница": ["5", "4"],
        "Суббота": ["1","2","5", "3"],
        "Воскресенье": []
    }

def time_now():
    time = datetime.datetime.now().strftime("%H:%M")
    return time

def weekday_now():
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    today = datetime.datetime(2021, 2, 13)
    return weekdays[today.weekday()]


if groups["1"] == time_now():
    print("начало занятия у группы 1")


def schedule_today():
    for day in weekdays:
        if day == weekday_now():
            print("сегодня", weekday_now())
            
            return schedule[day]

#==== main ====#
groups_today = schedule_today()

if groups_today != []:
    print(groups_today)
    
print(time_now())





