import json

numbers = [2, 3, 5, 7, 213, 55, 662]

filename = 'number.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
