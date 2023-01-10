box={'pencil':3,'pen':4,'eraser':2}
print(box)
box['pen']=2
print(box)
box['pen']=box['pen']+6
print(box)
# adding new elements in dictionary by specifying new key and value
box['sharpner']=8
print(box)
#Using update() function
box.update({"compass":2})
print(box)
# deleting keys in python using del keyword
del box['pencil']
print(box)
del box
print(box)