hours = int(input())
minutes = int(input())

hours_in_minutes = hours*60
all_minutes = hours_in_minutes+minutes + 15

hours_after = all_minutes//60
minutes_after = all_minutes%60

if hours_after==24:
    hours_after =0

print(f"{hours_after}:{minutes_after:02d}")


