import os
userfile = input("Enter the filename: ")
filename = os.path.join(os.getcwd(),'GenAI-Task6-Himani', userfile)
print('File path:', filename)
try:
    with open(filename, 'r') as file:
        content = file.readlines()[0:3]
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
else:
    print("Something went wrong!!")
finally:
    print("File operation attempted.")