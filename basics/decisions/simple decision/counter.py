number_one = int(input("Please enter the first whole number: "))
number_two = int(input("Please enter the second whole number: "))
number_three = int(input("Please enter the third whole number: "))

even = 0
odd = 0

if number_one % 2 == 0:
    even += 1
else:
    odd += 1
if number_two % 2 == 0:
    even += 1
else:
    odd += 1
if number_three % 2 == 0:
    even += 1
else:
    odd += 1

print("You entered " + str(even) + " even numbers, and " + str(odd) + " odd numbers. ")
