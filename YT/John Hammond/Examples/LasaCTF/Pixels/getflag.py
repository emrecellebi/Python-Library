#!/usr/bin/env python

from PIL import Image, ImageChops;
import subprocess;

def main():
#{
    white = (255, 255, 255);
    black = (0, 0, 0);
    
    image1 = Image.open('QR1.png');
    image2 = Image.open('QR2.png');
    data1 = image1.load();
    data2 = image2.load();
    
    size = width, height = image1.size;
    
    qr = Image.new('RGBA', size, white);
    new_data = qr.load();
    
    save_name = 'found_QR.png';
    
    for y in range(height):
    #{
        for x in range(width):
        #{
            if(data1[x, y] == data2[x, y]):
            #{
                continue;
            #}
            else:
            #{
                qr[x, y] = black;
            #}
        #}
    #}
    
    # qr.show();
    qr.save(save_name);
    
    print(subprocess.check_output(['zbarimg', save_name], stderr=PIPE).split()[-1]);
    
    qr.close();
    
    image1.close();
    image2.close();
#}

if(__name__ == "__main__"):
#{
    main();
#}