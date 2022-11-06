#!/usr/bin/env python

import os

if(__name__ == "__main__"):
#{
    head = '<table border="1" cellpadding="5"><tr bgcolor="E0E0E0">'
    all_lines = list()
    target_dir = './'
    
    if(os.path.isdir(target_dir)):
    #{
        os.chdir(target_dir)
        
        log_file = open('all_shares_found.html', 'w')
        log_file.write(head)
        
        for file in os.listdir('./'):
        #{
            if(file.endswith('.html')):
            #{
                f_handle = open(file)
                for line in f_handle.readlines():
                #{
                    if(line.startswith("<tr>")):
                    #{
                        if not (line in all_lines):
                        #{
                            all_lines.append(line)
                            log_file.write(line)
                        #}
                    #}
                #}
            #}
        #}
        log_file.close()
    #}
#}