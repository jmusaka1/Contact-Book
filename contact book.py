options = ["Add contact", "Search Contact", "Delete Contact", "View Contacts", "Update Contact", "Quit"]

contact_book = []


#Adding a contact
def addContact():
    contact = {}
    contact["first name"] = ""
    contact["last name"] = ""
    contact["phone number"] = ""

    #first name
    first_name = input("Enter first name: ").strip().capitalize()
    while first_name == "":
        try_again = input("The input is empty. Would you like to try again? (y/n): ")

        while try_again != 'y' and try_again != 'n':
            try_again = input("Please type 'y' or 'n': ")

        if try_again == 'y':
            first_name = input("Enter a name: ")
            first_name = first_name.strip().capitalize()

        if try_again == 'n':
            return

    first_name_check = any(not (char.isalpha() or char == '-' or char == "'") for char in first_name)


    while first_name_check is True:
        proceed = input("The name is invalid. Would you like to try again? (y/n): ")
        while proceed != 'y' and proceed != 'n':
            proceed = input("Please type 'y' or 'n': ")

        if proceed == 'y':
            first_name = input("Enter first name: ")
            first_name_check = any(not (char.isalpha() or char == '-' or char == "'") for char in first_name)
        if proceed == 'n':
            return
        
    contact["first name"] += first_name
        

    
    #last name
    last_name = input("Enter last name: ").strip().capitalize()
    while last_name == "":
        try_again = input("The input is empty. Would you like to try again? (y/n): ")

        while try_again != 'y' and try_again != 'n':
            try_again = input("Please type 'y' or 'n': ")

        if try_again == 'y':
            last_name = input("Enter last name: ")
            last_name = last_name.strip().capitalize()

        if try_again == 'n':
            return

    last_name_check = any(not (char.isalpha() or char == '-' or char == "'") for char in last_name)

    while last_name_check is True:
        proceed = input("The name is invalid. Would you like to try again? (y/n): ")
        while proceed != 'y' and proceed != 'n':
            proceed = input("Please type 'y' or 'n': ")

        if proceed == 'y':
            last_name = input("Enter last name: ")
            last_name_check = any(not (char.isalpha() or char == '-' or char == "'") for char in last_name)
        if proceed == 'n':
            return
            
    contact["last name"] += last_name
        

    #phone number
    phone_number = input("Enter your 10-digit phone number (no dashes): ").strip()
    phone_number_check = any(not char.isdigit() for char in phone_number)

    while phone_number_check is True or len(phone_number) != 10:
        proceed = input("Invalid number. Would you like to try again? (y/n): ")

        while proceed != 'y' and proceed != 'n':
            proceed = input("Please type 'y' or 'n': ")
        
        if proceed == 'y':
            phone_number = input("Enter your 10-digit phone number (no dashes): ")
            phone_number_check = any(not char.isdigit() for char in phone_number)
                
        if proceed == 'n':
            return
    
    contact["phone number"] += phone_number
    
    contact_book.append(contact)
    print("Contact added!\n")


def display_options():
    for num, option in enumerate(options, start=1):
        print(f"{num}.{option}")

display_options()

# Search Contact
def searchContact():

    if len(contact_book) == 0:
        print("Contact book is empty \n")
        return 0

    while True:
        name = input("Enter a name: ")
        name = name.strip().capitalize()
        search_results = []

        while name == "":
            try_again = input("The input is empty. Would you like to try again? (y/n): ")

            while try_again != 'y' and try_again != 'n':
                try_again = input("Please type 'y' or 'n': ")

            if try_again == 'y':
                name = input("Enter a name: ")
                name = name.strip().capitalize()

            if try_again == 'n':
                return 0


        for contact in contact_book:
            if contact["first name"] == name or contact["last name"] == name:
                search_results.append(contact)
        
        if len(search_results) == 0:
            try_again = input("No search results. Try again? (y/n): ")

            while try_again != 'y' and try_again != 'n':
                try_again = input("Please type 'y' or 'n': ")
                    
            if try_again == 'n':
                return 0
        
        else:
            if len(search_results) > 1:
                for item, result in enumerate(search_results, start=1):
                    print(f"{item}. {result['first name']} {result['last name']} | Phone no: {result['phone number']}")
            else:
                for result in search_results:
                    print(f"{result['first name']} {result['last name']} | Phone no: {result['phone number']}")
            print("\n")
            return search_results
            

