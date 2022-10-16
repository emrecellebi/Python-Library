#!/usr/bin/env python

import sys

class Base:
#{
    def __init__(self):
    #{
        print("Version: " + str(sys.getwindowsversion()))
        print("Major: " + str(sys.getwindowsversion().major))
        print("Minor: " + str(sys.getwindowsversion().minor))
        print("Build: " + str(sys.getwindowsversion().build))
        print("Platform: " + str(sys.getwindowsversion().platform))
        print("Service Pack: " + str(sys.getwindowsversion().service_pack))
        
        print("Major: " + str(sys.getwindowsversion()[0]))
        print("Minor: " + str(sys.getwindowsversion()[1]))
        print("Build: " + str(sys.getwindowsversion()[2]))
        print("Platform: " + str(sys.getwindowsversion()[3]))
        print("Service Pack: " + str(sys.getwindowsversion()[4]))
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}