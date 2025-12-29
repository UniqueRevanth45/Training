class AgeError(Exception):
    pass

try:
    age=int(input("Enter your Age: "))
    if age<18:
        raise AgeError
except AgeError:
    print("Age must be 18 or above")