#!/usr/bin/env python

import string

def main():
#{
    caption = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.";
    
    new_string = "";
    # for letter in caption:            # Yukarıdaki datayı çecirmek için aç
    for letter in string.ascii_lowercase:
    #{
        found_position = string.ascii_lowercase.find(letter);
        
        if(found_position == -1):
        #{
            new_string += letter;
            continue;
        #}
        index = found_position + 2;
        
        if(index >= 26):
        #{
            index -= 26;
        #}
        
        new_string += string.ascii_lowercase[index];
    #}
    
    # print(new_string);
    
    # table = string.maketrans(string.ascii_lowercase, "cdefghijklmnopqrstuvwxyzab");
    print(caption.translate(None, "cdefghijklmnopqrstuvwxyzab"));
#}

if(__name__ == "__main__"):
#{
    main();
#}