def add():
    val1 = int(input("enter first value:"))
    val2 = int(input("enter second value:"))
    # print(val1+val2)
    sum = val1+val2
    mul = val1 * val2
    sub = val1 - val2
    div = val1 / val2
    return sum, mul, sub, div

# print(add())
res = add()
print("Result =",res)