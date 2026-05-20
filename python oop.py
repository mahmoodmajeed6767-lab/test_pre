# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass 

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc = Account("1234","7890")
# print(acc.acc_no)
# print(acc.reset_pass())

# class Person:
#     __name = "anonymous"
#     def __hello(self):
#         print("hello person!")
    
#     def welcome(self):
#         self.__hello()
# p1 = Person()
# print(p1.welcome())

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod 
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):

#     def __init__(self,name):
#         self.name = name
# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")
# print(car1.color)

# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Object banana
d = Dog()

d.eat()   # Parent ka method
d.bark()  # Child ka method
