import math
serial_name = input()
serial_duration = int(input())
break_duration = int(input())

time_for_lunch =(1/8)*break_duration
time_for_break =(1/4)*break_duration
time_for_serial = break_duration-(time_for_lunch+time_for_break)

if time_for_serial >=serial_duration:
    time_left = math.ceil(time_for_serial-serial_duration)
    print(f"You have enough time to watch {serial_name} and left with {time_left} minutes free time.")
else:
    time_needed = math.ceil(serial_duration - time_for_serial)
    print(f"You don't have enough time to watch {serial_name}, you need {time_needed} more minutes.")