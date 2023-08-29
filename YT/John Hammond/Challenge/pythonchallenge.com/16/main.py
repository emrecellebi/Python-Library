#!/usr/bin/env python

from PIL import Image, ImageChops;
import subprocess;

def main():
#{
    image = Image.open("mozart.gif");
    size = width, height = image.size
    
    print(image.info);
    
    offset_indicator = "\xc3";
    frame = 0;
    for y in range(height):
    #{
        crop_box = 0, y, width, y + 1
        row = image.crop(crop_box);
        row_string = row.tostring();
        offset = row_string.index(offset_indicator) - 1;
        row = ImageChops.offset(row, -offset);
        image.paste(row, crop_box);
        image.save("frames" + str(frame)zfill(3) + ".png");
        frame += 1
    #}
    print(subprocess.check_output("conver -delay 1 -loop 0 frames*.png animation.gif").split());
    image.show();
    image.close();
#}

if(__name__ == "__main__"):
#{
    main();
#}