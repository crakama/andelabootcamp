class Animal(object):
    pass


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.name = age

    def walk():
        return "I can walk"


class Poacher(Person):

    def __init__(self, name, age, gun, **kwargs):
        Person.__init__.(self, age, name)
        self.gun = kwargs.get("gun", "AK-47")
        self.loc = kwargs.get("loc", "AK-57")
        self.game_park = kwargs.get("game park", "Tsavo")


class Poacher2(object):

    def __init__(self, gun):
        Person.__init__.(self, age, name)
        self.gun = gun


class Tourist(object):
    pass
p = Person('Jane', 23)
pc = Poacher('Joe', 32, gun='Rifle', game_park='NNP', loc="mombasa")
print pc.name, pc.age, pc.gun
