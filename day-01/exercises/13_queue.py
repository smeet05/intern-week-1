# Problem: Implement a queue using a list.

queue = []

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value: ")
        queue.append(value)
        print("Value added to queue.")

    elif choice == "2":
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            value = queue.pop(0)
            print("Removed value:", value)

    elif choice == "3":
        print("Queue:", queue)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")