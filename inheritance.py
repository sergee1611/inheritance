class Car:
    price = 1000000

    def horse_powers(self, hor_pow):
        print(f'Мощность: {hor_pow} л.с')


class Nissan(Car):
    price = 1100000


class Kia(Car):
    price = 900000


nissan = Nissan()
print(nissan.price)
nissan.horse_powers(150)
kia = Kia()
print(kia.price)
kia.horse_powers(110)
