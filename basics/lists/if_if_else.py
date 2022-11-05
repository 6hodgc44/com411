print("Hello, welcome to WHSmith.")
print()
print("What is your name?")
name = input()

if name == "Lee":
    print("Are you evil?")
    if input() == "yes":
        print("Be gone with you!")
        exit()
    else:
        print(f"Great to have you in the shop today {name}.")
else:
    print(f"Good to have you in the shop today {name}.")


def menu():
    print()
    print("Here is today's menu:")
    print("")
    print("McMuffin")
    print("Breakfast Roll")
    print("Steak Pie")
    print("Fish & Chips")
    print()
    print("Please select an option from the menu above")


menu()
option = input()
print()
print(f"""Thanks for your custom {name}, is there anything else you'd like, or is it just the {option}?
Here's the menu again:""")
menu()
option2 = input()
print()
if option2 == "McMuffin" or option2 == "Breakfast Roll" or option2 == "Steak Pie" or option2 == "Fish & Chips":
    if option2 == option:
        if option2 != "Fish & Chips":
            print("Thanks, your two " + option + "s are coming right up!")
        else:
            print(f"Thanks, your two {option} are coming right up!")
    else:
        print(f"Thanks, your {option}, and your {option2} are coming right up!")
else:
    print(f"Okay, just the one meal. Your {option} is coming right up!")
