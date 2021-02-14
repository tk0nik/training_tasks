import datetime
import time
from tkinter import *

#время начала занятий

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

#лучше вместо этого потом использовать dict keys
weekdays = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
        ]

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

#убрать потом это из функций (будет юзаться только при включении)
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
weekday = weekday_now()

if groups_today != []:
    print(groups_today)
    
print(time_now())

for i in groups_today:
    group = groups[i]
    print(group[weekday])

