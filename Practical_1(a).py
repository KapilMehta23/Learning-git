print("Choose any number from below:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Choice:"))

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

if choice == 1:
    print(n1 + n2)
elif choice == 2:
    print(n1 - n2)
elif choice == 3:
    print(n1 * n2)
elif choice == 4:
    print(n1 / n2)
else:
    print("Enter any valid option again!")
