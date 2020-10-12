# ==== functions ==== #

def check_query(query):
    if query.split(): #проверка списка на пустоту
        if query.split() [0] == 'Анфиса' or query.split() [0] == 'Анфиса,':
            return sep.join(tokens[1:]).strip() 
    else:
        return 'запрос пуст или некорректен'     

def print_query_info(q):
    for q in queries:
        if isinstance(q, str):
            result = check_query(q)
            print(q, '-', result)
        else:
            print('запрос пуст или некорректен')

# ==== data ==== #
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?' #,
#    '  ', 123, ['ddd', 'dd1']
]
            
# ==== main ==== #
            
print_query_info(queries)
