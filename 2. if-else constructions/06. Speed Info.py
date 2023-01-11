speed = float(input())

if 150<speed <=1000:
    print("ultra fast")
elif 50< speed <=150:
    print("fast")
elif 10<speed <= 50:
    print("average")
elif speed<=10:
    print("slow")
else:
    print("extremely fast")