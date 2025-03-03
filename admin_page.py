from register_page import check_birth
from convert_dic import turn_dic
from datetime import datetime
import re


def check_format(email):
    if not re.match(r"^[a-z0-9]+@+mail.apu.edu.my", email):  # \w any word character
        return False
    return True


def check_date(date):
    from datetime import datetime
    try:
        valid_date = datetime.strptime(date, "%d-%m-%Y")  # Validate date format
        if valid_date > datetime.now():
            return True
        else:
            return False
    except ValueError:
        return False


def add_hall_info(file):
    print("\n---➕Add Hall Info Page➕---\n")

    hall_id = input("\nEnter Hall ID: ")
    hall_name = input("Enter Hall Type: ")
    hall_desc = input("Enter Hall Description: ")

    hall_pax = input("Enter hall pax: ")
    while True:
        if not hall_pax.isdigit():
            print("Please enter only number!")
            hall_pax = input("Enter hall pax: ")
        else:
            break

    hall_pax = int(hall_pax)

    date_list = []
    print("You can press enter to skip this session.")
    hall_ava = input("Enter desired date to make hall booking unavailable (dd-mm-yyyy): ")
    while True:
        if len(hall_ava) < 1 or check_date(hall_ava):
            date_list.append(hall_ava)
            break

        else:
            print("Please follow the format with / and type the number.")
            print("And enter a future date.")
            hall_ava = input("Enter desired date to make hall booking unavailable (dd-mm-yyyy): ")

    hall_price = input("Enter rate price per hour: ")
    while True:
        if not hall_price.isdigit():
            print("Please enter only number!")
            hall_price = input("Enter rate price per hour: ")
        else:
            break
    hall_price = int(hall_price)

    hall_info = (f"Hall ID: {hall_id}\n"
                 f"Hall Name: {hall_name}\n"
                 f"Hall Description: {hall_desc}\n"
                 f"Hall pax: {hall_pax}\n"
                 f"Unavailable date: {date_list}\n"
                 f"Hall Price per hour: {hall_price}\n")
    print(hall_info)

    my_dic = turn_dic(file)
    new_hall_info = {
        "Hall ID": hall_id,
        "Hall name": hall_name,
        "Hall Price per hour": hall_price,
        "Hall pax": hall_pax,
        "Unavailable date": date_list,
        "Hall Description": hall_desc
    }
    my_dic.append(new_hall_info)

    with open(file, "w") as f:
        f.write(str(my_dic))
        print("Hall info has added successfully.")


def search_func(file):
    print('\n---🔍Search Page🔍---\n')
    my_dic = turn_dic(file)
    info = ''
    found = False

    if file == "user_info.txt":
        print("You can enter user's First Name or Last Name to filter the search information.")
    elif file == "booking_info.txt":
        print("You can enter Username or Booking ID to filter the search information.")
    elif file == "hall_info.txt":
        print("You can enter Hall Type or Hall ID to filter the search information.")

    area = input("Search Bar (Enter to show everything): ")
    print("")

    for data in my_dic:
        if file == "user_info.txt":
            info = (f"Username: {data['Username']}\n"
                    f"Password: {data['Password']}\n"
                    f"First Name: {data['First Name']}\n"
                    f"Last Name: {data['Last Name']}\n"
                    f"Birthday: {data['Birthday']}\n"
                    f"Phone Number: {data['Phone Number']}\n"
                    f"Email: {data['Email']}\n")

        elif file == "booking_info.txt":
            info = (f"Username: {data['Username']}\n"
                    f"Hall ID: {data['Hall ID']}\n"
                    f"Duration: {data['Duration']} hours\n"
                    f"Total Price: {data['Total Price']}\n"
                    f"Start: {data['Start']}\n"
                    f"End: {data['End']}\n"
                    f"Event Name: {data['Event Name']}\n"
                    f"Event description: {data['Event Description']}\n")

        elif file == "hall_info.txt":
            info = (f"Hall ID: {data['Hall ID']}\n"
                    f"Hall Type: {data['Hall name']}\n"
                    f"Rate per hour: RM{data['Hall Price per hour']}/h\n"
                    f"Number of pax: {data['Hall pax']}pax\n"
                    f"Unavailable dates: {data['Unavailable date']}\n"
                    f"Hall description: {data['Hall Description']}\n")

        if area.lower() in str(data).lower() or len(area) < 1:
            found = True
            print(info + "\n")

    if not found:
        print("There is no information related based on your searching area.")
        print("Your search result is nothing......." "\n")


