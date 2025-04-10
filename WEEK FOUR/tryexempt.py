try:
    with open('sample.txt', 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file was not found. Please check the file name and try again.")
finally:
    print("Execution terminated.")