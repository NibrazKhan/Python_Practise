# Reversing a string in python
inp="Nibraz"
# Approach 1:
# print(len(inp))
# output=""
# for i in range(len(inp)-1,-1,-1):
#     output=output+inp[i]
# print("reversed:",output)
#Approach 2:
# Nibraz
# N
# N
# "i"+"N"="iN"
# "b"+"iN"=biN
# "r"+"biN"=rbiN
# output=""
# for i in inp:
#     output=i+output
# print(output)

# Approach 3
inp="Programming"
# print(inp[::-1])
#Count words in a string
# input="We love Bangladesh"
# splitted_string=input.split()
# print("count of words in a string is",len(splitted_string))
# Capitalize first letter in every word
input="i am a superb individual"
# output="I Am A Superb Individual"
words=input.split()
# print(words)
# output=""
# for i in words:
#     output+=i[0].upper()+i[1:]+" "
# print(output)
#: input: bangladesh
#		    Output: B8H # Do it in at most two lines in python.
string="bangladesh"
# print(string[0].upper())
# print(string[-1].upper())
# print(len(string[1:-1]))
print(string[0].upper()+str(len(string[1:-1]))+string[-1].upper())





