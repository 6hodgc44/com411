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
