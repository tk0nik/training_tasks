# ==== task ==== #
'''If you need 5 kg of tomatoes for salad and 3 kg for soup, you immediately buy 8 kg.
Write a function that will print on the screen what products you need to buy and how many you need.
Print information about each ingredient on a separate line in the format: cucumbers, kg: 1.5.
Each product should only appear once in the output.'''

# ==== functions ==== #

def print_dict(d):
    for i in d:
        print(i, d[i])

def print_shopping_list(r1, r2):
    uniq_prod = set(r1.keys()).union(set(r2.keys()))
    result = {}
    for i in uniq_prod:
        if i in r1 and i in r2:
            result[i] = r1[i]+r2[i]
        elif i in r1:
            result[i] = r1[i]
        else:
            result[i] = r2[i]
    #return result
    print_dict(result)

# ==== data ==== #

pizza = {'flour, kg': 1,
         'tomatoes, kg': 1.5,
         'champignons, kg': 1.5,
         'cheese, kg': 0.8,
         'olive oil, l': 0.1,
         'yeast, g': 50}
salad = {'cucumbers, kg': 1,
         'peppers, kg': 1,
         'tomatoes, kg': 1.5,
         'olive oil, l': 0.1,
         'lettuce, kg': 0.4}

# ==== main ==== #

print_shopping_list(pizza, salad)
