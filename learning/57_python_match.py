# The match statement is used to perform different actions based on different conditions.
# The match expression is evaluated once.
# The value of the expression is compared with the values of each case.
# If there is a match, the associated block of code is executed.
day = 4
match day:
    case 1: 
        print("Monday")
    case 2:
        prnt("Tuesday")
    case 3:
        print("Wednesday")
    case 4: 
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("sunday")


# Default Value
# Use the underscore character _ as the last case value 
# if you want a code block to execute when there are not other matches

day1 = 4
match day1:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")