#!/usr/bin/env python

import pyfiglet;

class Base:
#{
    def __init__(self):
    #{
        file = open("message.txt", "a");
        for font in pyfiglet.FigletFont.getFonts():
        #{
            text = pyfiglet.Figlet(font).renderText("Ceren");
            file.write(font + "\n" + text + "\n\n");
        #}
        file.close();
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}