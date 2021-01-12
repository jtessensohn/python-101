day = int(input('Day (0-6)? '))
if day == 0:
    print("Sunday")
if day == 1:
    print("Monday")
if day == 2:
    print("Tuesday")
if day == 3:
    print("Wednesday")
if day == 4:
    print("Thursday")
if day == 5:
    print("Friday")
if day == 6:
    print("Saturday")

if day > 6:
    print("I don't know what sort of week you have, but I know a good place to vacation!")