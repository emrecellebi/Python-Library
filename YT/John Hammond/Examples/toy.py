#!/usr/bin/env python2

import hashlib, getpass;
from colorama import *;

class Base:
#{
    def __init__(self):
    #{
        init();
        
        filename = "save.dat";
        save_data = open(filename, 'w+');
        contents = save_data.read();
        
        code = hashlib.sha512();
        
        print(Fore.BLUE + "Hello welcome to the nullshell security shell login shell!" + Fore.YELLOW + Style.BRIGHT);
        if(contents == ""):
        #{
            print(Fore.YELLOW + Style.BRIGHT + "You need to create a password to be able to log in with!");
            password = getpass.getpass();
            code.update(password);
            save_data.write(code.hexdigest());
            print(Fore.GREEN + "\n\nSuccess! We have stored your password! Now when you log in next time, you will be asked for this and you will need to get it right!");
            exit();
        #}
        else:
        #{
            print(Fore.RESET + "Please login by entering the password: ");
            print(Fore.GREEN + "-----------------------------\n\n" + Fore.YELLOW + Style.BRIGHT);
            password = getpass.getpass();
            print(Fore.RESET + Style.RESET_ALL);
            code.update(password);
            hashed = code.hexdigest();
            if(contents == hashed):
            #{
                print(Fore.GREEN + Style.BRIGHT + "\n\nSuccess! You have successfully logged in! Thank you!");
            #}
            else:
            #{
                print(Fore.RED + Style.BRIGHT + "\n\nFailure! You have entered the wrong password!");
            #}
        #}
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}