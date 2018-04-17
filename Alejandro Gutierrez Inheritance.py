class Vechicle(object):
    def __int__(self, source, material, seat, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat_location = seat
        self.max_speed = speed
        self.passengers = passengers


    def move(self):
        print("You move forward.")

    def change_direction(self):
        print("You changed direction.")


class Car(Vechicle):
    def __int__(self,  material, seat, speed, passengers, windows):
        super(Car, self).__int__('engine',  material, seat, speed, passengers)
        self.windows = windows


    def roll_down_windows(self):
        print("You roll the windows down")

    def turn_on(self):
        print("You turn the key and the engine starts.")


test_car = Car('Aluminum', 'Drver side', 140, 2, True)
test_car.change_direction()


class KeylessCar(Car):
    def __int__(self, material, seat, speed, passengers, windows):
        super(KeylessCar, self).__int__(material, seat, speed, passengers, windows)

    def turn_on(self):
        print("You push the button and the car turns on")


cool_car = KeylessCar('Aluminum', 'Drver side', 140, 2, True)
cool_car.turn_on()


class Tesla(Car):
    def __int__(self, material, seat, speed, passengers, windows):
        super(Tesla, self).__int__(material, seat, speed, passengers, windows)


    def fly(self):
        print("You launch the car into low earth orbit.")


    def turn_on(self):
        Car.turn_on(self)