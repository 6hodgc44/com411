def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    movement_function = movements()
    print(f"""{movement_function[0]} for {movement_function[1]} steps
{movement_function[2]} for {movement_function[3]} steps
{movement_function[4]} for {movement_function[5]} steps
{movement_function[6]} for {movement_function[7]} steps""")
# the above print function is part of the run function


run()
