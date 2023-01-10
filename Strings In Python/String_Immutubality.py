# - Immutable means once it has been created its value cannot be changed.
# So, each time we have to modify the
# values, we need to make a copy of the original one and
# make changes to the duplicate one.
text = "Python"
text[3] = "K"
print("We cannot make changes to the created string")