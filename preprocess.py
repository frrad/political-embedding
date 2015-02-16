import glob
import json

input_files = glob.glob('votes/201?/*/data.json')

with open(input_files[0], 'r') as f:
    print json.loads(f.read())['votes'].keys()