def view_func(file):
    print("\n---🪟View Page🪟---\n")
    my_dic = turn_dic(file)

    if file == "user_info.txt":
        for data in my_dic:
            info = (f"Username: {data['Username']}\n"
                    f"Password: {data['Password']}\n"
                    f"First Name: {data['First Name']}\n"
                    f"Last Name: {data['Last Name']}\n"
                    f"Birthday: {data['Birthday']}\n"
                    f"Phone Number: {data['Phone Number']}\n"
                    f"Email: {data['Email']}\n")
            print(" ")
            print(info, "\n")

    elif file == "booking_info.txt":
        for data in my_dic:
            info = (f"Username: {data['Username']}\n"
                    f"Hall ID: {data['Hall ID']}\n"
                    f"Duration: {data['Duration']} hours\n"
                    f"Total Price: {data['Total Price']}\n"
                    f"Start: {data['Start']}\n"
                    f"End: {data['End']}\n"
                    f"Event Name: {data['Event Name']}\n"
                    f"Event description: {data['Event Description']}\n"
                    f"Booking ID: {data['Booking ID']}\n")
            print(" ")
            print(info, "\n")

    elif file == "hall_info.txt":
        for data in my_dic:
            info = (f"Hall ID: {data['Hall ID']}\n"
                    f"Hall Type: {data['Hall name']}\n"
                    f"Rate per hour: {data['Hall Price per hour']}RM/h\n"
                    f"Number of pax: {data['Hall pax']}pax\n"
                    f"Unavailable date: {data['Unavailable date']}\n"
                    f"Hall description: {data['Hall Description']}\n")
            print(" ")
            print(info, "\n")

    print("")
    return


def delete_func(file):
    print("\n---ℹ️ Delete Information Page ℹ️---\n")
    print("")
    view_func(file)
    my_dic = turn_dic(file)

    while True:
        found = False
        num = 0
        if file == "hall_info.txt":
            while True:
                hall_id = input("Please enter the hall ID: ")
                for index, info in enumerate(my_dic):
                    if info["Hall ID"] == hall_id and len(hall_id) >= 1:
                        found = True
                        num += index
                        break   

                if not found:
                    print("There is no related information for your hall ID.")
                else:
                    break

        elif file == "booking_info.txt":
            while True:
                book_id = input("Please enter the booking ID: ")
                for index, info in enumerate(my_dic):
                    if info['Booking ID'] == book_id and len(book_id) >= 1:
                        found = True
                        num += index
                        break

                if not found:
                    print("There is no related information for your booking ID.")
                else:
                    break

        elif file == "user_info.txt":
            while True:
                username = input("Please enter the username: ")
                for index, info in enumerate(my_dic):
                    if info["Username"] == username and len(username) >= 1:
                        found = True
                        num += index
                        break

                if not found:
                    print("There is no related information for your username.")
                else:
                    break
        while True:
            # Confirm again with the admin
            check = input("Do you want to delete this information? (yes/no/back): ")
            check = check.lower()
            if check == "yes":
                print("The information is deleted!\n")

                # Delete the dictionary in a dictionary list
                my_dic.pop(num)
                with open(file, 'w') as w:
                    w.write(str(my_dic))
                    return
            elif check == "no":
                break
            elif check == "back":
                return
            else:
                print("Please choose only the listed selection!!!")


def edit_func(file):
    while True:
        print("\n---😷Edit Page😷---\n")
        view_func(file)
        my_dic = turn_dic(file)
        check_list = ""
        idx = ""
        hall_id = ""
        if file == "booking_info.txt":
            while True:
                found = False
                book_id = input("Please enter the booking ID of the information: ")
                print("")
                for index, info in enumerate(my_dic):
                    if info["Booking ID"] == book_id and len(book_id) >= 1:
                        found = True
                        idx = index
                        break

                if not found:
                    print("There are no related information for your booking ID.")
                else:
                    break

            check_list = ['Username', 'Hall ID', 'Duration', 'Total Price', 'Start', 'End',
                          'Event Name', 'Number of pax', 'Event Description']

        elif file == "hall_info.txt":

            while True:
                found = False
                hall_id = input("Please enter the hall ID of the information: ")
                print("")
                for index, info in enumerate(my_dic):
                    if info["Hall ID"] == hall_id and len(hall_id) >= 1:
                        found = True
                        idx = index
                        break

                if not found:
                    print("There are no related information for your hall ID.")
                else:
                    break

            check_list = ['Hall ID', 'Hall name', 'Hall Price per hour',
                          'Hall pax', 'Unavailable date', 'Hall Description']

        elif file == "user_info.txt":
            while True:
                found = False
                username = input("Please enter the username of the information: ")
                print("")
                for index, info in enumerate(my_dic):
                    if info["Username"] == username and len(username) >= 1:
                        found = True
                        idx = index
                        break

                if not found:
                    print("There are no related information for your username.")
                else:
                    break
            check_list = ['Username', 'Password', 'First Name', 'Last Name',
                          'Birthday', 'Phone Number', 'Email']

        number = 0
        for items in check_list:
            print(f"{number} Edit {items}")
            number += 1

        while True:
            edit_area = input("Enter the command number:")
            if edit_area.isdigit():
                edit_area = int(edit_area)
                if -1 < edit_area < len(check_list):
                    break
                else:
                    print("Your command number is not within the listed number!")
            else:
                print("Please enter only number!")

        data = my_dic[idx][check_list[edit_area]]
        edit = ""

        if check_list[edit_area] == "Birthday":
            edit = input("Birthday (dd/mm/yyyy): ")
            while not check_birth(edit):
                print("Please follow the format with / and type the number.")
                print("And do not write the future date.")
                print("")
                edit = input("Birthday (dd/mm/yyyy): ")

        elif check_list[edit_area] == "Unavailable date":
            date_list = []
            for d in my_dic:
                if d["Hall ID"] == hall_id:
                    unavailable_date = d["Unavailable date"]
                    date_list.extend(unavailable_date)

            while True:
                hall_ava = input("Enter desired date to make hall booking unavailable (dd-mm-yyyy): ")
                if check_date(hall_ava):
                    date_list.append(hall_ava)
                    edit = date_list
                    break

                else:
                    print("Please follow the format with / and type the number.")
                    print("And enter a future date.")

        elif check_list[edit_area] == "Start" or check_list[edit_area] == "End":
            while True:
                edit = input("Enter your booking date (DD-MM-YYYY HHMM): ")
                try:
                    datetime.strptime(edit, "%d-%m-%Y %H%M")
                    break
                except ValueError:
                    print("Please follow the format!")

        elif type(data) == str:
            edit = input("Enter the data: ")

        elif type(data) == int:
            while True:
                edit = input("Enter the data: ")
                if edit.isdigit():
                    edit = int(edit)
                    break
                else:
                    print("Please enter only digit for this session.")

        my_dic[idx][check_list[edit_area]] = edit

        with open(file, "w") as f:
            f.write(str(my_dic))

        print("")
        while True:
            status = input("Do you want to continue? (yes/no): ")
            if status.lower() == "yes":
                break
            elif status.lower() == "no":
                return
            else:
                print("Please chose only yes or no!")


