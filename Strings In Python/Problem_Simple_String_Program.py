# input: bangladesh
# Output: B8H
# Do it in one line.
string="bangladesh"
# print(string[0].upper())
# print((len(string)))
# print(string[-1])
print(string[0].upper()+str(len(string[1:-1]))+string[-1].upper())