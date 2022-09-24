#!/usr/bin/env python

class Mother:
#{
    def __init__(self):
    #{
        self.first_name = "Alice";
        self.last_name = "Hawkings";
        self.full_name = self.first_name + " " + self.last_name;
    #}
    
    def say_hello(self):
    #{
        print(self.full_name + " says hello!");
    #}
        
    def set_first_name(self, name):
    #{
        self.first_name = name;
    #}
#}

class Child(Mother):                    # Kalıtım Multiple Kalıtım ise virgül ile ayırlarak gider örn: class Child(Mother, Mother2):
#{
    def get_married(self, soulmate):
    #{
        self.last_name = soulmate.last_name;
    #}
#}
    
class Soulmate:
#{
    def __init__(self, first_name, last_name):
    #{
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name;
    #}
    
    def say_hello(self):
    #{
        print(self.full_name + " says hello!");
    #}
#}
    
if(__name__ == "__main__"):
#{
    alice = Mother();
    alice.say_hello();

    bob = Child();
    bob.set_first_name("Bob");
    bob.say_hello();

    allie = Soulmate("Allie", "Deering");
    allie.say_hello();

    bob.get_married(allie);
    bob.say_hello();
#}