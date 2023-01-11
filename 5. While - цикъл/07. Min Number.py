import sys

command = input()
min_number = sys.maxsize
curr_min_num =0
while command != "Stop":

    if command == "Stop":
        break
    elif int(command) < min_number:
        min_number = int(command)
        curr_min_num = int(min_number)
    command = input()

print(curr_min_num)