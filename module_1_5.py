# Неизменяемые и изменяемые объекты. Кортежи и списки

immutable_var = 1, 'slow', False, 8.8
print(immutable_var)
immutable_var[1] = ('fast') #получим ошибку т.к. кортеж неизменяем
mutable_list = [1, 'slow', False, 8.8]
mutable_list[0] = 11
mutable_list.append('apple')
mutable_list.extend(['bear'])
mutable_list.remove('slow')
print(mutable_list)
