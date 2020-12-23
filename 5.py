gain = float(input("What is the revenue this month? $"))
costs = float(input("What is the monthly expenses? $"))

if gain == costs:
    print ("Not bad. No losses this month")
elif gain < costs:
    print("It's time to think seriosly about cutting costs")
else:
    print("Great! This month you have a profit")
    staff = int(input("How many employees do you have?"))
    profit = (gain - costs)/staff
    print ("Your profit is ${:.2f} per person".format(profit))