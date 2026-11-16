import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 6:
    print("Password length must be atleast 6!")

else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nYour Generated Password")
    print(password)