import random
from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any
from random import randint

'''
from pprint import pprint

class Thing:

    def __init__(self, name, weight, price=0, dims = []):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f'{self.__dict__}'

@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.price == other.price

th = Thing('name', 15, 1500)
print(th)

td = ThingData('name2', 12, 2.5)
td.dims.append(10)
print(td)
td2 = ThingData('name2', 12, 2.5)
print(td2)
'''


'''
class Vector3D:

    def __init__(self, x, y, z, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.lenght = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if calc_len else 0


@dataclass(frozen=True)
class VectorData:
    x: int
    y: int = field(compare=False)
    z: int = field(default=0)
    calc_len: InitVar[bool] = True
    lenght: float = field(init=False, default=0)
    pi: float = field(init=False, default=3.14)

    def __post__init__(self, calc_len):
        if calc_len:
            self.lenght = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        self.pi = 3.14

v = Vector3D(1, 2, 3)
print(v)
vd = VectorData(1, 4)
vd2 = VectorData(1, 4)
print(vd == vd2)
print(vd)
'''

'''
@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print('Goods')
        Goods.current_uid += 1
        self.uid = Goods.current_uid

class GoodMeassureFactory:

    @staticmethod
    def get_init_meassure():
        return [0, 0, 0]

@dataclass
class Book(Goods):
    title: str
    author: str
    price: int
    weight: float
    meassure: list = field(default_factory=GoodMeassureFactory.get_init_meassure)

    def __post_init__(self):
        super().__post_init__()
        print('Book')



g = Goods(1200, 2.5)
print(g)
g1 = Goods(1200, 2.5)
print(g1)
b = Book(2000, 2.5, 'dfgdfg', 'sdfsdf')
for i in range(0, len(b.meassure)):
    b.meassure[i] = random.randint(10, 20)
print(b)
'''

'''
class Car:

    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed

@dataclass
class CarD:
    model: str
    max_speed: int | float
    price: int = field(default=0)

    def get_max_speed(self):
        return self.max_speed

    def get_price(self):
        return self.price


CarData = make_dataclass('CarData', [('model', str), 'max_speed', ('price', int, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed,
                                    'get_price': lambda  self: self.price})

cd = CarData('Lada Granta', 120, 600000)
print(cd.get_max_speed())
print(cd.get_price())
'''


