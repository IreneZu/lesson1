# Неизменяемые и изменяемые объекты. Кортежи и списки

# tuple
immutable_var  = 'Строка ', 1,2,3, False, None, tuple([1,2,3])
print('Кортеж: ', immutable_var)

# immutable_var[0] = 'Другая строка'
# Нельзя изменить значения элементов кортежа по определению

# list
mutable_list = ['Строка ', 1,2,3, False, None, tuple([1,2,3])]
print('Список: ', mutable_list)
mutable_list[0] = 'Другая строка'
mutable_list[5] = 'Yes'
mutable_list[6] = [1,2,3]
print('Измененный список: ', mutable_list)



