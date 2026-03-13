a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a>b:
    if a>c:
        print("a is the greatest.")
    elif c>a:
        print("c is the greatest.")
    else:
        print("a is equal to c.")
else:
    if b>a:
        print("b is the greatest.")
    else:
        print("a is equal to b.")
