# ==== data ==== #

FRIENDS = {
    'Seryoga': 'Omsk',
    'Sonya': 'Moscow',
    'Misha': 'Moscow',
    'Dima': 'Chelyabinsk',
    'Alina': 'Krasnoyarsk',
    'Egor': 'Perm',
    'Kolya': 'Krasnoyarsk'
}
sep = ', '

# ==== functions ==== #

def format_friends(friends_count):
    if friends_count == 1:
        return 'You have 1 friend'
    elif friends_count>1:
        return 'You have ' + str(friends_count) + ' friends'
    elif friends_count == 0:
        return 'You have no friens'
    else:
        return 'server error'


def process_query (query):
    if query == 'How many friends do I have?':
        count = len (FRIENDS)
        return format_friends (count)
    elif query == 'Who are all my friends?':
        friends_string = ',' .join (FRIENDS)
        return 'Your friends:' + friends_string
    elif query == 'Where are all my friends?':
        return 'Your friends in cities:' + sep.join (set (FRIENDS.values ​​()))
    else:
        return '<unknown request>'


def runner ():
    print ('Hello, I'm Anfisa!')
    print (process_query ('How many friends do I have?'))
    print (process_query ('Who are all my friends?'))
    print (process_query ('Where are all my friends?'))

# ==== main ==== #

runner()
