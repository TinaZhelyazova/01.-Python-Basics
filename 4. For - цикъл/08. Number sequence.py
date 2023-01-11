import sys

numbers = int(input())

#-922337203684775807
max_num= -sys.maxsize

#922337203684775807
min_num = sys.maxsize

for i in range (numbers):
    curr_num=int(input())

    if curr_num>max_num:
        max_num=curr_num
    if curr_num<min_num:
        min_num=curr_num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")