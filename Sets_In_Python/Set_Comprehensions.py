nums=[1,2,3,4,5,6,7,8,9,10,4,4]
# Non-Comprhensive way:
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)

#Comprehensive way:
my_set={i for i in nums}
print(my_set)