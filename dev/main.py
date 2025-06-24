import os

vault = []

while True:
    print("\nWelcome to the password vault!")
    print("Choose an option:")
    print("1. Add a new password")
    print("2. View passwords")
    print("3. Remove a password")
    print("4. Change a password")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("This is where you put all your passwords!")
        password = input("Enter your password: ")
        vault.append(password)
        print("password saved!")

    elif choice == '2':
        if not vault:
            print("No passwords saved")
        else:
            print("passwords: ")
            for index, pwd in enumerate(vault, start=1):
                print(f"{index}. {pwd}")
                print(f"updated list")
    
    elif choice == '3':
        password_to_remove = input("Choose what password you want to remove: ")
        if password_to_remove in vault:
            vault.remove(password_to_remove)
            print(f"updated list")
        

    



    elif choice == '5':
        print("very well, goodbye!")
        break



    else:
        print("this option is invalid.")
        

                    