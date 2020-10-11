# ==== task ==== #
'''
You are going to go to Khabarovsk.
It would be great to meet friends there.
But does at least one of your friends live in Khabarovsk now?'''



# ==== functions ==== #
def is_anyone_in(collection, city):
    if city in  collection.values(): 
        for name in collection:
            if   collection[name] == city:
                print('In the' + city + 'city lives' + name + '.')
    else:
        print('No one yet.')

# ==== data ==== #
        
friends = {
    'Seryoga': 'Omsk',
    'Sonya': 'Moscow',
    'Dima': 'Chelyabinsk',
    'Alina': 'Khabarovsk',
    'Egor': 'Perm'
}

# ==== main ==== #

is_anyone_in (friends, 'Khabarovsk')
