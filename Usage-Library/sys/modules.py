#!/usr/bin/env python

import sys

class Base:
#{
    def __init__(self):
    #{
        print("Modules: " + str(sys.modules))
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}