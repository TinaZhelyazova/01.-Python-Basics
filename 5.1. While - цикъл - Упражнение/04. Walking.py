steps_per_walking = input()
steps_counter = 0
walking = True

while walking:
    if steps_per_walking == "Going home":
        steps_per_walking = input()
        steps_counter += int(steps_per_walking)
        if steps_counter >= 10000:
            steps_over = steps_counter - 10000
            print("Goal reached! Good job!")
            print(f"{steps_over} steps over the goal!")
            break
        elif steps_counter < 10000:
            steps_needed = 10000 - steps_counter
            print(f"{steps_needed} more steps to reach goal.")
            break
    steps_counter += int(steps_per_walking)

    if steps_counter >= 10000:
        steps_over = steps_counter - 10000
        print("Goal reached! Good job!")
        print(f"{steps_over} steps over the goal!")
        break

    steps_per_walking = input()
