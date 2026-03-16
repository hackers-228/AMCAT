def searchvalue(target):
    for i in range(len(mylist)):
        if mylist[i] == target:
            return i
        return -1

mylist = [4,2,7,8,5,4,1]
target =  10
result = searchvalue(target)
if result != -1:
    print("value found at index number = ",result)
else:
    print("value not found in the list")