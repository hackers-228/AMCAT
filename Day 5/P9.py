def login():
    username = input("Enter username:")
    password = input("Enter password:")
    if username == password:
        print("Login successfully")
    else:
        print("invalid credential")

login()