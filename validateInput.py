while True:
    print("Please enter your age: ", end='')
    age = input()
    if (age.isdecimal()):
        print("You will be " + str(int(age) + 5) + " in five years from now :O")
        break
    print("Please enter a number, God damn it")

while True:
    print("Please enter your password (letters and numbers only): ", end='')
    password = input()
    if (password.isalnum()):
        starpass = "";
        for i in range(len(password)):
            starpass = starpass + "*"
        print("Your password is " + starpass + ", censored")
        break
    print("Passwords can only have letters and numbers.")
