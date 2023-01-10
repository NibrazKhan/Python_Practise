# Create a dictionary{'name':'hero'} for each name,hero in zip(names,heros)
names=['Bruce','Clark','Peter','Logan','Wade']
heros=['Batman','Superman','Spiderman','Wolverine','Deadpool']
# zip()
# print(zip(names,heros))
# for i in zip(names,heros):
#     print(i)
# Zip prints out one index of a list and another index of a list in a tuple format
# empty dictionary
# non-comprehensive way:
my_dict={}
for name,hero in zip(names,heros):
    my_dict[name]=hero
print(my_dict)

my_dict={name:hero for name,hero in zip(names,heros)}
print(my_dict)