# Creating a set.
# Sets only takes unique values.
s1 = {23,2,2,2,2,2,3,2,1,2,2,12,6,3,12}
# can also create a set by passing list inside set()
num_set=set([0,1,2,3,4,5])

# Add one value inside sets.
s1.add(4444)
# Adds multiple values in set
s1.update([12,12,423,3423,634,123,432,23])
print(len(s1))
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

#remove(element)
s1.remove(3)
# removing an element that is not in the set.(will give error)
# s1.remove(345345345)
# discard doesnot give any error, it discards if doesnot present and removes if present
# like list: .pop,.clear,del,
# intersection,union
s1.discard(34534534)
print(s1)
# intersection:
x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}
result=x.intersection(y,z)
print(result)