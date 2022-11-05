def get_direction():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    directions = get_direction()
    for items in range(len(directions)):
        direction = directions[items]  # 'direction' vs 'directions'
        print(f" {items}: {direction}")


menu()
