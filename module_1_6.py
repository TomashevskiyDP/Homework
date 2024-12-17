# Практическое задание по теме: "Словари и множества"

my_dict = {'Liverpool': 36, 'Chelsea': 34, 'Arsenal': 30, 'Nottingham Forest': 28, 'Manchester City': 27}
print('Пятерка лидеров АПЛ:', my_dict)
print('Количество очков у Арсенала:', my_dict['Arsenal'])
print('Количество очков у Эвертона:', my_dict.get('Everton', None))
my_dict['AFC Bournemouth'] = 25
my_dict['Aston Villa'] = 25
print('Количество очков у чемпиона сезона 23/24:', my_dict.pop('Manchester City'))
print('Верх таблицы АПЛ без Мансити:', my_dict)

my_set = {1,2,8.8,'APL',2,'APL'}
print(my_set)
my_set.add((6.6, 7.7, 'nike'))
my_set.add(False)
my_set.remove(2)
print('Modified set:', my_set)