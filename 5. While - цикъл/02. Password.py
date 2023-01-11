username = input()
user_pass = input()
input_pass = input()

while input_pass != user_pass:
    input_pass = input()

print(f"Welcome {username}!")
