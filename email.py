def emailValidation(email):
    if email[0].isalpha() and "@gmail.com" in email.lower() and email.lower().count("@gmail.com") == 1:
        print("Valid Email")
    else:
        print("Wrong Email")


# user = input("Enter user Email id: ")
# print(emailValidation(user))

# output
# Enter user Email id: rishi@gmail.com
# Valid Email
