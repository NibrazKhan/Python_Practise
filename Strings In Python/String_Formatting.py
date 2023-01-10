#String formatting:
name="Nibraz"
creation_name="human"
temp="Hello I am {0} and I am {1}".format(name,creation_name)
# Interchanging
temp="Hello I am {1} and I am {0}".format(name,creation_name)
print(temp)
# f-string:
temp=f"Hello I am {name} and I am {creation_name}"
print(temp)
