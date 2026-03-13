entered_string = input("Enter a string: ")
string_to_print = ""

for i in entered_string:
    if i not in string_to_print:
        string_to_print += i

print(string_to_print)
        