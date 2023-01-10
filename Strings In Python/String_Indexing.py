# Positive Indexing:
# From left to right.
name="Nibraz"
# printing the last character:
print(name[1])
print(name[len(name)-1])
#Negative Indexing:
name="Khan"
# printing the last character:
print(name[-1])
# printing the first character:
print(name[-len(name)])
# Will give index error if out of range.
print(name[100])