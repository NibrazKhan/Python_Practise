# printing all the key names:
box = {'pencil':3,'pen':4,'eraser':2}
for key in box:
    print(key)
# printing all the values:
box = {'pencil':3,'pen':4,'eraser':2}
for key in box:
    print(box[key])
# Can also get all the values in list of dictionary using values() function.
box = {'pencil':3,'pen':4,'eraser':2}
for val in box.values():
    print(val)
# Can get keys and values using items() function:
box = {'pencil':3,'pen':4,'eraser':2}
for key,val in box.items():
    print(key,val)