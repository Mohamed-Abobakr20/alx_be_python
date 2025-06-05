"""
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.
"""
def check_input():
    message = input("Choose the type you want to add (int - string - decimal)?: ")
    item = input("Enter the item to add: ")
    match message:
        case 'int':
            item = int(item)
        case 'decimal':
            item = float(item)
    return item             
            

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = check_input()
            shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            item = check_input()
            if item in shopping_list:
                shopping_list.remove(item)
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()