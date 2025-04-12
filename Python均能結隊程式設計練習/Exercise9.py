try:
    s = input("Enter two numbers, separated by a comma: ")
    num1, num2 = s.split(",") 
    num1 = float(num1.strip())
    num2 = float(num2.strip())
    result = num1 / num2
    print(f"Result is {result}")
    print("No exceptions")
except ZeroDivisionError:
    print("Division by zero!")
except ValueError:
    print("A comma may be missing in the input" if "," not in s else "Something wrong in the input")
finally:
    print("The finally clause is executed")
