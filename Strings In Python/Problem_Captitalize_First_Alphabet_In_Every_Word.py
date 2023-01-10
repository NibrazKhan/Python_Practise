string= "rahim lives in sylhet"
splitted_string=string.split()
print(splitted_string)
output=""
for i in splitted_string:
    # print(i[0].upper())
    output+=i[0].upper()+i[1:]+" "
print(output)

