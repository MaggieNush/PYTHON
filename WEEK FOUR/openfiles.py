# with open("WEEK FOUR/example.txt", "r") as file:
#     # Read the entire file
#     content = file.read()
#     print(content)


#     with open("WEEK FOUR/example.txt", "r") as file:
#         # Read the first line
#         first_line = file.readline()
#         print(first_line)

with open("WEEK FOUR/input.txt", "r") as file:
    # Read the first 5 characters
        content = file.read()  # Read the entire file
        count = len(content.split())  # Count the number of words
        converted = content.upper()  # Convert the content to uppercase
        print(converted)

# with open("WEEK FOUR/output.txt", "w") as file: file.write(output.txt)
with open("WEEK FOUR/output.txt", "w") as file:
    file.write(f"Processed Text:\n{converted}\n\nWord Count: {count}")  # Write the processed text and word count to the output file
    print("File successfully written to output.txt")
 # Print the uppercase content
        