import datetime

class DescriptorInt:
    """Дескриптер данных содержит геттер, сеттер и делиттер.
    Если требуется присвоить нескольким private свойствам значения и одинаковыми проверками,
    правильнее написать один дескриптер, чем несколько свойств @property для предотвращения дублироваания кода."""
    @staticmethod
    def __check_int(value):
        if type(value) != int:
            raise TypeError('Вы ввели не целое число.')

    def __set_name__(self, owner, name):
        self.name = '_' + name  # геттер/сеттер и атрибут не должны иметь одинаковое имя. Это ведет к бесконечной рекурсии
                                # добавление '__' НЕ ДЕЛАЕТ атрибут private
    """
       self - ссылка на экземпляр класса DescriptorInt
       instance - ссылка на экземпляр myfirstwallet класса Wallet (в котором создан экземпляр класса DescriptorInt)
       owner - ссылка на сам класс Wallet (в котором создан экземпляр класса DescriptorInt)
    """
    def __get__(self, instance, owner):
        print(f'{owner.attrib} -- attribute of owner')
        return getattr(instance, self.name)  # instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.__check_int(value)
        setattr(instance, self.name, value)  # instance.__dict__[self.name] = value

    def __delete__(self, instance):
        delattr(instance, self.name)


class Wallet:
    """A class for creating some wallets.
    attribute (public)
    _attribute (protected) - для обращения внутри класса и во всех дочерних классах. Но если обратиться из вне, ошибка не вызовается.
    __attribute (private) - для обращения только внутри класса. При обращении из вне, вызывается ошибка"""
    __instance = None
    __CURRENCY_LIST = ["USD", "RUB", "EUR"]  # Атрибут (свойство) класса
    attrib = 0
    """Создание экземпляра дескриптера данных"""
    x = DescriptorInt()
    y = DescriptorInt()
    z = DescriptorInt()

    """Вызывается перед созданием объекта класса. 
       cls ссылается на текущий класс
       super() = class object -- базовый класс, от которого неявно наследуются все классы"""
    def __new__(cls, *args, **kwargs):  # В параметры передаются аргументы для init
        """Пример: Паттерн Singleton (anti-Pattern) - не дает создавать больше одного экземпляра класса.
        Остальные экземпляры - ссылки на первый экземпляр"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Возвращает адрес нового созданного объекта
        return cls.__instance

    """Вызывается сразу после создания объекта класса.
       self ссылается на созданный экземпляр класса"""
    def __init__(self, currency, owner_name, attr=-5, x=-8, y=3, z=-2):
        self.__currency = self.__check_currency(currency)
        self.__money = 0.00
        self.__owner_name = self.__check_name(owner_name)
        self.x = x
        self.y = y
        self.z = z
        self.attribute = attr
        self.somelist = [0, 1, 2, 3, 4]

    """Вызывается при вызове экземпляра() класса.
       Классы, имеющие __call__ - называются функторами"""
    def __call__(self, *args, **kwargs):
        pass

    """Вызывается, когда на экземпляр класса больше нет ссылок"""
    def __del__(self):
        self.__instance = None

    def info(self):  # метод класса
        return f'{self.__owner_name} has {self.__money} {self.__currency}'

    """Интерфейсные методы"""
    @property  # getter - позволяет посмотреть на private атрибуты
    def usemoney(self):
        return self.__money

    @usemoney.setter  # setter - позволяет изменять private атрибуты
    def usemoney(self, value):
        if isinstance(value, int):
            if self.__money + value >= 0.00:
                self.__money = self.__money + value
            else:
                raise ValueError("Недостаточно средств на кошельке.")
        else:
            raise TypeError("Значение должно быть целым числом.")

    @usemoney.deleter  # deleter - позволяет удалить private атрибут. Вызов: del myfirstwallet.usemoney
    def usemoney(self):
        del self.__money

    """Простая ф-ция внутри класса, которая ничего не знает ни об атрибутах класса, ни об экземпляре класса
    Определение неизменяемо через наследование."""
    @staticmethod
    def __check_name(name):
        if type(name) != str:
            raise ValueError(f'Имя должно быть строкой.')
        return name

    """Метод, который получает класс в качестве первого неявного аргумента.
    Имеет доступ ко всем атрибутам (сво-ва и методы) класса, но не к экземплярам класса.
    Можно переопределять через наследование."""
    @classmethod
    def __check_currency(cls, currency):
        if currency in cls.__CURRENCY_LIST:
            return currency
        else:
            raise ValueError(f'Недопустимая валюта. Допустимо: {cls.__CURRENCY_LIST}')

    """Магический метод вызывается всякий раз при обращении к ЛЮБОМУ атрибуту класса"""
    def __getattribute__(self, item):
        print(f"Сработал getattribute on {repr(item)}")
        return object.__getattribute__(self, item)

    """Магический метод вызывается всякий раз при присвоении значения к любому атрибуту класса
    Можно создать черный список имен атрибутов."""
    def __setattr__(self, key, value):
        if key == "xx":
            raise AttributeError("Недопустимое имя атрибута!")
        else:
            object.__setattr__(self, key, value)

    """Магический метод вызывается всякий раз при обращении к НЕСУЩЕСТВУЮЩЕМУ атрибуту класса"""
    def __getattr__(self, item):
        print(f"атрибута {item} не существует.")

    """Переопределение метода, удаляющего атрибут (добавление вывода в консоль)"""
    def __delattr__(self, item):
        object.__delattr__(self, item)
        print(f'Атрибут {repr(item)} был удален.')

    """Получение значения по ключу(индексу) в атрибуте класса (для словарей, листов, кортежей)"""
    def __getitem__(self, item):
        return self.somelist[item]

    """Присвоение значения по ключу(индексу) в атрибуте класса"""
    def __setitem__(self, key, value):
        if key >= len(self.somelist):
            extendvar = key + 1 - len(self.somelist)
            self.somelist.extend([None] * extendvar)
        self.somelist[key] = value

    """Удаление значения по ключу(индексу) в атрибуте класса"""
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('')
        del self.somelist[key]

    """Для отображения инфы об объекте класса для пользователей (например, для print, str)
       Если __str__ не определен, будет вызван __repr__"""
    def __str__(self) -> str:
        return self.info()

    """Для отображения инфы об объекте класса в режиме отладки"""
    def __repr__(self) -> str:  # вызвать в python console: >> myfirstwallet
        return self.info()

    """Позволяет применять ф-цию len() к экземплярам класса,
        а также ф-цию bool(), если __bool__ не определен (True, если len(myfirstwallet) != 0)"""
    def __len__(self):
        return len(self.__dict__)

    """Позволяет к экземплярам класса применять ф-цию bool() - возращает True, если данные отличны от 0 или не являются пустыми -
      bool(1) - True; bool(0) - False; bool("") - False; bool([]) - False; bool("Hello") - True"""
    def __bool__(self) -> bool:
        return self.attribute != 0

    """Позволяет применять ф-цию abs() - значение модуля числа к экземплярам класса"""
    def __abs__(self):
        return abs(self.attribute)

    """Позволяет применять сложение ( + ) к экземпляру(ам) класса"""
    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet('USD', f'{self.__owner_name} + {other.__owner_name}',
                          attr=self.attribute + other.attribute)
        return self.attribute + other

    def __radd__(self, other):  # определяет действия, когда экземпляр класса записан справа от +
        return self + other

    def __iadd__(self, other):  # определяет действия при операторе +=
        self.attribute += other
        return self

    def __sub__(self, other): # '-'
        pass

    def __mul__(self, other):  # '*'
        pass

    def __truediv__(self, other):  # '/'
        pass

    def __floordiv__(self, other):  # '//'
        pass

    def __mod__(self, other):  # '%'
        pass

    def __eq__(self, other): # '==' - тоже, что и not( c1 != c2 ) - __ne__ можно не определять
        if not isinstance(other, (int, Wallet)):
            raise TypeError('Операнд справа не int/Wallet')
        sc = other if isinstance(other, int) else other.attribute
        return self.attribute == sc

    def __ne__(self, other):  # '!='
        pass

    def __lt__(self, other):  # '<' - тоже, что и not( c2 > c1 ) - __gt__ можно не определять
        pass

    def __gt__(self, other):  # '>'
        pass

    def __le__(self, other):  # '<=' - тоже, что и not( c2 >= c1 ) - __ge__ можно не определять
        pass

    def __ge__(self, other):  # '>='
        pass

    """hash() - вычисление хэша неизменяемых объектов (для одинаковых объектов получается одинаковый хэш (наоборот невсегда верно))
    Словари используют в качестве ключей - их хэши, тк это быстрее, если хэши совпадают -- поиск по самому ключу
        поэтому ключи должны быть неизменяемыми типами данных.
    При сравнении экземпляров класса, по умолчанию они будут False с разными хэшами.
    При сравнении экземпляров класса с определенным __eq__ при выполнении условий, они будут True, но unhashable, тк стандартный алгоритм сравнения ломается
    При сравнении экземпляров класса с определенными __eq__ и __hash__, при выполнении условий они будут True с одиаковым хэшем,
        что значит, что два экземляра будут ссылками на один и тот же объект.
    """
    def __hash__(self):
        return hash(self.attribute)

"""class FRange"""
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    """Метод для того, чтобы сделать экземпляр итерируемым (функция iter() вызывается неявно внутри цикла for)"""
    def __iter__(self):
        return self

    """Для вызова функции next() - возвращает следующее значение"""
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

"""Class-decorator"""
class Derivate:
    """Вычисление производной"""
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate
def parabola(x):
    return x*x

"""Наследование"""
from abc import ABC, abstractmethod
class Geom(ABC):  # ABC - Abstract Base Class
    name = "Geom"

    """Можно создать белый список разрешенных имен локальных атрибутов экземпляра. 
    __dict__ при этом НЕ формируется, тк к нему можно было бы вручную добавлять атрибуты.
    + : ограничение создаваемых лок-ых св-в
    + : уменьшение занимаемой памяти
    + : ускорение работы с лок-ми св-ми
    __slots__ не наследуется в дочерние классы, но не дает отобразить лок-ые св-ва экземпляра в __dict__ дочернего класса,
    если они записаны в __slots__ базового класса"""
    __slots__ = ('x1', '_x2', '__y2', 'y1')

    def __init__(self, x1, x2, y1, y2):
        print(f"__init__ in Geom for {self.__class__}")
        self.x1 = x1
        self._x2 = x2  # '_x2' - protected - для использования в базовом и дочерних классах, но не вызывает ошибку, если обращаться в других местах
        self.y1 = y1
        self.__y2 = y2  # '_Geom__y2' - если сделать private, то нельзя будет явно использовать в дочерних классах

    """Абстрактный класс - класс, который содержит один и более абстракных методов
    абстрактный метод - метод, который не имеет своей реализации 
                                                    и который обязательно нужно переопределять в дочерних классах.
    Если использовать ABC и @abstractmethod, то попытка создать экземпляр базового класса приведет к ошибке."""
    @abstractmethod
    def get_perimetr(self):
        raise NotImplementedError("В дочернем классе нужно переопределить метод get_perimetr()")

"""При множественном наследовании обычно только первый базовый класс получает параметры, чтобы избежать путаницу."""
class TimeRecord:
    def get_date(self):
        self.time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"TimeRecord's method: {self.time}")

class Rectangle(Geom, TimeRecord):
    def __init__(self, x1, x2, y1, y2):
        print(f"__init__ in Square for {self.__class__}")
        super().__init__(x1, x2, y1, y2)  # == Geom.__init__(self, x1, x2, y1, y2) - обращение к базовому классу (делегирование)
        self.attr = 50

    def get_perimetr(self):
        return 2 * (self._x2 - self.x1 + self._Geom__y2 - self.y1)

class Square(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        print(f"__init__ in Square for {self.__class__}")
        super().__init__(x1, x2, y1, y2)  # == Geom.__init__(self, x1, x2, y1, y2) - обращение к базовому классу (делегирование)
        self.fill = fill

    def get_perimetr(self):
        return 4 * (self._x2 - self.x1)

"""Пользовательские классы исключений"""
class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""
    def __init__(self, *args):
        self.msg = args[0] if args else "общая ошибка принтера"

    def __str__(self):
        return f"Ошибка: {self.msg}"

class ExceptionPrintSendData(ExceptionPrint):
    def __init__(self, *args):
        self.msg = args[0] if args else "принтер не отвечает"

"""Пользовательский менеджер контекста (context manager)"""
class DefendList:
    def __init__(self, array):
        self.__array = array

    def __enter__(self):
        self.__temp = self.__array[:]  # срез [:] нужен, чтобы присвоить temp значения array (сделать копию),
                                        # а не создать вторую ссылку на тот же объект
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:  # если не произошло ошибки внутри with as
            self.__array[:] = self.__temp
        return False  # если ошибки возникли внутри with as, то они не обрабатываются автоматически (программа останавливается)
                      # если True, то ошибки обрабатываются и исключения не вызываются

"""Вложенные классы (пример из Django) - для создания низависимого пространства имен, 
например для предупреждения использования служебных атрибутов
При создании экземпляра внешнего класса, объект внутреннего класса не создается, 
но его можно создавать как лок-ый атрибут внешнего класса.
Также, ссылаться на свойства внешнего класса во внутреннем считается анти-паттерном."""
class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'

    def __init__(self, user, passwd):
        self._user = user
        self._passwd = passwd
        self.meta = self.Meta(user + '@' + passwd)  # Композиция - создание экземпляра класса в другом классе

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access

"""Метакласс - объект класса type; класс, который создает другие классы.
Его нельзя динамически пораждать другим метаклассом"""
class MetaC(type):
    def __new__(cls, name: str, bases: tuple, attrs: dict):
        attrs.update({'attribute': 100, 'attribute2': [1, 2, 3]})
        return type.__new__(cls, name, bases, attrs)

class Point(metaclass=MetaC):
    def __init__(self, x1, y1):
        super().__init__()
        self.x1 = x1
        self.y1 = y1

    def get_coords(self):
        return self.x1, self.y1


if __name__ == '__main__':
    myfirstwallet = Wallet("USD", "Artem")  # создание экземпляра класса
    print(Wallet.__doc__)   # строка с описанием класса
    print(myfirstwallet.__dict__)  # содержит набор локальных свойств (атрибутов) экземпляра myfirstwallet класса Wallet
    myfirstwallet.info()    # вызов метода
    myfirstwallet.usemoney = 20  # setter
    myfirstwallet[3] += 10  # __setitem__ (не имеет отношения к iadd)
    del myfirstwallet[0]  # __delitem__
    print(myfirstwallet[3])  # __getitem__
    print(myfirstwallet)  #  вернет __str__ или, если его нет - __repr__
    print(len(myfirstwallet))  # для len() нужно определить __len__
    print(abs(myfirstwallet))  # для abs() нужно определить __abs__
    #
    if myfirstwallet:           # проверка работы метода __bool__
        print(f' объект myfirstwallet возвращает True')
    else:
        print(f' объект myfirstwallet возвращает False')

    print(myfirstwallet.__class__)  # == print(type(myfirstwallet)) - узнать какому классу принадлежит экземпляр
    print(myfirstwallet.__class__.__name__)  # получить имя класса в str


    print(myfirstwallet + 10)  # == myfirstwallet.__add__(10), вернет результат метода __add__
    print(10 + myfirstwallet + 10)
    secondwallet = Wallet('USD', 'Misha')
    w3 = myfirstwallet + secondwallet
    w4 = w3 + myfirstwallet + secondwallet
    print(w4.attribute)
    w4 += 100
    print(w4.attribute)
    print(w4)
    print(myfirstwallet == secondwallet)
    print(myfirstwallet == -5)


    myfirstwallet.usemoney = -19  # property (setter)
    print(type(myfirstwallet.usemoney))  # <class 'float'>
    setattr(myfirstwallet, 'attrib', "value")   # обновить (создать новый) атрибут

    delattr(myfirstwallet, 'attrib')    # (= del myfirstwallet.attrib) удаляет атрибут, если такого нет, то ошибка
    print(hasattr(myfirstwallet, "attrib"))  # True, если у экземпляра (ИЛИ У ЕГО КЛАССА) есть такой атрибут
    print(getattr(myfirstwallet, 'attrib', 'There is no attribute'))  # возвращает значение атрибута или 3й аргумент

    fr = FRange(0, 2, 0.5)
    next(fr)
    for i in fr:
        print(i)

    print(f'Производная: {parabola(x=1)}')

    """Наследование"""
    print(issubclass(list, object))  # проверить, является ли первый класс дочерним от второго класса
    array = []
    print(isinstance(array, object))  # проверить, наследуется ли сущность от класса (экземпляр от его или родительского класса)

    s1 = Square(0, 3, 0, 3, "red")
    r1 = Rectangle(0, 3, 0, 4)
    print(s1.__dict__)
    print(r1.__dict__)  # {'attr': 50} тк остальные лок-ые св-ва записаны в __slots__ базового класса
    print(id(s1._Geom__y2))
    print(id(r1._Geom__y2))
    print(Geom.__dict__)  # нет атрибутов с именем y1
    r1.get_date()
    print(Rectangle.__mro__)  # Посмотреть в какой последовательности будут искаться объекты при обращении к ним экземпляром класса Rectangle

    """Полиморфизм - возможность работы с совершенно разными объектами единым образом"""
    g = Geom(1, 2, 4, 5)  # TypeError - попытка создания экземпляра абстрактного класса
    geom = [s1, r1]
    for i in geom:
        print(i.get_perimetr())  # единая обработка экземпляров разных классов за счет того, что классы имеют метод с одним названием

    """Обработка пользовательских исключений"""
    try:
        raise ExceptionPrintSendData("something went wrong")
    except ExceptionPrint:
        print("печать не прошла")

    """Custom context manager"""
    a = [10, 20, 30]
    b = [42, 12]
    try:
        with DefendList(a) as dl:
            for index, value in enumerate(dl):  # enumerate returns index and value of current item of iterable object
                dl[index] += b[index]
    except IndexError:
        print("Ошибка: длины листов не равны")
        print(f"Лист a: {a} не был изменен частично, тк мы работали с его копией")

    print(a)

    w = Women('root', '12345')
    print(w.__dict__)
    print(w.meta.__dict__)

    """Динамическое создание классов"""
    def get_perimetr(self):
        return 2 * (self._x2 - self.x1 + self._Geom__y2 - self.y1)

    Trapezoid = type('Trapezoid', (Geom, TimeRecord), {'attr': 100, 'get_perimetr': get_perimetr, 'get_attr': lambda self: self.attr})
                     # название; наследуемые классы; словарь свойств класса
    t1 = Trapezoid(0, 3, 0, 2)
    print(t1.get_perimetr())
    t1.get_date()
    print(t1.get_attr())

    """Метаклассы"""
    p1 = Point(1, 0)
    print(p1.attribute2)
    print(p1.get_coords())
