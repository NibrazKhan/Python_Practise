
try:
    num1 = int(input("Enter num 1 :\n"))
    num2 = int(input("Enter num 2\n"))
    pass
except Exception as e:
    print(e)
    print("Error Occurred")
else:
    print("The sum of these two number is ", num1 + num2)
finally:
    print("This is a super duper important line")
