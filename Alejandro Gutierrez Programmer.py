class Person(object):
    def __int__(self, name, age):
        self.name = name
        self.age = age


    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __int__(self, name, age, shirt):
        super(Employee, self).__int__(name, age, shirt)


    def check_in(self):
        print("%s checked in to work and turned on their computer." % self.name)


class Programmer(Employee):
    def __int__(self, name, age, shirt, glasses):
        super(Programmer, self).__int__(name, age, shirt, glasses)


    def coding(self):
        print("%s they started coding their project." % self.name)


Programmer("Bob", 29, 'black shirt', 'green glasses')