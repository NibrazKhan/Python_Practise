#1) Looping through tuple using for loop:
example_tuple = ("Banana", "Mango", "Apple",
"Orange","Grape","Jackfruit")
for fruit in example_tuple:
    print(fruit)
#2) To check if an item exists in the tuple:
example_tuple = ("Banana", "Mango", "Apple",
"Orange","Grape","Jackfruit")
if "Grape" in example_tuple:
    print("Yes,Grape is in the tuple")
#4) To create a tuple with single item, we
# need to put comma:
# example_tuple = ("Grape",)
print(type(example_tuple))
#NOT a tuple
example_tuple = ("Grape")
print(example_tuple)
print(type(example_tuple))
# deleting a tuple
del example_tuple["Jackfruit"]

print(example_tuple)
del example_tuple
# joining two tuples.:
tuple1 = ("Anna", "Lukas","Julia")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)