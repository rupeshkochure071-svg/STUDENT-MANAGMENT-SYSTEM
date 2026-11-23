
print("================================")
print("     STUDENT MANAGEMENT SYSTEM")
print("================================")

while True:

    print("\n1. Add Student")
    print("2. View Student")
    print("3. Exit")
    print("4. Search Student")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter Student Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter your Marks: "))

        percentage = (marks / 100) * 100

        print("Percentage:", percentage, "%")

        with open("student.txt", "a") as file:
            file.write(
                f"Name: {name}, Roll Number: {roll_no}, "
                f"Marks: {marks}, Percentage: {percentage}%\n"
            )

        print("Student added successfully!")

    # View Student
    elif choice == "2":

        print("\n----- Student Records -----")

        try:
            with open("student.txt", "r") as file:
                data = file.readlines()

                if not data:
                    print("No student records found.")

                for student in data:
                    if student.strip():
                        print(student.strip())

        except FileNotFoundError:
            print("No student records found.")

    # Exit
    elif choice == "3":

        print("Thank you!")
        break

    # Search Student
    elif choice == "4":

        search_roll = input("Enter Roll Number to search: ").strip()
        found = False

        try:
            with open("student.txt", "r") as file:

                for student in file:

                    if not student.strip():
                        continue

                    data = student.strip().split(", ")

                    if len(data) < 4:
                        continue

                    roll = data[1].split(":", 1)[1].strip()

                    if roll == search_roll:

                        print("\nStudent Found!")
                        print(data[0])
                        print(data[1])
                        print(data[2])
                        print(data[3])

                        found = True
                        break

            if not found:
                print("Student not found.")

        except FileNotFoundError:
            print("Student file does not exist.")

    else:
        print("Invalid choice!")
