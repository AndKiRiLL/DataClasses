from dataclasses import dataclass, field

# Класс «Воздушный Замок» (AirCastle)
'''
@dataclass
class AirCastle:
    height: int | float
    count_clouds: int
    color: str
    alpha: int
    visible: int = field(init=False, default=0)

    def __post_init__(self):
        self.visible = self.height // self.alpha * self.count_clouds

    def change_height(self, value):
        if value != 0:
            self.height = value

    def add_clouds(self, value):
        self.count_clouds += value
        self.height += value // 5

    def __str__(self):
        return f'The AirCastle at an altitude of {self.height} meters is {self.color} with {self.count_clouds} clouds'

    def __lt__(self, other):
        return (self.count_clouds, self.height, self.color) < (other.count_clouds, other.height, other.color)

    def __le__(self, other):
        return (self.count_clouds, self.height, self.color) <= (other.count_clouds, other.height, other.color)

    def __eq__(self, other):
        return (self.count_clouds, self.height, self.color) == (other.count_clouds, other.height, other.color)

    def __ne__(self, other):
        return (self.count_clouds, self.height, self.color) != (other.count_clouds, other.height, other.color)

    def __gt__(self, other):
        return (self.count_clouds, self.height, self.color) > (other.count_clouds, other.height, other.color)

    def __ge__(self, other):
        return (self.count_clouds, self.height, self.color) >= (other.count_clouds, other.height, other.color)

ac = AirCastle(15, 5, 'White', 3)
ac2 = AirCastle(20, 10, 'Gray', 5)
print(str(ac))
print(f'Visible: {ac.visible}')
ac.add_clouds(5)
print(str(ac))

print()
print(ac < ac2)
print(ac <= ac2)
print(ac == ac2)
print(ac != ac2)
print(ac > ac2)
print(ac >= ac2)
'''


# Класс Добрый Ифрит (GoodIfrit)
'''
from copy import deepcopy

@dataclass
class GoodIfrit:
    height: int
    name: str
    kindness: int

    def change_goodness(self, value):
        if value < 0:
            self.kindness += 0
        else:
            self.kindness += value

    def __add__(self, other):
        new = deepcopy(self)
        new.height += other
        return new

    def __call__(self, arg):
        return arg * self.kindness // self.height

    def __str__(self):
        return f'Good Ifrit {self.name}, heigh {self.height}, goodness {self.kindness}'

    def __lt__(self, other):
        return (self.kindness, self.height, self.name) < (other.kindness, other.height, other.name)

    def __le__(self, other):
        return (self.kindness, self.height, self.name) <= (other.kindness, other.height, other.name)

    def __eq__(self, other):
        return (self.kindness, self.height, self.name) == (other.kindness, other.height, other.name)

    def __ne__(self, other):
        return (self.kindness, self.height, self.name) != (other.kindness, other.height, other.name)

    def __gt__(self, other):
        return (self.kindness, self.height, self.name) > (other.kindness, other.height, other.name)

    def __ge__(self, other):
        return (self.kindness, self.height, self.name) >= (other.kindness, other.height, other.name)

# Пример 1
# gi = GoodIfrit(80, 'Hazrul', 3)
# gi.change_goodness(4)
# print(gi)
#
# gi1 = gi + 15
# print(gi1)
#
# print(gi(31))

# Пример 2

gi = GoodIfrit(80, 'Hazrul', 3)
gi1 = GoodIfrit(80, 'Dalziel', 1)
print(gi < gi1)
gi1.change_goodness(2)
print(gi > gi1)
print(gi, gi1, sep='\n')
'''

# Класс «Волшебник» (Wizard)

@dataclass
class Wizard:
    name: str
    rating: int
    visible_age: int


    def change_rating(self, value):
        rat_start = self.rating
        self.rating += value

        if rat_start < self.rating:
            self.visible_age -= abs(value) // 10

            if self.rating > 100:
                self.rating = 100

            if self.visible_age < 18:
                self.visible_age = 18

        if rat_start > self.rating:
            self.visible_age += abs(value) // 10

            if self.rating < 1:
                self.rating = 1

    def __iadd__(self, string):
        self.rating += len(string)
        self.visible_age -= len(string) // 10

        if self.rating > 100:
            self.rating = 100

        if self.visible_age < 18:
            self.visible_age = 18
        return self

    def __call__(self, arg):
        return (arg - self.visible_age) * self.rating

    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks {self.visible_age} year old'

    def __lt__(self, other):
        return (self.rating, self.visible_age, self.name) < (other.rating, other.visible_age, other.name)

    def __le__(self, other):
        return (self.rating, self.visible_age, self.name) <= (other.rating, other.visible_age, other.name)

    def __eq__(self, other):
        return (self.rating, self.visible_age, self.name) == (other.rating, other.visible_age, other.name)

    def __ne__(self, other):
        return (self.rating, self.visible_age, self.name) != (other.rating, other.visible_age, other.name)

    def __gt__(self, other):
        return (self.rating, self.visible_age, self.name) > (other.rating, other.visible_age, other.name)

    def __ge__(self, other):
        return (self.rating, self.visible_age, self.name) >= (other.rating, other.visible_age, other.name)


w = Wizard('Gendalf', 50, 60)
w2 = Wizard('Gendalf', 75, 30)
w.change_rating(60)
print(w)
w.change_rating(-15)
print(w)
w += '1234567897896789686678'
print(w)
print(w(3))

print()
print(w < w2)
print(w <= w2)
print(w == w2)
print(w != w2)
print(w > w2)
print(w >= w2)

