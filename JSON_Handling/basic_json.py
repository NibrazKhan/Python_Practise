import json

data = '''
{
        "name":"Nibraz Khan",
        "CGPA":3.97,
        "Instituition":"Brac University"        
}
'''
print("json before parsing:", data)
# Will give an error for the below line as the json is not parsed.
# print("name:", data["name"])
# Parsing the json format into python object
json_parsed = json.loads(data)
print("json After parsing:\n", json_parsed)
print(type(json_parsed))
print("name:", json_parsed["name"])

data2 = {
    "food": "Pizza",
    "cricketers": ['Shakib Al Hasan', 'Martin Guptill', 'Michael Clarke'],
    "testing_tools": ('Selenium Web Driver', 'Robot Framework', 'Appium')
}
# Convert dictionary to Json
json_compatible = json.dumps(data2)
print("Converting to Json:\n", json_compatible)
# sort keys in json dumps
json_sorted=json.dumps(data2,sort_keys=True)
print("Sorted Json:\n", json_sorted)

