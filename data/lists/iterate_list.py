def direction():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    directions = direction()
    for items in range(len(directions)):
        directions = directions[items]
        print(f" {items}: {directions}")


menu()
