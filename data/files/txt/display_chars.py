def display_line():
    with open('library.txt') as file:
        number = file.readline()
        print(number)

def display_chars():
    with open('library.txt') as file:
        number = file.read(5)
        for character in number:
            print(character, end = '')

def full_text():
    with open('library.txt') as file:
        text = file.read()
        print(text)

print("The first 5 characters are: ")

display_chars()

print("\n")
print("The first line is: ")

display_line()

print()
print("The full text is: ")

full_text()

