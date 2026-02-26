# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime
import time

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # TODO: Create a contact dictionary with all fields
    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: Append to contacts list
    # TODO: Return the new contact
    createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    contact = {
        'name' : name,
        'phone' : phone,
        'email' : email,
        'category' : category,
        'created_at': createdAt
    }
    contacts.append(contact)
    return contact


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts): # Make the output more pretty before turning it in
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    print("="*45)
    print(" "*12 + f"CONTACT BOOK ({len(contacts)} contacts)")
    print("="*45)
    # TODO: Print table headers
    print("#, Name, Phone, Email, Category, Added")
    # TODO: Loop through contacts and print each row
    for i in range(len(contacts)):
        print(f"{i}, {contacts[i]['name']}, {contacts[i]['phone']}, {contacts[i]['email']}, {contacts[i]['category']}, {contacts[i]['created_at']}")
    # TODO: Print footer
    print("="*45)

def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details
    print("--- CONTACT DETAILS ---")
    print("Name: " + contact['name'])
    print("Phone: " + contact['phone'])
    print("Email: " + contact['email'])
    print("Category: " + contact['category'])
    print("Added: " + contact['created_at'])
    print("-"*24)


# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()
    return [contact for contact in contacts if query.lower() in contact['name'].lower()]


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    # I added in the .lower() for safety measure
    return [contact for contact in contacts if contact['category'].lower() == category.lower()]


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    success = [contact for contact in contacts if contact['phone'] == phone]
    if(len(success) == 1):
        return success[0]
    else:
        return None


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    # TODO: Find contact by phone
    contact = find_by_phone(contacts, phone)
    # TODO: Update the specified field
    # TODO: Return success/failure
    if(contact == None):
        return False
    
    contact[field] = new_value
    return True


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    # Look for contact
    contact = find_by_phone(contacts, phone)

    # Check if they do not exist
    if(contact == None):
        return False # Return False. Cannot delete a non-existent contact
    
    # Contact Exists. Proceed to delete them
    contacts.remove(contact)
    return True # Return True. Successfully deleted contact


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    print("--- Contact Book Statistics ---")

    # TODO: Count total contacts
    print(f"Total Contacts: {len(contacts)}")

    # TODO: Count contacts by category
    print("By Category:")
    print(f"  - Friends: {len(filter_by_category(contacts, 'friends'))}")
    print(f"  - Family: {len(filter_by_category(contacts, 'family'))}")
    print(f"  - Work: {len(filter_by_category(contacts, 'work'))}")
    print(f"  - Other: {len(filter_by_category(contacts, 'other'))}")
    
    # TODO: Find most recently added contact
    index = 0
    mostRecent = datetime.strptime(contacts[0]['created_at'], "%Y-%m-%d %H:%M:%S")
    for i in range(len(contacts)):
        added = datetime.strptime(contacts[i]['created_at'], "%Y-%m-%d %H:%M:%S")
        if(added > mostRecent):
            mostRecent = added
            index = i
    print(f"Most Recent: {contacts[i]['name']} (added {contacts[i]['created_at']})")


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    display_menu()
    choice = int(input("Make your choice: "))
    while(choice > 0 and choice < 7):
        if(choice == 1):
            display_all_contacts(contacts)
        elif(choice == 2):
            name = input("Enter a name for the contact: ")
            phone = input("Enter the contact's phone number in the form of 000-000-0000: ")
            email = input("Enter the contact's email address: ")
            category = input("Category (friends, family, work, or other) this contact falls under: ")
            add_contact(contacts, name, phone, email, category)
        elif(choice == 3):
            results = []
            searchMethod = input("What do you want to search by (name, category, phone)? ")
            if(searchMethod == 'name'):
                query = input("Enter a name or part of a name to search for: ")
                results = search_by_name(contacts, query)
            elif(searchMethod == 'category'):
                filter = input("Enter the category (friends, family, work, or other) you want to filter for: ")
                results = filter_by_category(contacts, filter)
            elif(searchMethod == 'phone'):
                phoneNum = input("Enter a phone number in the form of 000-000-0000: ")
                results = find_by_phone(contacts, phoneNum)
            if(len(results == 0)):
                print("No contacts found based on the given search criteria.")
            elif(len(results == 1)): # Check type and flip with conditional above it
                display_contact_details(results[0])
            else:
                display_all_contacts(results)
        elif(choice == 4):
            phoneNum = input("Enter the contact's phone number in the form of 000-000-0000: ")
            field = input("Enter the column to update: ")
            value = input("Enter information to update: ")
            update_contact(contacts, phoneNum, field, value)
        elif(choice == 5):
            phoneNum = input("Enter the contact's phone number in the form of 000-000-0000: ")
            delete_contact(contacts, phoneNum)
        elif(choice == 6):
            display_statistics(contacts)
        elif(choice == 0):
            exit()
        else:
            print("Not a valid choice.")

        choice = int(input("Make your choice: "))


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    # TODO: Add at least 5 sample contacts
    # add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Isabelle Smart", "773-202-6382", "notrealemail@email.com", "other")
    add_contact(contacts, "Alice Smart", "667-098-4732", "ohmeohmy@email.com", "family")
    add_contact(contacts, "Carlos Aesron", "703-735-1833", "superyippee@email.com", "work")
    add_contact(contacts, "Fang Lin", "554-397-0122", "forestdweller@email.com", "friends")
    time.sleep(5)
    add_contact(contacts, "Yangjin Shao", "370-229-7834", "outofideas@email.com", "friends")
    
    # TODO: Test your functions
    # display_all_contacts(contacts)
    # results = search_by_name(contacts, "alice")
    # etc.
    display_all_contacts(contacts)

    results = search_by_name(contacts, "Lin")
    display_all_contacts(results)
    display_contact_details(results[0])
    results = search_by_name(contacts, "i")
    display_all_contacts(results)

    display_statistics(contacts) # Proves filter_by_category(contacts, category) works

    delete_contact(contacts, "703-735-1833") # Proves find_by_phone(contacts, phone) works
    display_all_contacts(contacts)

    
    # STRETCH: Uncomment to run interactive menu
    # main()
