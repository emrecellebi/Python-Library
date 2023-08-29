#!/usr/bin/env python2

# from PIL import Image, ImageChops;
import difflib;

def main():
#{
    # image = Image.open("balloons.jpg");
    # size = width, height = image.size;
    
    # image1 = 0, 0, width / 2, height;
    # image2 = width / 2, 0, width, height;
    
    # image1 = image.crop(image1);
    # image2 = image.crop(image2);
    
    # ImageChops.difference(image1, image2).show();
    
    filename = "delta.txt";
    handle = open(filename);
    lines = handle.readlines();
    handle.close();
    
    sequence1 = [];
    sequence2 = [];
    for line in lines:
    #{
        sequence1.append(line[:55].strip());
        sequence2.append(line[55:].strip());
    #}
    differ = difflib.Differ();
    comparison = list(differ.compare(sequence1, sequence2));
    print(comparison);
    
    sequence1_image = open('sequence1_image.png', 'wb');
    sequence2_image = open('sequence2_image.png', 'wb');
    both_image = open('both_image.png', 'wb');
    
    for each_result in comparison:
    #{
        bytes_ = [chr(int(b, 16)) for b in each_result[2:].split()];
        
        if each_result.startswith('-'):
        #{
            for byte in bytes_:
            #{
                sequence1_image.write(byte);
            #}
        #}
        
        if each_result.startswith('+'):
        #{
            for byte in bytes_:
            #{
                sequence2_image.write(byte);
            #}
        #}
        
        if each_result.startswith(' '):
        #{
            for byte in bytes_:
            #{
                both_image.write(byte);
            #}
        #}
    #}
    
    sequence1_image.close();
    sequence2_image.close();
    both_image.close();
#}

if(__name__ == "__main__"):
#{
    main();
#}