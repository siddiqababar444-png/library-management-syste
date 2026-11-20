# Library Management System

books = ["Python Basics", "C++ Programming", "Data Structures", "English Grammar"]

print("===== Welcome to Library Management System =====")

while True:
    print("\n--- MENU ---")
    print("1. Show All Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Add a New Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- All Books ---")
        for book in books:
            print("-", book)

    elif choice == "2":
        name = input("Enter book name to borrow: ")
        if name in books:
            books.remove(name)
            print(f"{name} has been borrowed successfully!")
        else:
            print("This book is not available in the library!")

    elif choice == "3":
        name = input("Enter book name to return: ")
        books.append(name)
        print(f"{name} has been returned successfully! Thank you!")

    elif choice == "4":
        name = input("Enter new book name: ")
        books.append(name)
        print(f"{name} has been added to the library!")

    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
