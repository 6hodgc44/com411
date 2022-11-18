import matplotlib.pyplot as chart
import random as rand


def data():
    paths = {}
    print("What kind of line would you like? (:, --, or -)")
    paths['line'] = input()
    print()
    print("What colour would you like? (r, g, or b)")
    paths['colour'] = input()
    print()
    print("What style of marker would you like? (o, s, or ^)")
    paths['style'] = input()
    return paths


def generate():
    print()
    print("How many lines would you like to display?")
    loops = int(input())
    counter = 0
    while counter <= loops:
        values = data()
        x = loops
        y = rand.randint
        chart.plot(loops, y, f"{values['colour']}{values['line']}{values['style']}")
        counter += 1
    chart.show()


def run():
    print()
    print("Running...")
    generate()
    print("Done!")


run()
