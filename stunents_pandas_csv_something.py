import pandas

#====functions====#
def only_in_group(value):
    return table[table['group'] == value]
        

#====data====#
file = 'students_2021.csv'
table = pandas.read_csv(file)   #table is pandas dataframe (thanks cap)

#====main====#

    #preparation to processing

table.drop('Отметка времени', inplace = True, axis = 1)
table.columns = [   'group', 'name', 'birth','phone',
                    'parents','have_google','have_discord',
                    'discord_name','equipment','skills','practice']
    #processing
num = input('group number')
print(only_in_group(num+'Р')[['group','name','birth']])