#Deleting a contact
def deleteContact():
    results = searchContact()

    if results == 0:
        return
    
    #There are search results
    if len(results) == 1:
        confirmation = input("Would you like to delete this contact? (y/n):")
        while confirmation != 'y' and confirmation != 'n':
            confirmation = input("Please type 'y' or 'n': ")

        if confirmation == 'y':
            contact_book.remove(results[0])
            print('Contact deleted')
                

    if len(results) > 1:
        while True:
            try:
                delete = int(input("Which contact would you like to delete? Enter a number: "))
                
                for i, contact in enumerate(results, start=1):
                    if delete == i:
                        confirmation = input( "Would you like to delete this contact? (y/n):")

                        while confirmation != 'y' and confirmation != 'n':
                            confirmation = input("Please type 'y' or 'n': ")

                        if confirmation == 'y':
                            contact_book.remove(contact)
                            print('Contact deleted')
                            return

                if delete not in range(1, len(results)+1):
                    try_again = input("Invalid number. Try again? (y/n): ")

                    while try_again != 'y' and try_again != 'n':
                        try_again = input("Please type 'y' or 'n': ")
                    
                    if try_again == 'n':
                        return

            except ValueError:
                print('Invalid input. Try again.')

#Viewing Contacts
def viewContact():

    if len(contact_book) == 0:
        print("Contact book is empty")

    for contact in contact_book:
        print(f"-{contact['first name']} {contact['last name']} | Phone no: {contact['phone number']}")
    print('\n')

#Updating a contact
def updateContact():
    results = searchContact()

    if results == 0:
        return

    while True:
        try:
            update_selection = int(input(
                """Which part do you want to update?
                1. First name
                2. Last name
                3. Phone number
                Enter a number: 
                """))

            if update_selection not in range(1,4):
                raise ValueError

            #Names
            if update_selection == 1 or update_selection == 2:
                if len(results) == 1:
                    while True:
                        new_name = input("Enter the new name: ").strip().capitalize()
                        while new_name == "":
                            try_again = input(
                                "The input is empty. Would you like to try again? (y/n): ")

                            while try_again != 'y' and try_again != 'n':
                                try_again = input("Please type 'y' or 'n': ")

                            if try_again == 'y':
                                new_name = input("Enter a name: ")
                                new_name = new_name.strip().capitalize()

                            if try_again == 'n':
                                return

                        new_name_check = any(not (char.isalpha() or char == '-' or char == "'") for char in new_name)

                        while new_name_check is True:
                            proceed = input(
                                "The name is invalid. Would you like to try again? (y/n): ")
                            while proceed != 'y' and proceed != 'n':
                                proceed = input("Please type 'y' or 'n': ")

                            if proceed == 'y':
                                new_name = input("Enter name: ")
                                new_name_check = any(
                                    not (char.isalpha() or char == '-' or char == "'") for char in new_name)
                            
                            if proceed == 'n':
                                return
                        
                        if new_name == results[0]['first name'] or new_name == results[0]['last name']:
                            try_again = input("This is the old name. Would you like to try again? (y/n): ")

                            while try_again != 'y' and try_again != 'n':
                                try_again = input("Please type 'y' or 'n': ")

                            if try_again == 'n':
                                return
                        else:
                            break


                confirmation = input("Confirm? (y/n): ")

                while confirmation != 'y' and confirmation != 'n':
                    confirmation = input("Please type 'y' or 'n': ")

                if confirmation == 'y':
                    if update_selection == 1:
                        results[0]['first name'] = new_name
                    
                    else:
                        results[0]['last name'] = new_name

                    print("Contact updated!")
                    return

                if confirmation == 'n':
                    return

        except ValueError:
            print('Invalid input. Try again')

def select():
    while True:
        try:
            choice = int(input("Please select an option: "))

            if choice not in range(1,7):
                raise ValueError

            if choice == 1:
                addContact()

            elif choice == 2:
                searchContact()
                
            elif choice == 3:
                deleteContact()

            elif choice == 4:
                viewContact()

            elif choice == 5:
                updateContact()

            else:
                return

            display_options()

            #break
        except ValueError:
            print("Invalid input. Try again.")


select()