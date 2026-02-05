def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y

print("Hello!Please select the operation you wish to make: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1, 2, 3 or 4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {substract(num1, num2)}")

        elif choice == '3':
            print(f" {num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print (f" {num1} / {num2} = {divide(num1, num2)}")
            

        new_calc = input("Do you want to make another calculation (yes or no): ")
        if new_calc.lower() != 'yes':
            break
    
    else:
        print("Invalid input. Please choose 1, 2, 3 or 4.")


print("Closing... Have a great day!")
