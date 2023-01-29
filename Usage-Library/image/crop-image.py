#!/usr/bin/env python

from PIL import Image;

def main():
#{
    filename_one = "img/3.jpg";
    filename_two = "img/4.jpg";
    
    image_one = Image.open(filename_one);
    image_two = Image.open(filename_two);
    
    image_one.crop(250, 250, 100, 100).show();
    
    del image_one, image_two;
#}

if(__name__ == "__main__"):
#{
    main();
#}