# JSON = JavaScript Object Notataion
'''
6 kinds of data type in JSON

Number: 1, 2, 3, 4.1
String: "String1", "String2"
Bool: true false (note small case)
Null: null
Array: [10, 20, "hello", true]
Object instance: 
{
    "KeyA": 273, 
    "KeyB": "Val", 
    "KeyC": true, 
    "KeyD": [12, 52],
    "KeyE": {"name": 52}
}
'''
import urllib.request as req
import json

json_str = req.urlopen("https://api.github.com/repositories").read()
json_example = """[
    {"name": "apple", "price": 100},
    {"name": "banana", "price": 200}, 
    {"name": "pear", "price": 300}, 
    {"name": "orange", "price": 400}, 
    {"name": "plum", "price": 500}
]"""

output = json.loads(json_str) # usually using loads
print(type(output)) # json.loads returns a list   
# print(output)

for item in output: 
    print(item["name"])
    print(item["full_name"])
    print(item["owner"]["login"])
    print()

# text = json.dumps(json_example) # usually using dumps 
# print(type(text))    
# print(text)

