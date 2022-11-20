#!/usr/bin/env python

import urllib;

class Base:
#{
    def __init__(self):
    #{
        modified = urllib.quote("#<>HELP!");
        print(modified);
        print(urllib.unquote(modified));
       
        modified = self.quote("#<>HELP!");
        print(modified);
        print(self.unquote(modified));
    #}
    
    def quote(self, string, safe = '/'):
    #{
        escape_sequence = '  %20 ! %21 $ %24 & %26 ` %60 : %3A < %3C > %3E [ %5B ] %5D { %7B } %7D " %22 + %2B # %23 @ %40 / %2F ; %3B = %3D ? %3F \ %5C ^ %5E | %7C ~ %7E \' %27 , %2C'
        percent_sign = ['%', '%25'];
        escape_sequence = [' '] + escape_sequence.split();
        
        count = 0;
        escape_sequence_length = len(escape_sequence);
        new_string = string;
        
        if(percent_sign[0] in new_string):
        #{
            new_string = new_string.replace(percent_sign[0], percent_sign[1]);
        #}
        for count in range(count, escape_sequence_length, 2):
        #{
            if(escape_sequence[count] in safe):
            #{
                continue;
            #}
            new_string = new_string.replace(escape_sequence[count], escape_sequence[count + 1]);
        #}
        return new_string;
    #}
    
    def unquote(self, string, safe = ''):
    #{
        escape_sequence = '  %20 ! %21 $ %24 & %26 ` %60 : %3A < %3C > %3E [ %5B ] %5D { %7B } %7D " %22 + %2B # %23 @ %40 / %2F ; %3B = %3D ? %3F \ %5C ^ %5E | %7C ~ %7E \' %27 , %2C'
        percent_sign = ['%', '%25'];
        escape_sequence = [' '] + escape_sequence.split();
        
        count = 0;
        escape_sequence_length = len(escape_sequence);
        new_string = string;
        
        if(percent_sign[1] in new_string):
        #{
            new_string = new_string.replace(percent_sign[1], percent_sign[0]);
        #}
        for count in range(count, escape_sequence_length, 2):
        #{
            if(escape_sequence[count] in safe):
            #{
                continue;
            #}
            new_string = new_string.replace(escape_sequence[count + 1], escape_sequence[count]);
        #}
        return new_string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}