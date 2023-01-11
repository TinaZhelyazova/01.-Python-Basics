length = int(input())
width = int(input())
height=int(input())
percentage = float(input())
area = length*width*height
litters = area*0.001
occupied_area = percentage/100
area_for_water = litters*(1-occupied_area)
print(area_for_water)
