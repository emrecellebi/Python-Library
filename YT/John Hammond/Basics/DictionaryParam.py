#!/usr/bin/env python

class Base:
#{
    def __init__(self, **book):
    #{
        print(book);
        for key, value in book.items():
        #{
            print(str(key) + " " + str(value));
        #}
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base(key_1 = 1, key_2 = 2);
#}