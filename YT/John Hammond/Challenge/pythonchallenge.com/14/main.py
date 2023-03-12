#!/usr/bin/env python

from PIL import Image;

def main():
#{
    img = Image.new('RGB', (100, 100));
    wire = Image.open('wire.png', 'r');
    
    xmin, xmax = 0, 99;
    ymin, ymax = 0, 99;
    
    pos = [0, 0];
    place = 0;
    
    output = True;
    
    while not (xmax - 1 == xmin or ymax - 1 == ymin):
    #{
        for x in range(xmin, xmax + 1):
        #{
            if output: print("X: ", pos[0], " Y: ", pos[1]);
            pos[0] = x;
            place += 1;
            img.putpixel(pos, wire.getpixel((place, 0)));
        #}
        ymin += 1;
        
        for y in range(ymin, ymax + 1):
        #{
            if output: print("X: ", pos[0], " Y: ", pos[1]);
            pos[1] = y;
            place += 1;
            img.putpixel(pos, wire.getpixel((place, 0)));
        #}
        xmax -= 1;
        
        for x in range(xmax, xmin - 1, -1):
        #{
            if output: print("X: ", pos[0], " Y: ", pos[1]);
            pos[0] = x;
            place += 1;
            img.putpixel(pos, wire.getpixel((place, 0)));
        #}
        ymax -= 1;
        
        for y in range(ymax, ymin - 1, -1):
        #{
            if output: print("X: ", pos[0], " Y: ", pos[1]);
            pos[1] = y;
            place += 1;
            img.putpixel(pos, wire.getpixel((place, 0)));
        #}
        xmin += 1;
    #}
    img.save("spiral.png");
#}

if(__name__ == "__main__"):
#{
    main();
#}

