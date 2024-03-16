class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

name = input("Enter name of man: ")
age = input("Enter age of man: ")

man = Person(name, age)
print("\nDetails of person: ")
print("Name of man: " + man.name)
print("Age of man: " + man.age)
