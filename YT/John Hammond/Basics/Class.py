#!/usr/bin/env python

class Person:
#{
    def __init__(self):             # Constructures
    #{
        self.name = "Test"
    #}
    
    def __init__(self, name = "", age = 0):  # Constructures Patameters
    #{
        self.name = name
        self.age = age
    #}
    
    def say_hello(self):
    #{
        print("Name: " + self.name + " Age: " + str(self.age))
    #}
    
    def __del__(self):              # Deconstructures
    #{
        print(self.name + " has die.")
    #}
#}

if(__name__ == "__main__"):
#{
    per = Person()
    per2 = Person("Melek", 22)

    per.say_hello();
    per2.say_hello();
#}