def admin_email():
    file_name = "admin_email.txt"
    my_dic = turn_dic(file_name)
    while True:
        new_admin = input("Please enter the new email account for the new admin: ")
        if check_format(new_admin) and new_admin not in my_dic:
            print("The new admin email account is added.")
            break

        elif new_admin in my_dic:
            print("This account already exist in the database.")

        else:
            print("Wrong domain name!!")

    my_dic.append(new_admin)
    with open(file_name, 'w') as f:
        f.write(str(my_dic))


def admin_page():

    while True:
        print("== 🫷Welcome back admin!🫸 ==")
        print("What you like to perform?")
        print("1 Hall management")
        print("2 Booking management")
        print("3 User management")
        print("4 Exit")
        print("5 Log Out")

        choice = input("Enter your command number: ")

        if choice == "1":
            while True:
                file = "hall_info.txt"
                print("\na Add hall info")
                print("b View all hall info")
                print("c Search hall info")
                print("d Edit hall info")
                print("e Delete hall info")
                print("f Exit")

                choice2 = input("Enter your choice: ")
                choice2 = choice2.lower()

                if choice2 == "a":
                    add_hall_info(file)
                elif choice2 == "b":
                    view_func(file)
                elif choice2 == "c":
                    search_func(file)
                elif choice2 == "d":
                    edit_func(file)
                elif choice2 == "e":
                    delete_func(file)
                elif choice2 == "f":
                    print("")
                    return admin_page()
                else:
                    print("Invalid choice" "\n")

        elif choice == "2":
            while True:
                file = "booking_info.txt"
                print("\na View all booking info")
                print("b Search booking info")
                print("c Edit booking info")
                print("d Delete booking info")
                print("e Exit")

                choice3 = input("Enter your choice: ")
                choice3 = choice3.lower()

                if choice3 == "a":
                    view_func(file)
                elif choice3 == "b":
                    search_func(file)
                elif choice3 == "c":
                    edit_func(file)
                elif choice3 == "d":
                    delete_func(file)
                elif choice3 == "e":
                    print("")
                    return admin_page()
                else:
                    print("Invalid choice")

        elif choice == "3":
            while True:
                file = "user_info.txt"
                print("\na View all user info")
                print("b Search user info")
                print("c Edit user info")
                print("d Delete user info")
                print("e Add new admin email")
                print("f Exit")

                choice4 = input("Enter your choice: ")
                choice4 = choice4.lower()

                if choice4 == "a":
                    view_func(file)
                elif choice4 == "b":
                    search_func(file)
                elif choice4 == "c":
                    edit_func(file)
                elif choice4 == "d":
                    delete_func(file)
                elif choice4 == "e":
                    admin_email()
                elif choice4 == "f":
                    print("")
                    return admin_page()
                else:
                    print("Invalid choice" "\n")

        elif choice == "4":
            print("Hope to see you again~")
            exit()

        elif choice == "5":
            print("")
            return

        else:
            print("Invalid command" "\n")
