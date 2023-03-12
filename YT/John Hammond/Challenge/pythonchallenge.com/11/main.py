#!/usr/bin/env python

from PIL import Image;

def main():
#{
    image = Image.open("cave.jpg");
    size = width, height = image.size;
    
    new_image = Image.new("RGB", size);
    
    for x in range(0, width, 2):
    #{
        for y in range(0, height, 2):
        #{
            even_color = image.getpixel((x, y));
            odd_color = image.getpixel((x + 1, y + 1));
            
            new_image.putpixel((x, y), even_color);
            new_image.putpixel((x + 1, y + 1), odd_color);
        #}
    #}
    
    new_image.save("image.png");
#}

if(__name__ == "__main__"):
#{
    main();
#}

