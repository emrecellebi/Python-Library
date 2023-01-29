#!/usr/bin/env python

from PIL import *;

def main():
#{
    filename = "img/3.jpg";
    
    image = Image.open(filename);
    
    width, height = image.size;
    
    print(image.getcolors(width * height));
    
    del image;
#}

if(__name__ == "__main__"):
#{
    main();
#}