# storage 
contact = {}

while True: 
  print("Welcome to the Contact App")
  print("1. Add Contact")
  print("2. View Contacts") 
  print("3. Update Contact")
  print("4. Delete Contact")
  print("5. Exit")
  choice = input("Please choose an option (1-5): ")
  if choice == '1':
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact[name] = phone
    print(f"Contact {name} added successfully.")
  
  elif choice == '2':
    if not contact:
      print("No contacts available.")
    else:
      print("Contacts:")
      for name, phone in contact.items():
        print(f"{name}: {phone}")
  
  elif choice == '3':
    name = input("Enter the name of the contact to update: ")
    if name in contact:
      new_phone = input("Enter new phone number: ")
      contact[name] = new_phone
      print(f"Contact {name} updated successfully.")
    else:
      print(f"Contact {name} not found.")
  
  elif choice == '4':
    name = input("Enter the name of the contact to delete: ")
    if name in contact:
      del contact[name]
      print(f"Contact {name} deleted successfully.")
    else:
      print(f"Contact {name} not found.")
  
  elif choice == '5':
    print("Exiting the Contact App. Goodbye!")
    break
  
  else:
    print("Invalid option. Please try again.")