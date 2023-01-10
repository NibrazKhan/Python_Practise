''' JavaScript Object Notation '''
import json

with open('states.json') as f:
  # use json.load when handling a json file
  data = json.load(f)
print(data)
for state in data['states']:
  #deleting a key in dictionary
  del state['area_codes']

with open('new_states.json', 'w') as f:
  json_dumped= json.dump(data, f, indent=2)
print(data)