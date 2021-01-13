total = int(input('Total bill amount? $'))
level = str(input('Level of service? (good, fair, bad) '))
if level == "good":
    print("$" + str(total + (total *.20)))
if level == "fair":
    print("$" + str(total + (total *.15)))
if level == "bad":
    print("$" + str(total + (total *.10)))
else:
    print("Please try again.")