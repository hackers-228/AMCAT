name = "Electronics"

vowels = ['A','E','I','O','U','a','e','i','o','u']

vow = 0
cons = 0

for i in name:
    if(i in vowels):
        vow+=1
    else:
        cons+=1

print("Number of vowels: ",vow)
print("Number of consonants: ",cons)