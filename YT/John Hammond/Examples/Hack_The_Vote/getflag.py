#!/usr/bin/env python

from PIL import Image;

def main():
#{
    image = Image.open("warp_speed.jpg");
    
    for i in range(32):
    #{
        region = image.crop((0, 8 * i, 1000, 8 * (i + 1)));
        image.paste(region, (-(8 * i), 8 * i, 1000 - (8 * i), 8 * (i + 1)));
    #}
    
    image2 = Image.new('RGBA', (500, 500));
    
    first_half = True;
    
    i = 0;
    Q = 0;
    
    while(i < 64):
    #{
        if first_half:
        #{
            region = image.crop((0, 8 * i, 500, 8 * (i + 1)));
        #}
        else:
        #{
            region = image.crop((500, 8 * i, 1000, 8 * (i + 1)));
            i += 1;
        #}
        
        image2.paste(region, ((0, 8 * Q, 500, 8 * (Q + 1))));
        Q += 1;
        
        first_half = not first_half;
    #}
    
    image2.show();
    image2.save("winner.jpg");
#}

if(__name__ == "__main__"):
#{
    main();
#}