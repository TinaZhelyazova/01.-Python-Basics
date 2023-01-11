record_in_seconds = float(input())
meters_swim = float(input())
seconds_per_meter_swim = float(input())

ivans_record = seconds_per_meter_swim*meters_swim

how_many_delays = meters_swim//15
ivans_record_with_delays = ivans_record+how_many_delays*12.5

if ivans_record_with_delays<record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {ivans_record_with_delays:.2f} seconds.")
else:
    seconds_needed = ivans_record_with_delays-record_in_seconds
    print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")