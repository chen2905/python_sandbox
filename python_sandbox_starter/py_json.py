# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json


userJson = '{"first_name":"chen","last_name":"gao","age":30}'

user = json.loads(userJson)

# print(user)
# print(user['first_name'])

#change dict into a json


car = {'make':'Ford','model':'Mustang','year':1970}

carJson = json.dumps(car)

print (carJson)