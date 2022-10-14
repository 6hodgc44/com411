number_one = int(input("Please input a whole number: "))
number_two = int(input("Please input a second whole number which is different from the first: "))
print()
if number_one > number_two:
    print("The first number is larger. ")
elif number_two > number_one:
    print("The second number is larger. ")
else:
    print("I said enter different numbers! These are the same number")
