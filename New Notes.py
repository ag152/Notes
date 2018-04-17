# def hello_world():
#     print("Hello World")
#
#
# hello_world()
#
#
# def square_it(number):
#     return number**2
#
#
# print(square_it(3))
#
#
# def tip_calc(bill):
#     tax_amt = bill * 0.18
#     total_bill = bill + tax_amt
#     return total_bill
#
#
# print(tip_calc(15))
#
#
# def distance_calc(x1, y1, x2, y2):
#     inside = (x1 - x2)**2 + (y1 - y2)**2
#     answer = inside ** 0.5
#     return answer
#
#
# print(distance_calc(0, 0, 3, 4))
#
# def pythagorean(a, b):
#     c = a**2 + b**2
#     return c
#
#
# print(pythagorean(6, 7))
# Definig a class


class Cheeseburger(object):
    def __init__(self,patty_type, cheese):
        self.patty = patty_type
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("You cut the cheeseburger")

    def eat(self):
        print("You ate the cheeseburger")
        self.eaten = True


burger1 = Cheeseburger("beef", "Havarti")
burger2 = Cheeseburger("Bacon", "Swiss")
print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)

class Car(object):
    def __init__(self, color, num_of_doors, hp, name):
        self.color = color
        self.door = num_of_doors
        self.running = False
        self.HP = hp
        self.name = name
        self. passengers = 0
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("Nothing Happens")
        else:
            self.running = True
            print("The car starts")

    def move_forward(self):
        if self.running:
            print("You move forward.")
        else:
            print("Nothing Happens")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You turn the car off")
        else:
            print("The car is already off.")

    def go_for_drive(self, passengers):
        print("%d passengers get in." % passengers)
        self.passengers = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out." % passengers)
        self.passengers = 0


my_car = Car("Black", 4, 10000, "T pose")
my_car.go_for_drive(2)
