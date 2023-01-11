number_of_groups = int(input())
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
peak =""

for i in range(number_of_groups):
    people_in_each_group = int(input())
    if people_in_each_group >= 41:
        group5 = group5+people_in_each_group
        peak = "Eверест"
    elif people_in_each_group <= 5:
        group1 = group1+people_in_each_group
        peak = "Мусала"
    elif people_in_each_group== 6 or people_in_each_group<= 12:
        group2 = group2+people_in_each_group
        peak = "Монблан"
    elif people_in_each_group== 13 or people_in_each_group<=25:
        group3 = group3+people_in_each_group
        peak = "Килиманджаро"
    elif people_in_each_group== 26 or people_in_each_group<=40:
        group4 = group4+people_in_each_group
        peak = "K2"

all_people = group1+group2+group3+group4+group5

print(f"{(group1/all_people)*100:.2f}%")
print(f"{(group2/all_people)*100:.2f}%")
print(f"{(group3/all_people)*100:.2f}%")
print(f"{(group4/all_people)*100:.2f}%")
print(f"{(group5/all_people)*100:.2f}%")