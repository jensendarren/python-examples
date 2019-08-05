import json, difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data=json.load(open('data.json'))
print(data)
print(data['name'])

score = SequenceMatcher(None, 'rainn', 'rain').ratio()
print(score)

match = get_close_matches("rainn", ['python', 'house', 'block', 'rain', 'ghost'])
print(match)