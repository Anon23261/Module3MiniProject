# Module3MiniProject
Project

# Contact Management System

## Explanation of the Code:

- **Imports Required Libraries**: 
  - Uses the `json` library for reading and writing contact data to files.
  - Uses the `re` library for validating phone numbers and email addresses.

- **Defines the `contacts` Dictionary**:
  - This dictionary is used to store contact information, where each contact's phone number is the key, and details like name, email, and additional information are stored in nested dictionaries.

- **Function Definitions**:
  - `display_welcome_message()`: Prints a welcome message to the user.
  - `display_menu()`: Shows the menu options to the user.
  - `validate_phone(phone)`: Checks if the provided phone number is in the correct format.
  - `validate_email(email)`: Checks if the provided email address is in the correct format.
  - `add_contact()`: Prompts the user to enter contact details and adds them to the `contacts` dictionary.
  - `edit_contact()`: Allows the user to modify the details of an existing contact.
  - `delete_contact()`: Removes a contact from the `contacts` dictionary.
  - `search_contact()`: Finds and displays a contact's details using their phone number.
  - `display_all_contacts()`: Lists all contacts stored in the system.
  - `export_contacts()`: Saves all contacts to a specified JSON file.
  - `import_contacts()`: Loads contacts from a specified JSON file and adds them to the system.

- **Main Program Execution**:
  - The program checks if it is being run as the main module and starts the main loop.
  - Displays the welcome message and presents the menu options.
  - Waits for the user to select an option and calls the appropriate function based on the user's choice.

## Expected Outcome:
When you run the script, it will display a welcome message and a menu of options. You can add, edit, delete, search for contacts, and import/export contact data. If you enter invalid input, appropriate error messages will be shown.


