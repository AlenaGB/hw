second = int (input("What is the time in second? "))

hours = second//3600
minutes = (second - 3600)//60
second = second - (hours*3600+minutes*60)

print(f"Time {hours}:{minutes}:{second}")