import sys

command = input()
max_number = -sys.maxsize
curr_max_num =0
while command != "Stop":

    if command == "Stop":
        break
    elif int(command) > max_number:
        max_number = int(command)
        curr_max_num = int(max_number)
    command = input()

print(curr_max_num)