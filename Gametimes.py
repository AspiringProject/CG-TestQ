minutesPlayed = [[60, 180, 200, 60, 100], [30, 60, 30, 10, 35], [45, 0, 0, 15, 30], [0, 60, 20, 15, 45]]

day = int(input("Enter the day of the week: "))

def dayOfWeek(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    else:
        return "Invalid day"
    
print(dayOfWeek(day))
