# ==== data ==== #
separator = ', '
all_cities = set([
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
])

used_cities = set(['Калуга', 'Абакан' , 'Новосибирск'])

# ==== functions ==== #
def print_valid_cities(all_cities, used_cities):
    unused_cities = all_cities.difference(used_cities)
    print(separator.join(unused_cities))

# ==== main ==== #
print_valid_cities(all_cities, used_cities)
