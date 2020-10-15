import datetime as dt

# ==== data ==== #

DATABASE = {
    'Seryoga': 'Omsk',
    'Sonya': 'Moscow',
    'Dima': 'Chelyabinsk',
    'Alina': 'Krasnoyarsk',
    'Egor': 'Perm'
}

UTC_OFFSET = {
    'Saint Petersburg': 3,
    'Moscow': 3,
    Samara: 4,
    'Novosibirsk': 7,
    'Yekaterinburg': 5,
    'Nizhny Novgorod': 3,
    'Kazan': 3,
    'Chelyabinsk': 5,
    'Omsk': 6,
    'Rostov-on-Don': 3,
    'Ufa': 5,
    'Krasnoyarsk': 7,
    'Perm': 5,
    Voronezh: 3,
    'Volgograd': 4,
    Krasnodar: 3,
    Kaliningrad: 2
}

# ==== functions ==== #

def what_time_in(city):
    now = dt.datetime.utcnow()
    period = dt.timedelta(hours = UTC_OFFSET[city])
    return now + period

def what_time(friend):
    city = DATABASE[friend]
    result = what_time_in(city) 
    return result.strftime('%H:%M') 

# ==== main ==== #
print(what_time('Alina'))