#!/usr/bin/env python

import getpass;

class Base:
#{
    def __init__(self):
    #{
        # print("Get Pass: " + getpass.getpass());
        print("Get Pass: " + getpass.getpass("emre@kali: "));
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}