#List Comprehension:
#in separate line:
str1="I love Programming"
[print(i) for i in str1.split()]
#in single line:
# [print(i,end=" ") for i in str1.split()]
# Example 2
# copy numbers_list in a new list.
nums=[1,2,3,4,5,6,7,8,9,10]
#non_comprehensive way:
my_list=[]
for i in nums:
    # print(i)
    my_list.append(i)
# print(my_list)
# in one line via list comprehension.
my_list=[i for i in nums]
print(my_list)

# Print the list containing only even items.
list=[1,2,3,4,5,6,7,8,9,10]
# non-comprehensive way:
even_list=[]
for i in list:
    if i%2==0:
        even_list.append(i)
# print(even_list)
# list comprehensive way:
even_list=[i for i in list if i%2==0]
print(even_list)