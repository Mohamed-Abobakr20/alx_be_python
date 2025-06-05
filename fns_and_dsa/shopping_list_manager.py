"""
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.
"""
def check_input(dataType):
    match dataType:
        case 'int':
            item = int(input("Enter the item to add: "))
            return item
        case 'str':
            item = input("Enter the item to add: ")
            return item
        case 'decimal':
            item = float(input("Enter the item to add: "))
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
            message = input("Choose the type you want to add (int - string - decimal)?: ")
            item = check_input(message)
            shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            message = input("Choose the type you want to add (int - string - decimal)?: ")
            item = check_input(message)
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