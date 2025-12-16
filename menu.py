from transactions import (
    transaction_1,
    transaction_2,
    transaction_3,
    transaction_4,
    transaction_5,
    transaction_6
)

def main_menu():
    while True:
        print("\n" + "="*50)
        print("        CS623 Project - Transaction Menu")
        print("="*50)
        print("1. Transaction 1 - Delete product p1")
        print("2. Transaction 2 - Delete depot d1")
        print("3. Transaction 3 - Rename product p1 → p10")
        print("4. Transaction 4 - Rename depot d1 → dd1 from depot and stock table ")
        print("5. Transaction 5 - Insert (p100, cd, 5) in product  and stock table")
        print("6. Transaction 6 - Insert depot d100 in depot and stock table")
        print("7. Exit")
        print("="*50)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            transaction_1()
        elif choice == "2":
            transaction_2()
        elif choice == "3":
            transaction_3()
        elif choice == "4":
            transaction_4()
        elif choice == "5":
            transaction_5()
        elif choice == "6":
            transaction_6()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1–7.")

if __name__ == "__main__":
    main_menu()
