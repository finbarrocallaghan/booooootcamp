import json

tweets = [json.loads(s) for s in open('20120807150301.json', 'r').read().split('\n\n')[:-1]]
