
class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # repr правильный, должен позволить простым копированием в код воссоздать объект
    #  используем !r  и вместо Car служебное __class__.__name__
    def __repr__(self):
        # return f'Car({self.color!r}, {self.mileage!r})'
        return f'{__class__.__name__}({self.color!r}, {self.mileage!r})'

    def __str__(self):
        # return f'{self.color} автомобиль'
        return '__str__ для объекта Car'

    # def __repr__(self):
    #     return '__repr__ для объекта Car'


my_car = Car('красный', 37821)

print(repr(my_car))
print(str(my_car))
print(my_car)
print([my_car])

import datetime
today = datetime.date.today()

print(str(today))
print(repr(today))

d = datetime.date(2022, 8, 31)
print(repr(d))

# __repr__ для объекта Car
# __str__ для объекта Car
# __str__ для объекта Car
# [__repr__ для объекта Car]
# 2022-08-31
# datetime.date(2022, 8, 31)
# datetime.date(2022, 8, 31)


# Работа над ошибками
# Создаем базовый класс ошибок модуля
class BaseValidationError(ValueError):
    pass

# Далее в названиях подклассов описываем причину ошибок
class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
     pass

def handle_validation_error(err):
    return print(f'Ошибка {err.__class__.__name__}: {err}')

# описываем функцию с какой-то одной причиной ошибки
def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

# далее в коде программы при вызове функции достаточно вызвать
# базовое исключение, которое само определит тип исключения -
# функция handle_validation_error придумана мной - не изкниги)))

name = 'Джейн'

try:
    validate(name)
except BaseValidationError as err:
    handle_validation_error(err)

# Абстрактные классы ABC
# нужны в качестве проектируемого решения, други программисты не смогут порождать дочерние классы без
# описания заложенных в них процедур
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    # Мы снова забыли объявить bar()...

# c = Concrete() # Приведет к TypeError: "Can't instantiate abstract class Concrete with abstract methods bar"

# Именованные кортежи - могут быть заменой классов
# является эффективной с точки зрения потребляемой оперативной памяти краткой формой для опрделения
# неизменяющегося класса вручную.
from collections import namedtuple

Car = namedtuple('Авто', [
    'цвет',
    'пробег',
])

my_car = Car('синий', 24522.5)

print(my_car)
print(my_car.цвет)
print(my_car.пробег)

print(my_car[0])

color, mileage = my_car
print(color, mileage)
print(*my_car)

# НО тк это НЕИЗМЕНЯЕМЫЙ тип код ниже вернет ошибку
# my_car.цвет = 'красный'
# также можно наследовать
ElectricCar = namedtuple('ЭлектрическоеАвто', Car._fields + ('заряд',))
print(ElectricCar('красный', 1234, 45.0))
# также есть _asdict(). Он возвращает содержимое именованного кортежа в виде словаря
# _replace() . Он создает (мелкую) копию кортежа и позволяет вам выборочно заменять некоторые его поля
# make() может использоваться для создания новых экземпляров класса namedtuple из (итерируемой) последовательности:

# Переменные класс и переменные экземпляра
# модификация переменной класса одновременно затрагивает все экземпляры объекта.
# модификация переменной экземпляра одновременно затрагивает только один экземпляр объекта.

class Dog:
    num_legs = 4 # <- Переменная класса

    def __init__(self, name):
        self.name = name # <- Переменная экземпляра

jack = Dog('Джек')
jill = Dog('Джилл')

print(jack.num_legs, jill.num_legs)
# (4, 4)
print(Dog.num_legs)
# 4

# ЭФФЕКТ: при увеличении num_legs через экземпляр класса приведет к созданию дополнительной переменной экземпляра
# которая будет перекрывать переменную класса
Dog.num_legs = 4
jack.num_legs = 6
print(jack.num_legs, jill.num_legs, Dog.num_legs)
# (6, 4, 4))
# вот как можно увидеть эффект:
print(jack.num_legs, jack.__class__.num_legs)

# другой пример, чтобы создать счетчик созданных инстансов лучше елать так:

class CountedObject:
     num_instances = 0
     def __init__(self):
         self.__class__.num_instances += 1


# Методы экземпляра, методы класса и статические методы
class MyClass:
    def method(self):
        """Методы экземпляра могут не только модифицировать состояние объекта, но и получать доступ к самому классу
        через атрибут self.__class__. Это означает, что методы экземпляра также могут модифицировать состояние класса."""
        return 'вызван метод экземпляра', self

    @classmethod
    def classmethod(cls):
        """Могут модифицировать состояние класса, которое применимо во всех экземплярах класса."""
        return 'вызван метод класса', cls

    @staticmethod
    def staticmethod():
        """Может модифицировать состояние объекта или состояние класса,
        прежде всего, являются средством организации пространства имен ваших методов"""
        return 'вызван статический метод'

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
# ('вызван метод экземпляра', <__main__.MyClass object at 0x10e2ca6d0>)
# ('вызван метод класса', <class '__main__.MyClass'>)
# вызван статический метод

# раскроем понятия на примерах
import math
class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return (f'Pizza({self.radius!r},'
                f'{self.ingredients!r})')

    # Фабричные методы
    # фабричные функции можно использовать для создания новых объектов Pizza,
    # которые сконфигурированы именно так, как мы хотим
    @classmethod
    def margherita(cls):
        return cls(5, ['моцарелла', 'помидоры'])

    @classmethod
    def prosciutto(cls):
        return cls(6, ['моцарелла', 'помидоры', 'ветчина'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi



print(Pizza(4, ['сыр', 'помидоры']))
# использование фабричных методов
piz_margo = Pizza.margherita()
print(piz_margo)
print(Pizza.prosciutto())
# Pizza(['сыр', 'помидоры'])
# Pizza(['моцарелла', 'помидоры'])
# проверим статик методы
p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
print(Pizza.circle_area(4))
