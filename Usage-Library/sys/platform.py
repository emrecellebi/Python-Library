#!/usr/bin/env python

import sys

class Base:
#{
    def __init__(self):
    #{
        print("Platform: " + sys.platform)
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}