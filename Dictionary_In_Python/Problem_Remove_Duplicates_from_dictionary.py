dic={"Cristiano Ronaldo":30,"Lionel Messi":30,"Suarez":25,"Mbappe":50,"Modric":30}
result=dict()
for key,value in dic.items():
    if value not in result.values():
        result[key]=value
print(result)