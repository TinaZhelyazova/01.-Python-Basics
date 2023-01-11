
first = int(input())
second = int(input())
third = int(input())

all_seconds = first+second+third
minutes = int(all_seconds/60)
seconds_left = all_seconds - (minutes*60)

if seconds_left<10:
    print(f"{minutes}:0{seconds_left}")
else:
    print(f"{minutes}:{seconds_left}")