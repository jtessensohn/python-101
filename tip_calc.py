while True:
    try:
        total = int(input('Total bill amount? $'))
        level = input('Level of service? (good, fair, bad) ')
        if level == "good":
            print("$" + str(total + (total *.20)))
        if level == "fair":
            print("$" + str(total + (total *.15)))
        if level == "bad":
            print("$" + str(total + (total *.10)))
    except ValueError:
        print("Please rate based on what is in the parentheses")

    
    
