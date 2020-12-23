currentKm = float(input("How many kilometers did you run on the first day? "))
finalKm = float(input("Set a goal "))
day = 1
if currentKm == 0:
    print("Try better!")
else:
    while currentKm <= finalKm:
        currentKm = currentKm+currentKm*0.1
        day += 1
    print(f"Great! You have reached the goal in {day} days")
