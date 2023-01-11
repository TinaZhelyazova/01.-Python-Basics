

name = input()
starting_points= float(input())
raters = int(input())
end_points=0
points=0

for i in range(1,raters+1):
    name_of_rater = input()
    points_from_rater = float(input())
    chars_in_name_of_rater = float(len(name_of_rater))
    if i==1:
        points = starting_points+(chars_in_name_of_rater*points_from_rater)/2
        end_points=points
    else:
        points = end_points + (chars_in_name_of_rater * points_from_rater) / 2
        end_points = points
    if end_points>1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {end_points:.1f}!")
        break

if end_points<1250.5:
    points_needed = 1250.5 - end_points
    print(f"Sorry, {name} you need {points_needed:.1f} more!")

