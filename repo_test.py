print("Hello, and welcome to the best shop in town. ")
print()
name = input("What's your name stranger? ")
if name == "Chris":
    print("Oh, I'm Chris too! ")
print("Nice to meet you", name)
item_needed = input("What can I get you today? We have Oranges, Apples, and Strawberries. ")
if item_needed == "Oranges" or "An Orange" or "an orange" or "an Orange" or "oranges":
    print("They're too bitter for my liking. ")

elif item_needed == "Strawberries" or "strawberries" or "strawberries please" or "Strawberries please":
    print("They're my favorite! ")
else:
    print("I do like those. ")

#A simple counter:

even_counter = 0
odd_counter = 0

choice_one = int(input("please enter a number"))
choice_two = int(input("please enter another number"))
choice_three = int(input("please enter a third number"))

if choice_one % 2 == 0:
    even_counter += 1
else:
    odd_counter += 1

if choice_two % 2 == 0:
    even_counter += 1
else:
    odd_counter += 1

if choice_three % 2 == 0:
    even_counter += 1
else:
    odd_counter += 1

if even_counter != 1 and if odd_counter != 1:
        print(f"You chose {even_counter} even numbers, and {odd_counter} odd numbers.")

#Result is that the variables get numbers added to them as the if statements find the odd and even numbers.
