import json
import random
import re
import os

file_path = "data/users.json"

def load_data():
    '''
    Check if the file and folder exists. If exists, loads the data. If not, creates the file and an empty list.
    '''
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return data

def load_user():
    '''
    Prints data of every user.
    '''
    data = load_data()
    for user in data:
        print(f"Id: {user["id"]}\nUsername: {user["username"]}\nNIP: {user["nip"]}\nPESEL: {user["pesel"]}\nREGON: {user["regon"]}\nPassword: {user["password"]}\nStatus: {user["status"]}\n")

def save_data(data):
    """
    Saves data to .json file.
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def check_user():
    username_correct = False
    while username_correct == False:
        user_count = 0
        login_username = input("Enter your username (Full name): ")
        for value in data:
            if value["username"] == login_username:
                username_correct = True
                user_count += 1
                break
        if user_count == 0:
            print("Incorrect username, try again.\n")
    return login_username

def add_user(user_data):
    '''
        Loads data from the .json file, creates new user with provided data and saves them to the file.
    '''
    # Load existing data
    data = load_data()

    # Add new user
    if data:
        user_data["id"] = data[-1]["id"] + 1
    else:
        user_data["id"] = 1

    data.append(user_data)

    # Save new user to the file
    save_data(data)

    print("User created successfully!")

def remove_user(user_id):
    """
    Makes user inactive based on the ID.
    """
    # Load existing data
    data = load_data()

	# Find a list with user that needs to be deleted
    for user in data:
        if user["id"] == user_id:
            user.update({"status": "Inactive"})
            break

	# Saves new date to the found list. It's not necessary to check if list was found because it's already done in other part of the code.
    save_data(data)
    print(f"User has been deleted.\n")

def edit_user(user_id, updated_data):
    """
    Edits user based on the ID.
    """
    # Load existing data
    data = load_data()

	# Find a list with user that needs to be edited
    for user in data:
        if user["id"] == user_id:
            user.update(updated_data)
            break

	# Saves new data to the found list. It's not necessary to check if list was found because it's already done in other part of the code.
    save_data(data)
    print(f"User has been updated.\n")

def validate_nip(nip):
	nip = nip.replace('-', '')
	if len(nip) != 10 or not nip.isdigit():
		print("NIP is incorrect, try again.")
		return False
	digits = [int(digit) for digit in nip]
	weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
	is_last_number_valid = sum(digit1 * digit2 for digit1, digit2 in zip(digits, weights)) % 11
	return is_last_number_valid == digits[9]

def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        print("PESEL is incorrect, try again.")
        return False
    digits = [int(digit) for digit in pesel]
    is_month_valid = True if digits[2] in range(0,4) and digits[3] in range(0,10) else False # People born in 1900-2099 have number from 01 to 32
    if not is_month_valid:
        print("PESEL has incorrect month, try again.")
        return False
    day_number_one = str(digits[4])
    day_number_two = day_number_one + str(digits[5])
    day_number_two = int(day_number_two)
    is_day_valid = True if day_number_two in range(0,32) else False
    if not is_day_valid:
        print("PESEL has incorrect day, try again.")
        return False
    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    last_number = sum(digit1 * digit2 for digit1, digit2 in zip(digits, weights))
    if last_number > 9:
        last_number = str(last_number)
        last_number_digits = [last_number_digit for last_number_digit in last_number]
        last_number = 10 - int((last_number_digits[1]))
    else:
        last_number = 10 - last_number
    if last_number == digits[10]:
        return True
    else:
        print("Incorrect last digit, try again.")
        return False

def validate_regon(regon):
    pass

def generate_password():
    pass

def validate_password(password):
    pass

print("Welcome to the user registration!")
app_running = True
while app_running:
    option = input(f"What would you like to do?\n1. Register\n2. Edit user\n3. Remove user\n4. Load all users\n")

    if option == "1":
        user_data_list = {}
        user_data_list["id"] = 1
        user_data_list["username"] = input("Enter your full name: ")
        # NIP
        valid_nip = False
        while valid_nip == False:
            user_data_list["nip"] = input("Enter your NIP: ")
            valid_nip = validate_nip(user_data_list["nip"])
        # PESEL
        valid_pesel = False
        while valid_pesel == False:
            user_data_list["pesel"] = input("Enter your PESEL: ")
            valid_pesel = validate_pesel(user_data_list["pesel"])
        # REGON
        user_data_list["regon"] = input("Enter your Regon number: ")
        user_data_list["password"] = input("Create strong password: ")
        user_data_list["status"] = "Active"

        add_user(user_data_list)

    elif option == "2":
        data = load_data()
        login_username = check_user()

        password_correct = False
        while password_correct == False:
            password_count = 0
            login_password = input("Enter your password: ")
            for value in data:
                if value["username"] == login_username and value["password"] == login_password:
                    password_correct = True
                    password_count += 1
                    print("Login successful!")

                    edit_data = input("\nWhat you want to edit?\n1. Name\n2. NIP\n3. PESEL\n4. Regon\n5. Password\n")
                    if edit_data == "1":
                        new_username = input("Enter new name: ")
                        value["username"] = new_username
					# NIP
                    elif edit_data == "2":
                        valid_nip = False
                        while valid_nip == False:
                            new_nip = input("NIP: ")
                            valid_nip = validate_nip(new_nip)
                        value["nip"] = new_nip
					# PESEL
                    elif edit_data == "3":
                        new_pesel = input("Enter new PESEL: ")
                        value["pesel"] = new_pesel
                    elif edit_data == "4":
                        new_regon = input("Enter new Regon: ")
                        value["regon"] = new_regon
                    elif edit_data == "5":
                        new_password = input("Enter new password: ")
                        value["password"] = new_password

                    edit_user(value["id"], value)
                    break
            if password_count == 0:
                print("Incorrect password, try again.\n")

    elif option == "3":
        data = load_data()
        login_username = check_user()

        password_correct = False
        while password_correct == False:
            password_count = 0
            login_password = input("Enter your password: ")
            for value in data:
                if value["username"] == login_username and value["password"] == login_password:
                    password_correct = True
                    password_count += 1
                    print("Login successful!")

                    remove_user(value["id"])
                    break
            if password_count == 0:
                print("Incorrect password, try again.\n")

    elif option == "4":
        load_user()
