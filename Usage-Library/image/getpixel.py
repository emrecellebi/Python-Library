#!/usr/bin/env python

from PIL import Image;

def main():
#{
    filename = "img/5.jpg";
    image = Image.open(filename);
    size = width, height = image.size;
    
    coordinate = x, y = 180, 69;
    print(image.getpixel(coordinate));
    
    del image;
#}

if(__name__ == "__main__"):
#{
    main();
#}