#!/usr/bin/env python2

import os;
import re;
import subprocess as shell;

def main():
#{
    repo_url = 'https://github.com/l33tdev42/testApp';
    print(shell.check_output(str('git clone ' + repo_url).split()))
    
    repo_dir = repo_url.split('/')[-1];
    os.chdir(repo_dir);
    content = shell.check_output('git show'.split());
    print content;
    
    matched = re.search('CTF{.*}', content, re.IGNORECASE);
    print matched.group();

#}

if(__name__ == "__main__"):
#{
    main();
#}