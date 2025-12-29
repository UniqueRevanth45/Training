try:
    f=open('non_existent_file.txt', 'r')
    print(f.read())
except FileNotFoundError:
    print("Error: The file does not exist.")   
finally:
    print("Execution completed.")
    try:
        X=int(input())
        print(10/X)
    except(ValueError, ZeroDivisionError):
        print("Invalid Input or Zero Division ")