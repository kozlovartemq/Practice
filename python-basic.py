#!/bin/python3
# Mutable (изменяемые) data types: list, dicts, set, user-defined classes
# Immutable data types: int, float, decimal, bool, string, tuple, range

# Decimal - более точные, чем float, но медленнее, тк реализован программно
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 1  # Количество знаков после запятой (def = 28)
a = Decimal(0.1) + Decimal(0.1) + Decimal(0.1)
if a == Decimal(0.3):
	print("True")

# Print string
print("Hello")
print('World')
print("""This is 
a multi-line string!"""+"text1"'\n'"text2.")

# Math
print(2 ** 3)  # exp
print(5 / 2)
print(5.0 / 2)
print(5 // 2)  # отбрасывает числа после запятой
print(5 % 2)   # mod

# Strings - не изменяемый тип данных (при взаимодействии создается новая строка)
a = "Cool things are coming!"
print(len(a))     # length
print(a.upper())  # CAPS
print(a.lower())
print(a.title())  # Каждое слово с большой буквы
print(a.capitalize()) # Первый символ с большой буквы, остольные с нижним регистром


too_much_space = "      hello      "
print(too_much_space.strip())  # удалить символ из строки (пробел по дефолту)

full_name = "Elon Mask"
print(full_name.replace("Elon", "Green"))
print(full_name.find("Mask"))  # = 5 (the index of first occurrence)

age = 22    # type(age) = integer
ves = 68.8  # type(age) = float
print(age)
print("Hello, Iam " + str(age) + "yo")  # в строку не может писаться значение в int, его переводят в строку str()
Movie = "Gifted"
Place = "Netflix"
print("how to write \" in a string")
print("I have watched \"" + Movie + "\" on " + Place)
print("I have watched \"{}\" on {}".format(Movie, Place))  # в скобках можно указывать индекс параметра в функции format вот так {0}
print(f'I have watched "{Movie}" on "{Place}"')

word = "Word"
print(word[0])   # первая буква
print(word[-1])  # последняя буква
sentence = "This is a sentence."
print(sentence[:4])      # первое слово
print(sentence[-9:-1])   # последнее слово
sentence_split = sentence.split()  # Разбить слова в отдельные Айтемы (разделитель - пробел по дефолту)
print(sentence_split)   # srt -> list
sentence_join = ' '.join(sentence_split)  # Соединить строку из отдельных Айтемов разделяя из разделителем ' '
print(sentence_join)    # list -> str
print('\n'.join(sentence_split))  # Соединить строку из отдельных Айтемов, но каждое слово будет записываться с новой строки

def printiwant(m, p):
	return print("I have watched \"{}\" on {}".format(m, p))


printiwant("Arrow", "torrent")

# Определение и вызов функции
def myfunc1():
	birthday = 1
	agenow = 22
	agenow += birthday
	print(agenow)


myfunc1()  # без аргументов, вычисления проходят только внутри функции (внутрь ничего не входит и не выходит)

def myfunc(agenow):
	birthday = 1
	agenow += birthday
	print(agenow)

myfunc(20)  # аргументы функции для того, чтобы брать значения из остальной проги
age = 27
myfunc(age)


def mysqrt(x, y):  # x,y - параметры
	m = x ** .5  # корень квадратный
	return m + y

print(mysqrt(64,2))  # использование нескольких аргументов и возврат числа

# Boolean
bool1 = True				 # boolean
bool2 = "True" 				 # string
bool3 = 3*3 == 9			 # True
bool4 = 4 <= 9				 # True
bool5 = (3 != 4) or (3 > 3)  # True
bool6 = not False			 # True
print(type(bool1), type(bool2), bool3, bool4, bool5)

letter = "a"
word = "Apple"
print("A" in "Apple")  # True
print(letter in word)  # False
print(letter.lower() in word.lower())  # True (не учитывая регистр)

# Conditional
def myfuncif(age, money):
	if (age >= 21) and (money >= 5):
		return "its yours!"
	elif (age >= 21) and (money < 5):
		return "need more money!"
	elif (age < 21) and (money >= 5):
		return "U A a KID!"
	else:
		return "this kid has no money!"

mon = 3
print(myfuncif(22, mon))

# Lists (Массивы) - индексы начинаются с нуля
mas = ["0 First", "1 Second", "2 Third", "3 Fourth", "4 Fifth", "5 Sixth"]
print(len(mas))      	  # length									  6
print(mas[1:3])   		  # show 2nd and 3rd items					  ['1 Second', '2 Third']
print(mas[1:])    		  # show 2nd till the end					  ['1 Second', '2 Third', '3 Fourth', '4 Fifth', '5 Sixth']
print(mas[:2]) 		 	  # show from start to 2nd					  ['0 First', '1 Second']
print(mas[-1])    	 	  # show LAST item							  5 Sixth
print(mas[::-1])  	 	  # reverse list and show all items			  ['5 Sixth', '4 Fifth', '3 Fourth', '2 Third', '1 Second', '0 First']
mas.append("6 Seventh")   # add item on LAST position
mas.insert(0, "element")  # add item on certain index
print(mas.pop())  		  # RETURN and remove item from last position  6 Seventh
print(mas.pop(1))		  # -//- from certain index					   0 First
mas.remove("element")	  # remove certain item
print(mas)				  # ['1 Second', '2 Third', '3 Fourth', '4 Fifth', '5 Sixth']
mas = ["0hey", "1wake", "2up"]
sam = ["0am", "I", "2wrong", "3yet"]
mas += sam  		  	  # == mas.extend(sam):  ["0hey", "1wake", "2up", "0am", "I", "2wrong", "3yet"]
combined = zip(mas, sam)  # склеить массивы
print(list(combined))	  # [("0hey", "0am"), ("1wake", "I"), ("2up", "2wrong")] - для 4ого элемента в 'sam' нет пары
mas.strip()  			  # удалить все (или заданные в скобках символы) из начала и конца строки
sam.count("I") 			  # количество элементов "I": 1
sam.clear()				  # []
sam = ["1", "z", "A", "9", "a", "Z"]
sam.sort()				  # ['1', '9', 'A', 'Z', 'a', 'z']

# Tuples (Кортежи - Статичесские массивы, которые не изменяются) -
# быстрее, чем лист, но лист более эффективен с точки зрения использования памяти (при изменении новый лист не создается)
grades = ("A", "B", "C", "D", "F")
grades += ("E", "G")  #  при попытке изменения кортежа создается новый Кортеж
print(grades[1])	#  нельзя переопределять значения Кортежа grades[0] = "X"
grades.index[0]
grades.count("A")

# Sets - множества (неповторяющиеся неизменяемые (число, строка, кортеж) элементы в рандомном порядке) - быстрая проверка принадлежности
set1 = {'a', 'o', 'u', 'i', 'e'}
set2 = set([1, 2, 3, 4, "df", "ds"])
if 'e' in set1:
	print('Optimisation!')
set1.add("a")
set1.discard("a")  		  		 # remove, if there is no item 'a', nothing happens
set1.remove("a")  		  		 # if there is no item 'a', KeyError raise
set3 = set1.union(set2)   		 # union 2 sets
set1.update(set2)		 		 # union 2 sets in set1
set4 = set1.intersection(set2)	 # сохранение в новое множество только пересечение множеств
set5 = set1.difference(set2)	 # новое множество = все элементы из set1, кроме тех, которые есть в set2


# Dictionaries - словари, имеют "ключи" и "значения" - такая же скорость, как Кортеж
user1 = ["login", "pass"]
user2 = ["login2", "pass2"]
user3 = ["login3", "pass3"]
print(dict([user1, user2, user3]))  # {'login': 'pass', 'login2': 'pass2', 'login3': 'pass3'}
drinks = {"Cola": 55, "Vodka": 350}
drinks = dict(Cola=55, Vodka=350)
d1 = dict.fromkeys([1, 2, 3], "Value")  # {1: 'Value', 2: 'Value', 3: 'Value'}
drinks['Cola'] = 60
drinks.update({"Soda": ["mb malo", "mb mnogo"]})
print(drinks)       	      # {'Cola': 60, 'Vodka': 350, 'Soda': ['mb malo', 'mb mnogo']}
d2 = drinks.copy()
print(drinks.get("Soda"))     # == print(drinks["Soda"]) = ["mb malo", "mb mnogo"]
print(*drinks.get("Soda"))    #  mb malo mb mnogo (* - UNPACKING)
print(drinks.get("Soda")[0])  #  mb malo
print(drinks.get("Martini"))  # None
print(drinks.get("Martini", "NOT IN DICT"))  # NOT IN DICT
print(drinks.values())  # for loop: for value in drinks.values():	(Для экономии ресурсов)
print(drinks.keys())  # for loop: for key in drinks.keys():
print(drinks.items())  # for loop: for key, value in drinks.items():
print(drinks.pop())  # возвращает и удаляет элемент словаря (последний по умолчанию)

# Сделать из двух листов словарь
NAMES = ["kate", "Mary", "Elza"]
AGE = ["18", "24", "43"]
COMBINED = zip(NAMES, AGE)
new_dictionary = {key: value for key, value in COMBINED}
print(new_dictionary)  # {'kate': '18', 'Mary': '24', 'Elza': '43'}

# Looping
family = ["Mum", "Dad", "Bro", "Sis"]
for x in family:
	print(x)

# Exception Handling (Обработка исключений)
"""List of exceptions:
https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
"""
while True:
	try:
		enter = float(input("Enter a number: "))
		result = 100 / enter

	except ValueError:
		print("You entered not a number!")

	except ZeroDivisionError:
		print("You can't divide by zero!")

	except:  # Handling other exceptions
		print("Something went wrong!")

	else:  # Run if 'try:' ran without errors
		print(f'100/{enter} = {result}')
		break

	finally:  # Run no matter what
		print("The code is running no matter what")

# Working with files
# Context manager WITH AS
"""
'r' - открытие на чтение (является значением по умолчанию).
'w' - открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
'x' - открытие на запись, если файла не существует; Исключение, если файл существует.
'a' - открытие на дозапись, информация добавляется в конец файла.
'+' - открытие на чтение и запись
't' - открытие в текстовом режиме (является значением по умолчанию).
'b' - открытие в двоичном режиме
"""
data_list = ["Important data1\n", "Important data2\n", "Important data3\n"]
with open('file.txt', 'w') as r:  # do not need to r.close()
	r.writelines(data_list)
	print(r.writable())  	  # True
	r.write("Something")

with open('file.txt', 'r') as r:
	print(r.readable())       # True
	print(r.read())           # read(bytes) file
	print(r.readlines())      # ['Important data1\n', 'Important data2\n', 'Important data3\n', 'Something']
	print(r.readline())       # read 1 line
	print(r.encoding)

# Decorator
def my_decorator(func):
	def wrapper():
		print("The code before func:")
		t1 = datetime.now()
		func()
		print("The code after func:")
		print(datetime.now() - t1)
	return wrapper

@my_decorator  # my_function = my_decorator(my_function)
def my_function():
	string = "Something"
	time.sleep(0.3)
	print(string)

my_function()

# List, dict, set comprehensions (Генераторы списков, словарей, множеств)
import os
list1 = [i for i in range(1, 11)]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [i ** 2 for i in list1] + list1  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = [i for i in list2 if i % 2 == 0 and i > 50]  # [64, 100]
set1 = {i for i in list2}  # {64, 1, 2, 3, 4, 36, 100, 5, 6, 9, 7, 8, 10, 16, 49, 81, 25}
dict1 = {i: i ** 2 for i in list1}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
dict2 = {x: round(x * 0.3267, 2) for x in dict1.values() if x <= 25}  # {1: 0.33, 4: 1.31, 9: 2.94, 16: 5.23, 25: 8.17}
list4 = [os.path.join(z, i) for z, x, c in os.walk(os.getcwd()) for i in c if '.py' in i]
print('\n'.join(list4))

# Выражение генератор - при работе с большими данными использует мало памяти и может итерироваться в цикле
import os
list5 = [x for x in range(20)]
list6 = [x for x in range(20000)]
generator = (x for x in range(20))
generator2 = (x for x in range(20000))
print(f'{type(list5)} size: {list5.__sizeof__()} bytes.')			 # <class 'list'> size: 120 bytes.
print(f'{type(list6)} size: {list6.__sizeof__()} bytes.') 			 # <class 'list'> size: 89000 bytes.
print(f'{type(generator)} size: {generator.__sizeof__()} bytes.')    # <class 'generator'> size: 48 bytes.
print(f'{type(generator2)} size: {generator2.__sizeof__()} bytes.')  # <class 'generator'> size: 48 bytes.
for i in generator:
	print(i)

