try:
    username=input("Username: ")
    password=input("Password: ")
    
    if password != "admin123":
        raise ValueError("Incorrect Password")
    print("Login Successful")
except ValueError as e:
    print(e)