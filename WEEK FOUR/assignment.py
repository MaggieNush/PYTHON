# while True:
#     try:
#         filename = input("Enter the full path or name of the file: ") # Prompt user for file or path to the file
#         new_filename = input("Enter the new filename to save the output: ")

#         with open(filename, "r") as file:
#             data = file.read()  # Read the entire file

#             modified_data = "=== start of file ===\n" + data + "\n=== end of file ===" # Modify the content as needed

#         with open(new_filename, "w") as new_file:
#             new_file.write(modified_data) # Modify the content as needed
#             print(f"Modified content has been saved to {new_filename}")

#     except FileNotFoundError:
#         print("The file was not found. Please check the full path or file name and try again.")
#     except IOError:
#         print("An error occurred while trying to read or write to the file. Please try again.")


while True:
    try:
        filename = input("Enter the full path or name of the file: ")

        with open(filename, "r") as file:
            data = file.read()

        print("\nHow would you like to modify the file?")
        print("1. Uppercase everything")
        print("2. Lowercase everything")
        print("3. Add custom text at the beginning")
        print("4. Add custom text at the end")
        print("5. Replace a word")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            modified_data = data.upper()
        elif choice == "2":
            modified_data = data.lower()
        elif choice == "3":
            custom_text = input("Enter text to add at the beginning: ")
            modified_data = custom_text + "\n" + data
        elif choice == "4":
            custom_text = input("Enter text to add at the end: ")
            modified_data = data + "\n" + custom_text
        elif choice == "5":
            old_word = input("Enter word to replace: ")
            new_word = input("Enter new word: ")
            modified_data = data.replace(old_word, new_word)
        else:
            print("Invalid choice! No modifications made.")
            modified_data = data

        new_filename = input("Enter the new filename to save the output: ")

        with open(new_filename, "w") as new_file:
            new_file.write(modified_data)

        print(f"\nSuccess! Your modified content has been saved to {new_filename}")

        break  # Exit after success

    except FileNotFoundError:
        print("The file was not found. Please check the path or file name and try again.")
    except IOError:
        print("An error occurred while trying to read or write the file.")
