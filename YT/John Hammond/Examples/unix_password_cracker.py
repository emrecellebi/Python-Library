#!/usr/bin/env python2


from colorama import Fore as colors;
from os import getuid;
from crypt import crypt;
from sys import argv;
from spwd import getspnam;
# https://wiki.skullsecurity.org/index.php/Passwords

def main():
#{
    if(getuid() != 0):
    #{
        print colors.YELLOW + "You must be root to run this utility.";
        exit(1);
    #}
    
    if(len(argv) <= 1):
    #{
        print colors.YELLOW + "What user should we try and crack the password for?" + colors.RESET;
        username = raw_input();
    #}
    else:
    #{
        username = argv[1];
    #}
    
    print colors.CYAN + "Cracking UNIX password for user... " + colors.YELLOW + username;
    
    dict_file = open("passwords.txt");
    
    encrypted_password = getspnam(username)[1];
    
    print colors.CYAN + "Encrypted password looks to be... " + colors.YELLOW + encrypted_password;
    
    count = 0;
    for password in dict_file.readlines():
    #{
        password = password.rsplit()[0];
        new_password = crypt(password, encrypted_password);
        print colors.YELLOW + "Trying password " + colors.MAGENTA + password + colors.YELLOW + "...";
        if(encrypted_password == new_password):
        #{
            print colors.GREEN + "Password found! ";
            print colors.YELLOW + "It took " + colors.CYAN + str(count) + colors.CYAN + " different attempts to find it";
            print colors.RESET + "The cracked password is " + colors.BLUE + password;
            exit(0);
        #}
        else:
        #{
            print colors.RED + "Password failed...";
            count += 1;
        #}
    #}
    print colors.RED + "No password crack was found. Try another dictionary file.";
    exit(1);
#}

if(__name__ == "__main__"):
#{
    main();
#}

