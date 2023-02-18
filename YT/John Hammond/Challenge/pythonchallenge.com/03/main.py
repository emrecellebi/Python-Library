#!/usr/bin/env python

from urllib import *;
from string import *;

def main():
#{
    page = urlopen("http://www.pythonchallenge.com/pc/def/equality.html");
    
    contents = page.read();
    
    page.close();
    
    mess = contents.split("<!--\n")[-1][:-4];
    
    mess_length = len(mess);
    counter = 0;
    
    while(counter < mess_length):
    #{
        character = mess[counter];
        
        if character in ascii_lowercase:
        #{
            letter_left_1 = mess[counter - 1];
            if letter_left_1 in ascii_uppercase:
            #{
                letter_left_2 = mess[counter - 2];
                if letter_left_2 in ascii_uppercase:
                #{
                    letter_left_3 = mess[counter - 3];
                    if letter_left_3 in ascii_uppercase:
                    #{
                        letter_left_4 = mess[counter - 4];
                        if letter_left_4 in ascii_lowercase:
                        #{
                            letter_right_1 = mess[counter + 1];
                            if letter_right_1 in ascii_uppercase:
                            #{
                                letter_right_2 = mess[counter + 2];
                                if letter_right_2 in ascii_uppercase:
                                #{
                                    letter_right_3 = mess[counter + 3];
                                    if letter_right_3 in ascii_uppercase:
                                    #{
                                        letter_right_4 = mess[counter + 4];
                                        if letter_right_4 in ascii_lowercase:
                                        #{
                                            # print(letter_left_4 + letter_left_3 + letter_left_2 + letter_left_1 + character + letter_right_1 + letter_right_2 + letter_right_3 + letter_right_4);
                                            print(character);
                                        #}
                                    #}
                                #}
                            #}
                        #}
                    #}
                #}
            #}
        #}
        counter += 1;
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}