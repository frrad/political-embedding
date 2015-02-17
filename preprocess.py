import glob
import json
import sys

input_files = glob.glob('votes/201?/*/data.json')

def validate(key_list):
    if len(key_list) != 4:
        print "keylist has wrong length", key_list
        sys.exit()
    
    for key in [u'Yea', u'Nay', u'Present', u'Not Voting']:
        if key not in key_list:
            print key, 'not in key_list', key_list
            sys.exit()

    return True



with open(input_files[0], 'r') as f:
    vote = json.loads(f.read())
    print vote['vote_id']
    validate(vote['votes'].keys())
    print [info['id'] for info in vote['votes']['Yea']]
    print [info['id'] for info in vote['votes']['Nay']]
    print vote['votes']
