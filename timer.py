import datetime
import time


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
    today = datetime.datetime.today()
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

#если сегодня вообще есть занятия
if groups_today != []:
    print(groups_today)

#вывод всего расписания на день
for i in groups_today:
    group = groups[i]
    print(i+" группа ", group[weekday])

while True:
    hours = int(time_now()[0:2])
    minutes = int(time_now()[3:5])
  
    for i in groups_today:
        group = groups[i]
        class_hours = int(group[weekday][0:2])
        print(class_hours)
        
        while hours < class_hours:
            print("для занятия группы", i, "ещё рано")
            time.sleep(3)
            
        #TO DO: добавить оповещение за 10 минут
            
        if hours == class_hours and minutes ==0:
            print(time_now())
            print("О! Начало занятия группы", i)
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
print("Конец работы программы :)")
