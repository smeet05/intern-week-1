# Problem: Implement a stack using a list.

stack = []

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value: ")
        stack.append(value)
        print("Value pushed.")

    elif choice == "2":
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            value = stack.pop()
            print("Popped value:", value)

    elif choice == "3":
        print("Stack:", stack)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")