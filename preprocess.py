#!/usr/bin/python

import glob
import json
import sys

input_files = glob.glob('votes/201?/*/data.json')


def validate(key_list):
    fail = True

    # not a yes / not vote
    if len(key_list) > 10:
        return {}

    # first schema
    if len(key_list) == 4:
        fail = False
        for key in [u'Yea', u'Nay', u'Present', u'Not Voting']:
            if key not in key_list:
                fail = True

    if not fail:
        return {'Yea': 1, 'Nay': -1}

    # second schema
    if len(key_list) == 4:
        fail = False
        for key in [u'Aye', u'Present', u'Not Voting', u'No']:
            if key not in key_list:
                fail = True

    if not fail:
        return {'Aye': 1, 'No': -1}

    # non-schema
    if len(key_list) == 2:
        fail = False
        for key in [u'Present', u'Not Voting']:
            if key not in key_list:
                fail = True

    if not fail:
        return {}

    print key_list
    print "exiting..."
    sys.exit()

for input_file in input_files:
    with open(input_file, 'r') as f:
        vote = json.loads(f.read())
        voteid = vote['vote_id']
        schema = validate(vote['votes'].keys())

        for scheme in schema:
            consider = [info['id'] for info in vote['votes'][scheme]]
            for cons in consider:
                print ",".join([voteid, cons, str(schema[scheme])])
