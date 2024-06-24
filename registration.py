from database import add_user, verify_user

def register_user():
    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")

        if password1 == password2:
            if add_user(first_name, last_name, email, password1):
                print("You have successfully created an account.")
                break
            else:
                print("Error: This email is already registered.")
        else:
            print("Your passwords must match.")

def login_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user = verify_user(email, password)
    if user:
        print("Login successful.")
        return user
    else:
        print("Invalid email or password.")
        return None
