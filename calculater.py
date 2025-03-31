def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error! Division by zero."
    return x / y

while True:
    print("\n📌 Simple Calculator")
    print("1️⃣ Addition")
    print("2️⃣ Subtraction")
    print("3️⃣ Multiplication")
    print("4️⃣ Division")
    print("5️⃣ Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("👋 Exiting... Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"✅ Result: {num1} × {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"✅ Result: {num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("❌ Invalid choice! Please select a valid option.")
