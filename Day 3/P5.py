
ch = ord(input("Enter any character: "))

if 65 <= ch <= 90:
    print(f"'{chr(ch)}' is an uppercase letter.")
elif 97 <= ch <= 122:
    print(f"'{chr(ch)}' is a lowercase letter.")
elif 48 <= ch <= 57:
    print(f"'{chr(ch)}' is a digit.")
else:
    print(f"'{chr(ch)}' is a special symbol.")
