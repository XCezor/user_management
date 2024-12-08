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

	# Find a list with user that needs to be edited
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

	# Saves new date to the found list. It's not necessary to check if list was found because it's already done in other part of the code.
    save_data(data)
    print(f"User has been updated.\n")

def validate_nip(nip):
    pass

def validate_pesel(pesel):
    pass

def validate_regon(regon):
    pass

def generate_password():
    pass

def validate_password(password):
    pass

print("Welcome to the user registration!")
app_running = True
while app_running:
	option = input(f"What would you like to do?\n1. Register\n2. Edit user\n3. Remove user\n")

	if option == "1":
		user_data_list = {}
		user_data_list["id"] = 1
		user_data_list["username"] = input("Enter your full name: ")
		user_data_list["nip"] = input("Enter your NIP: ")
		user_data_list["pesel"] = input("Enter your PESEL: ")
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
					elif edit_data == "2":
						new_nip = input("Enter new NIP: ")
						value["nip"] = new_nip
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
