#1.
class Animal :
    def move(self):
        print("동물이 움직입니다")

class Dog:
    def __init__(self):
        self.animal = Animal ()

    def move(self):
        self.animal . move()
        print("개가달립니다")

dog = Dog()
dog.move()


#2. 
class Person :
    def speak(self):
        print("사람이 말을 합니다")

class Student:
    def __init__(self) :
        self.person = Person()

    def study(self) :
        self.person.speak()
        print("학생이공부합니다")

stu = Student()
stu.study()


#3.
class Vehicle :
    def drive(self):
        print("차량이이동중입니다")

class Car :
    def __init__(self):
        self.vehicle = Vehicle()

    def drive(self) :
        self.vehicle.drive()
        print("자동차가 도로를 달립니다")

car = Car ()
car.drive()