#!/usr/bin/env python

from subprocess import *;

class Base:
#{
    def __init__(self):
    #{
        baby = Popen(["ls","-l"]);
        print("Pid: " + str(baby.pid));
        print("Return Code: " + str(baby.returncode));
        print("Poll: " + str(baby.poll()));
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}