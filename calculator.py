def add(x, y):
    return x + y

def substract(x, y):
    return x - y

print("Hello!Please select the operation you wish to make: ")
print("1. Addition")
print("2. Substraction")

while True:
    choice = input("Enter choice (1 or 2): ")

    if choice in ('1', '2'):
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

        new_calc = input("Do you want to make another calculation (yes or no): ")
        if new_calc.lower() != 'yes':
            break
    
    else:
        print("Invalid input. Please choose 1 or 2.")

print("Closing... Have a great day!")
