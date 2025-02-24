from register_page import register
from admin_page import admin_page
from user_page import user_page
from convert_dic import turn_dic


# Request user to go register page
def go_register():
    while True:
        perform = input("Do you want to register? (yes/no): ")
        perform = perform.lower()
        if perform == "yes":
            print("")
            return register()
        elif perform == "no":
            print("")
            return login()
        else:
            print("Wrong input! Please type again!")


def login():
    print("----🙋‍♀️Login Page🙋‍️----")
    print("")

    # Allow user to back to previous page
    while True:
        print("(Press enter key) to continue" "\n"
              "(Type back) to back to main page")
        user_perform = input("Continue or Back: ")
        if user_perform.lower() == "back":
            print("")
            return
        elif len(user_perform) < 1:
            break
        else:
            print("Please perform only the action that has listed.")
            print("")

    print("")

    while True:
        role = input("Enter as (admin/user): ")
        role = role.lower()
        if role == "admin":
            file_name = "admin_info.txt"
            break

        elif role == "user":
            file_name = "user_info.txt"
            break

        else:
            print("Invalid candidate!!")
            print("")

    # To direction the user to their page
    my_dic = turn_dic(file_name)

    # Ask username and password for three times
    # If still failed try ask for register
    for i in range(1, 4):
        username = input("Enter username: ")
        password = input("Enter password: ")
        found = False
        for info in my_dic:
            if info["Username"] == username and info["Password"] == password:
                authorise = info["Admin"]
                found = True
                print("----Login success----")
                print("")
                if authorise == "no":
                    return user_page(username)
                elif authorise == "yes":
                    return admin_page()

        # When they cannot log in, request them to go register page
        if not found and i == 3:
            return go_register()

        elif not found:
            print("Username or password incorrect")
            print("")

        i += 1
