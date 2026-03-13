mylist = [2,5,8,4,1,9,8]

even = 0
odd = 0
sum = 0
for i in mylist:
    if i%2==0:
        even+=1
    else:
        odd+=1
    sum+=i

print("number of even numbers: ",even)
print("number of odd numbers: ",odd)
print("sum of all the numbers: ",sum)
