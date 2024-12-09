# Tutorial: User Management System - `user_management.py`

## Functions:
- `add_user(user_data)`: Adds new user.
User is asked to provide full name, nip, pesel and regon numbers. After that, user is asked either to create a random generated password or to create a new one by himself. If any number or password doesn't match the correct criteria, it is immediately reported and asks user to retry the input. At the end, it automatically sets next ID number and status to "Active" and saves user to the users.json file if exists. If the file doesn't exists, it creates a new one.

- `remove_user(user_id)`: Deletes existing user.
User is asked to enter a username and a password. Additional function `check_user()` asks user to input a username. If username exists, it asks user to input a password. If username and password are matching the same registered user, it changed user status to "Inactive".

- `edit_user(user_id, updated_data)`: Edits users data.
User is again asked to enter username and password. If both are correct, then user is asked which value he wants to change. If user will choose to change password, he's once again asked to generate a random password or to provide a new one by himself. All validations are the same as in `add_user` function.

- `validate_nip(nip)`: Validates NIP number.
Checks if the provided NIP number is 10 digits long and if is made fully of the integer digits (0, 1, 2, etc.). If not, it returns an error and asks user to input NIP again. Then it checks if the last number (the control number) is correctly calculated based on an algorithm that's supposed to check if the control number is valid.

- `validate_pesel(pesel)`: Validates PESEL number.
Same rules as for the NIP validation but with PESEL requirements. So it needs to be 11-digit number with pre-set criterias such as correct first 6 numbers (year-month-day) and the control number.

- `validate_regon(regon)`: Validates REGON number.
Checks if REGON has 9 or 14 digits and is a number. Then it checks first 2 digits (voivodeship number) and calculates if the control number is correct.

- `generate_password()`: Randomly generates strong password.
New password is at least 12 digits long, contains from 3 to 5 small and large letters, from 2 to 3 symbols and from 3 to 4 numbers. Then prints that password to the user.

- `validate_password(password)`: Validates strength of a password.
Checks if password is at least 12 digits long, contains at least 1 small and large letter, at least 1 symbol and at least 1 number. If not, the user is asked to create password again.

### Additional functions:
- `load_user()`: Prints out list of all registered users.

- `load_data()`: Additional function to load all data from the .json file, important to speed up the process of registering user, deleting and editing users.

- `save_data(data)`: Similar to load_data(), saves the provided data into .json file if the user was created, edited or removed.

## Suggestions:
- I'd suggest to later add a password encryption to safely store users passwords, as well as the PESEL numbers so they shouldn't be visible in the .json file as a normal values.
- If possible, it could be good to check if provided nip, pesel and regon exists and are registered.