#!/bin/python3

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

# Funcs and Methods with strings
a = "Cool things are coming!"
print(len(a))     # length
print(a.upper())  # CAPS
print(a.lower())
print(a.title())  # Каждое слово с большой буквы

age = 22    # type(age) = integer
ves = 68.8  # type(age) = float
print(age)
print("Hello, Iam " + str(age) + "yo")  # в строку не может писаться значение в int, его переводят в строку str()
Movie = "Gifted"
Place = "Netflix"
print("I have watched \"" + Movie + "\" on " + Place)
print("I have watched \"{}\" on {}".format(Movie, Place))
# в скобках можно указывать индекс параметра в функции format вот так {0}


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


def mysqrt(x,y):
	m = x ** .5  # корень квадратный
	return m + y

print (mysqrt(64,2))  # использование нескольких аргументов и возврат числа

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
mas = ["0hey", "1wake", "2up"]
print(len(mas))  # length
print(mas)
print(mas[1:2])   	 # show 2nd and 3rd items
print(mas[1:])    	 # show 2nd till the end
print(mas[:1]) 		 # show from start to 2nd
print(mas[-1])    	 # show LAST item
print(mas[::-1])  	 # reverse list and show all items
mas.append("Baddy")  # add item on LAST position
print(mas)
mas.pop()  			 # RETURN and remove item from last position
print(mas)
mas.pop(1) 			 # remove item from 2nd position
print(mas)
mas = ["0hey", "1wake", "2up"]
sam = ["0am", "I", "2wrong", "3yet"]
print(mas + sam)  		  # ["0hey", "1wake", "2up", "0am", "I", "2wrong", "3yet"]
combined = zip(mas, sam)  # склеить массивы
print(list(combined))	  # [("0hey", "0am"), ("1wake", "I"), ("2up", "2wrong")] - для 4ого элемента в 'sam' нет пары
mas.strip()  			  # удалить все (или заданные в скобках символы) из начала и конца строки

word = "Word"
print(word[0])   # первая буква
print(word[-1])  # последняя буква
sentence = "This is a sentence."
print(sentence[:4])      # первое слово
print(sentence[-9:-1])   # последнее слово
print(sentence.split())  # Разбить слова в отдельные Айтемы (разделитель - пробел по дефолту)
sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)  # Соединить строку из отдельных Айтемов разделяя из разделителем ' '
print(sentence_join)
print('\n'.join(sentence_split))  # Соединить строку из отдельных Айтемов, но каждое слово будет записываться с новой строки

print("how to write \" in a string")

too_much_space = "      hello      "
print(too_much_space.strip())  # удалить символ из строки (пробел по дефолту)

full_name = "Elon Mask"
print(full_name.replace("Elon", "Green"))
print(full_name.find("Mask"))  # = 5 (the index of first occurrence)

# Tuples (Кортежи - Статичесские массивы, которые не изменяются) - быстрее, чем лист
grades = ("A", "B", "C", "D", "F")
print(grades[1])

# Sets - множества (неповторяющиеся элементы в рандомном порядке) - быстрая проверка принадлежности
set1 = {'a', 'o', 'u', 'i', 'e'}
if 'e' in set1:
	print('Optimisation!')

# Dictionaries - словари, имеют "ключи" и "значения"
drinks = {"Cola": 55, "Vodka": 350}
print(drinks)
drinks['Cola'] = 60
drinks.update({"Soda": ["mb malo", "mb mnogo"]})
print(drinks)
print(drinks.get("Soda"))   # == print(drinks["Soda"]) = ["mb malo", "mb mnogo"]
print(*drinks.get("Soda"))  # = mb malo mb mnogo (* - UNPACKING)
print(drinks.get("Martini"))  # None

# Сделать из двух листов словарь
NAMES = ["kate", "Mary", "Elza"]
AGE = ["18", "24", "43"]
COMBINED = zip(NAMES, AGE)
new_dictionary = {key: value for key, value in COMBINED}
print(new_dictionary)

# Looping
family = ["Mum", "Dad", "Bro", "Sis"]
for x in family:
	print(x)
