"""1) OrderedDict - упорядоченный словарь, оптимизирован для работы с порядком элементов в словаре.
Позволяет доставать пары как с конца так и с начала словаря, переставлять пары в конец или начало словаря.
При сравнении учитывает порядок элементов, а не только их равенство.
За все это платит большим потреблением памяти."""
from collections import OrderedDict

d1 = {4: '00', 1: '01', 2: '02'}
d2 = {1: '01', 0: '00', 2: '02'}
print(d1 == d2)  #  True

od1 = OrderedDict(d1)  # хранит значения словаря (копирует словарь)
od2 = OrderedDict(d2)
print(od1 == od2)  # False

print(d1.popitem())
print(od1.popitem(last=False))  # возвращает и удаляет ПЕРВЫЙ элемент
od2.move_to_end(key=0, last=False)  # переместить элемент с ключом "0" в НАЧАЛО (True - в конец)
print(od2)

"""2) ChainMap нужен для логического объединения словарей для поиска информации, 
физического копирования словарей не происходит и если изменить один из исходников, то изменение отобразится и в chainMap. 
Удобен для поиска информации, но при изменениях меняется первый словарь в наборе."""
from collections import ChainMap

d3 = {0: '00', 1: '01', 2: '02'}
d4 = {3: '03', 4: '04', 5: '05'}
chain = ChainMap(d3, d4)  # хранит ссылки (при последующем изменении поменяется вместе с оригинальным словарем)
print(chain)
d3[0] = 'wrong'
print(chain)
print(1 in chain)  # True
print(4 in chain)  # True
chain[4] = '000444'
print(chain)  # ChainMap({0: 'wrong', 1: '01', 2: '02', 4: '000444'}, {3: '03', 4: '04', 5: '05'})
print(d3)  # {0: 'wrong', 1: '01', 2: '02', 4: '000444'}

"""3) Counter - удобный инструмент для подсчета элементов в последовательности,
считает только iterable или словарь (т.к. он их перебирает) 
с hashable (т.к. создает словарь) типами данных внутри (строки, числа, кортежи)."""
from collections import Counter

d5 = {3: '03', 4: '04', 5: '05', 'a': '2', 'b': '3'}
array = 'hello WOrld'
counter1 = Counter(d5)  # хранит значения (при изменении d5, counter уже не меняется)
counter2 = Counter(array)
print(counter1)
d5[3] = '000333'
print(counter1)  # Counter({3: '03', 4: '04', 5: '05', 'a': 0, 'b': '3'})
print(counter2)  # Counter({'l': 3, 'h': 1, 'e': 1, 'o': 1, ' ': 1, 'W': 1, 'O': 1, 'r': 1, 'd': 1})
print(type(counter2.most_common()), counter2.most_common())  # <class 'list'> [('l', 3), ('h', 1), ('e', 1), ('o', 1), (' ', 1), ('W', 1), ('O', 1), ('r', 1), ('d', 1)]
print(counter2.most_common(2))  # [('l', 3), ('h', 1)] - вывести "2" самых частых символа
print(counter2.pop('l'))  # можно пользоваться методами dict

"""4) defaultdict нужен для создания словаря со значением по умолчанию.
Значение подставляется при обращении к несуществующему ключу, что позволяет не писать лишней логики.
В остальном аналогичен обычному словарю."""
from collections import defaultdict

d6 = {'0': '1', '2': '3', '4': 5}
d_dict = defaultdict(int)  # в параметрах указывается функция, которая выполнятся при обращении
                           к несуществующему элементу (тип значения по умолчанию)
print(int())  # 0

print('5' in d_dict)  # False
print(d_dict['5'])  # 0
print(d_dict)  # defaultdict(<class 'int'>, {'5': 0})
d_dict.update(d6)
print(d_dict)  # defaultdict(<class 'int'>, {'5': 0, '0': '1', '2': '3', '4': 5})

l1 = [(0, '00'), (1, '01'), (2, '02')]
d_dict2 = defaultdict(str, l1)
print(d_dict2)  # defaultdict(<class 'str'>, {0: '00', 1: '01', 2: '02'})

"""5) deque - двунаправленная очередь, быстро вставляет элементы как в конец, так и начало, быстро достает с обоих концов.
Она потокобезопасна (thread-safe) и может быть использована для многопоточных операций, позволяет задать максимальный размер."""
from collections import deque

deq = deque(maxlen=5)
deq.extend([3, 4])
deq.extendleft([-2, -1])
deq.append(1)
print(deq)  # deque([-1, -2, 3, 4, 1], maxlen=5)
deq.appendleft(0)
print(deq)  # deque([0, -1, -2, 3, 4], maxlen=5)
deq.pop()  # нельзя передавать индекс
deq.popleft()
print(deq[-1])  # можно обращаться по индексу, но не по срезу

l2 = [(0, '00'), (1, '01'), (2, '02')]
deq2 = deque(l2, maxlen=1)
print(deq2)  # deque([(2, '02')], maxlen=1)
print(deq2[0][1])  # 02

"""6) namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом. 
Пригодится когда отдельный класс избыточен.
Неизменяемый, позволяет обращаться по имени атрибута (причем быстро), позволяет использовать индексы."""
from collections import namedtuple

Point = namedtuple('Point', 'x y')
point1 = Point(0, 0)
print(point1)
print(point1.y)

Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'brown')
print(tom)
print(tom.name)
print(tom.age)  # обращение по атрибуту
print(tom[2])  # обращение по индексу
