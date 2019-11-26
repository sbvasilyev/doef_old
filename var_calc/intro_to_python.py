# Объявление переменных
a = 0
b = 2.3
is_valid = True
some_string = "Это строка"
another_string = 'Это тоже строка'
interpolated_string = f'А можно и так. b = {b}'

# Коллекции
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
some_list[0] = -2
range_from_0_to_20 = range(0, 21)

some_tuple = (1, 2, 3, 4)
ua, ub, uc, ud = some_tuple
print(ua, ub, uc, ud)

some_dict = {
    'value': 5,
    'is_valid': True,
    'name': 'A'
}

print(f'value = {some_dict["value"]} and name = {some_dict["name"]}')

# List comprehension
squared_list = [x ** 2 for x in some_list]
squared_even_list = [x ** 2 for x in some_list if x % 2 == 0]


# Функции
def abs(x):
    if x >= 0:
        return x
    else:
        return -x
