class Animal:
    def __init__(self, age):
        self.age = age
        self.live = True
        self.beak = False

    def speak(self):
        print('Sone animal sound')

    def attack(self):
        print("Be careful, i'm attacking you 0_0")

    def move(self,dx, dy, dz):
        self._cords = (self._cords[0] + dx, self._cords[1] + dy, self._cords[2] + dz)

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

class Bird(Animal):
    def __init__(self, age):
        super().__init__(age)
        self.beak = True

    def lay_eggs(self):
        print(f'Here age(is) {self._eggs_count} eggs for you')

    def speak(self):
        print('Some bird sound')


class AqiaticAnimal(Animal):
    _DEAGEE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords = (self._cords[0], self._cords[1], self._cords[2] - abs(dz))
        self.speed /= 2

    def move(self,dx, dy, dz):
        super().move(dx, dy, dz)
        self.dive_in(dz)


class PoisonoousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    def attack(self):
        print("Be careful, i'm a poisonous animal!")


class Duskbill(Bird, AqiaticAnimal, PoisonoousAnimal):
    def __init__(self, age):
        super().__init__(age)
        self._cords = (10, 20, 30)
        self._eggs_count = 3
        self.speed = 5
        self.sound = 'Click-click-click'

    def speak(self):
        print(self.sound)

    def lay_eggs(self):
        super().lay_eggs()

db = Duskbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2 ,3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()