width = int(input())
length = int(input())
height = int(input())
number_of_boxes = input()
space = width*length*height
boxes_counter = 0

while True:
    if number_of_boxes == "Done":
        print(f"{space} Cubic meters left.")
        break
    space -= int(number_of_boxes)
    boxes_counter += int(number_of_boxes)
    if space <= 0:
        #meters_needed = space - boxes_counter
        print(f"No more free space! You need {abs(space)} Cubic meters more.")
        break
    number_of_boxes = input()
