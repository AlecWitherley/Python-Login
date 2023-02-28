def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    cred = open(r"credentials.txt", "r")

    if(cred):
        stored_email, stored_pwd = cred.read().split("\n")
    cred.close()
    if email == stored_email and pwd == stored_pwd:
        print("Logged in Successfully!")
    else:
        print("Login failed! \n")

login()