# Task 1
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Invalid!! Please enter integers for numerator and denominator.")
except ZeroDivisionError:
    print("Invalid!! Denominator cannot be zero.")
else:
    print(f"The result of {numerator} divided by {denominator} is: {result}")
finally:
    print("Operation Complete")