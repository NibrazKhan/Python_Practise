# len(string)
print(len('Hello'))
# lower()
text = 'Hello World'
temp = text.lower()
#upper()
text = 'Hello World'
temp = text.upper()

#strip()
# text = ' BracU CSE110'
# temp = text.strip()
#lstrip()
text = ' BracU CSE110'
temp = text.lstrip()
#rstrip()
text = ' BracU CSE110          '
temp = text.rstrip()
#count()
text = 'Bangladesh'
temp = text.count('a')
#startswith(substring):
text = 'Hello'
temp =text.startswith('He')
#endswith(substring)
text = 'Tikolo'
temp =text.endswith('lo')
temp_false=text.endswith("Ti")
print(temp_false)
#find(substring)
text = 'Bangladesh'
temp = text.find('a')
#replace(oldstring,newstring): Replace every instance of the old string with the new string
# -----------------
car="Toyota"
# var=car.replace("T","B")
var=car.replace("Toy","B")
print(var)
# replacing a long string
var="Pizza,Burger,Somosa"
# var=var.replace(",","")
var=var.replace(",","\n")
print(var)
text = 'Hello'
temp = text.replace('l','nt')
print(text)
print(temp)
# split(delimeter):returns a list of string splitted using the delimiter
# Extract individual words from a string.
str1= "I love playing cricket"
print(str1.split())
str2="Egg,Rooti,Porota,chini"
print(str2.split(','))
#List Comprehension:
#in separate line:
[print(i) for i in str1.split()]
#in single line:
[print(i,end=" ") for i in str1.split()]
#string.join(iterable):
lis=["I","Am","The","Best"]
# Join this list in a single sentence?
print()
print(" ".join(lis))
