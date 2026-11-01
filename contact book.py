options = ["Add contact", "Search Contact", "Delete Contact", "View Contacts", "Quit"]

contact_book = []


#Adding a contact
def addContact():
    contact = {}
    contact["first name"] = ""
    contact["last name"] = ""
    contact["phone number"] = ""

    #first name
    first_name = input("Enter first name: ")
    while True:
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
        
        first_name = first_name.capitalize()
        contact["first name"] += first_name
        break

    
    #last name
    last_name = input("Enter last name: ")
    while True:
        while last_name == "":
            try_again = input("The input is empty. Would you like to try again? (y/n): ")

            while try_again != 'y' and try_again != 'n':
                try_again = input("Please type 'y' or 'n': ")

            if try_again == 'y':
                last_name = input("Enter a name: ")
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
            
        last_name = last_name.capitalize()
        contact["last name"] += last_name
        break

    #phone number
    phone_number = input("Enter your 10-digit phone number (no dashes): ")
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
        print("Contact deleted!")

    if len(results) > 1:
        while True:
            delete = int(input("Which contact would you like to delete? Enter a number: "))
            
            for i, contact in enumerate(results, start=1):
                if delete == i:
                    contact_book.remove(contact)
                    break

                else:
                    try_again = input("Invalid number. Try again? (y/n): ")

                    while try_again != 'y' and try_again != 'n':
                        try_again = input("Please type 'y' or 'n': ")

                    if try_again == 'y':
                        break
            
                    if try_again == 'n':
                        return

            

def select():
    while True:
        try:
            choice = int(input("Please select an option: "))

            if choice not in range(1,6):
                raise ValueError

            if choice == 1:
                addContact()

            if choice == 2:
                searchContact()
                
            if choice == 3:
                deleteContact()

            display_options()

            #break
        except ValueError:
            print("Invalid input. Try again.")


select()