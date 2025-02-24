import re
from datetime import datetime
from convert_dic import turn_dic


# Check the format of the email to identify user
def check_user_email(email):
    if re.match(r"^[a-z0-9]+@+[a-z]+[.][a-z]{2,3}$", email):
        return True
    return False


# To avoid duplicate email address
def email_duplicate(email):
    admin_info = turn_dic("admin_info.txt")
    user_info = turn_dic("user_info.txt")
    check = any(admin['Email'] == email for admin in admin_info) or any(user['Email'] == email for user in user_info)
    return check


# check email is exist in admin_email database or not
def email_exist(email):
    my_dic = turn_dic("admin_email.txt")
    return email in my_dic


# Check the format of the user input in birthday section
def check_birth(birth_day):
    try:
        valid_date = datetime.strptime(birth_day, "%d/%m/%Y")  # Validate date format
        if valid_date < datetime.now():
            return True
    except ValueError:
        return False


def register():

    # Giving user instruction
    print("----®️Register Page®️----")
    print("Only APU email will be given authorization to act as admin.")
    print("For security🔐 reason, please don't put the same characters for "
          "your username and password.")
    print("")
    f_user = turn_dic("user_info.txt")
    f_admin = turn_dic("admin_info.txt")

    # Allow user to back to previous page
    while True:
        print("(Press enter key) to continue" "\n"
              "(Type back) to back to main page" "")
        user_perform = input("Continue or Back: ")
        if user_perform.lower() == "back":
            print("")
            return
        elif len(user_perform) < 1:
            break
        else:
            print("Please perform only the action that has listed.")
            print("")

    while True:
        role = input("What type of account you want to create? (admin/user): ")
        role = role.lower()
        if role == "admin":
            break

        elif role == "user":
            break

        else:
            print("Invalid candidate!!")
            print("")

    print("")
    # Ask username
    while True:
        username = input("Username: ")
        # Check if 'username' exists in the user data
        user_exists = any(user["Username"] == username for user in f_user)
        # Check if 'username' exists in the admin data
        admin_exists = any(admin["Username"] == username for admin in f_admin)
        if len(username) >= 1:
            if user_exists or admin_exists:
                print("Username exist.")
            else:
                break

    # Ask password
    while True:
        while True:
            password = input("Password: ")
            if len(password) < 8:  # User couldn't need at least 8 characters to create password
                print("Please write at least 8 characters to create the password.")
            else:
                break

        password2 = input("Retype the password: ")

        if password != password2:     # Make sure user type same password twice
            print("Passwords do not match.")
        elif username == password:  # User are not allow to have same characters for username and password
            print("Please avoid using your password same as username!!!")
        else:
            break

    # Ask first name
    while True:
        first_name = input("First Name: ")
        no_space = first_name.replace(" ", "")
        if not no_space.isalpha():
            print("Please enter only alphabets.")
        else:
            first_name = no_space.title()
            break

    # Ask last name
    while True:
        last_name = input("Last Name: ")
        no_space = last_name.replace(" ", "")
        if not no_space.isalpha():
            print("Please enter only alphabets.")
        else:
            last_name = last_name.title()
            break

    # Ask user birthday
    birth_day = input("Birthday (dd/mm/yyyy): ")
    while not check_birth(birth_day):
        print("Please follow the format with / and type the number.")
        print("And do not write the future date.")
        print("")
        birth_day = input("Birthday (dd/mm/yyyy): ")

    # Ask user contact number
    contact_num = input("Phone Number: ")

    # Ask user email address and check its format, avoid create unauthorized admin account and duplicate account
    # If failed enter the correct email account for 3 times
    # Ask register want to continue or not
    num = 5
    while True:
        if num % 4 == 0:
            while True:
                user_perform = input("Do you want to continue (yes/no): ")
                user_perform = user_perform.lower()
                if user_perform == "yes":
                    num += 1
                    break
                elif user_perform == "no":
                    print("")
                    return
                else:
                    print("Please only enter the listed selection!")

        email = input("Email: ")
        if not email_duplicate(email):
            if role == "user":
                if check_user_email(email):
                    admin = "no"
                    file_name = "user_info.txt"
                    break

                else:
                    print("Wrong email format. Please try again!!")

            elif role == "admin":
                # check email is exist in admin_email database or not
                if email_exist(email):
                    admin = "yes"
                    file_name = "admin_info.txt"
                    break

                else:
                    print("This account is not exist in the admins' email database.")

        else:
            print("There is another account that link to this email address.")

        num += 1

    data = {
        "Username": username,
        "Password": password,
        "First Name": first_name,
        "Last Name": last_name,
        "Birthday": birth_day,
        "Phone Number": contact_num,
        "Email": email,
        "Admin": admin
    }

    my_dic = turn_dic(file_name)
    my_dic.append(data)

    with open(file_name, 'w') as f:
        f.write(str(my_dic))
        f.close()

    print("----Register successful----" "\n")
