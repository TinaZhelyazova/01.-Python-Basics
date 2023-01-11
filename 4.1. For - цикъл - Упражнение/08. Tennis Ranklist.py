import math

number_of_games = int(input())
starting_points = int(input())
w = 0
f = 0
sf = 0

for i in range(number_of_games):
    stage = input()
    if stage == "W":
        w= w+1
    elif stage == "F":
        f = f+1
    elif stage == "SF":
        sf= sf+1

win_points = w*2000
finalist_points = f*1200
semifinalist_points = sf*720
all_points = win_points+finalist_points+semifinalist_points +starting_points
points_without_starting_points = win_points+finalist_points+semifinalist_points
average_points = points_without_starting_points/number_of_games
percentage_of_win_games = (w/number_of_games)*100

print(f"Final points: {all_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_of_win_games:.2f}%")