#ASSIGNMENT 2
# ABMI/08305P/2023- MAGHANGA ROSINAH WAKIO
# ABMI/- SERAH NJOKI
# ABMI/ - JOY KIMATHI

password ="admin123"
attempts = 0

while attempts <3:

    password_entered = input("Enter password :")

    if password_entered == password==password:
        print("Login successful")

        marks= int(input("Enter marks (0-100) :"))
        if marks>=80 and marks<=100:
            print("Grade: A")
        elif marks>=70:
            print("Grade: B")
        elif marks >=41:
            print("Grade: C")
        elif marks >=30:
            print("Grade: D")
        elif marks>=0:
                print("Grade: F")

        else:
            print("Invalid marks")

            break
    else:
        attempts += 1
        print("Incorrect password.")

        if attempts==3:
            print("Login failed")


