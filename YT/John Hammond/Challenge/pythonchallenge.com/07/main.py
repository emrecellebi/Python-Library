#!/usr/bin/env python

from PIL import Image;

def main():
#{
    oxygen = Image.open("oxygen.png");
    size = width, height = 629, 95;
    
    y = 48;
    end = 607;
    step = 7;
    
    new_string = "";
    for x in range(0, end, step):
    #{
        new_string += chr(oxygen.getpixel((x, y))[0]);
    #}
    print(new_string);
    
    new_string = "";
    
    to_change = [105, 110, 116, 101, 103, 114, 105, 116, 121];
    for item in to_change:
    #{
        new_string += chr(item);
    #}
    
    print(new_string);
#}

if(__name__ == "__main__"):
#{
    main();
#}

