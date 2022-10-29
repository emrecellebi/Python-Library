#!/usr/bin/env python

import getpass;

class Base:
#{
    def __init__(self):
    #{
        print("Get User: " + getpass.getuser());
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}