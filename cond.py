
while True:
    try:
        student = int(input("Fill in your marks: "))
        if 0 <= student <= 100:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

grade = student
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
elif grade >= 50:
    print("Grade: E")
else:
    print("Grade: F")


