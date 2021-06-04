#List generators

list_1 = [i for i in range(20)]
print(list_1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# Здесь берется ключ из словаря, а в генерируемый список добавляется произведение ключа на его значение.

dict_1 = {1:10, 2:20, 3:30, 4:40}
l = [i*dict_1[i] for i in dict_1 ]
print(l)

# В конец генератора можно добавлять конструкцию if. Например, надо из строки извлечь все цифры:

s = "as1sc2і 3іві9 0"
l=[int(i) for i in s if '0'<=i<='9']
print(l)

"""Выражения-генераторы (generator expressions) доступны, начиная с Python 2.4.
Основное их отличие от генераторов коллекций в том, что они выдают элемент по-одному,
не загружая в память сразу всю коллекцию."""

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a)    # выражение-генератор
print(next(my_gen))     # -2 - получаем очередной элемент генератора
print(next(my_gen))     # -1 - получаем очередной элемент генератора