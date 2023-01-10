#Order does not matter.
stu_id = {'Harry':12,'Ron':15,'Hermione':1}
value = stu_id['Hermione']
# print(value)
print(stu_id['Harry'])

# Can also use get() to get values, returns none if the key is not present.
stu_id = {'Harry':12,'Ron':15,'Hermione':1}
value = stu_id.get('Hermione')
print(value)
print(stu_id.get("Draco"))