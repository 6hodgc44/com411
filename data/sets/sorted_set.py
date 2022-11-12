def observed():
    observations = []
    x = 0
    while x <= 4:
        print("Please enter an observation:")
        observations.append(input())
        x += 1
    return observations
    # to test list creation:
    # print(observations)


def remove_observations():
    observations = observed()
    items = 0
    while items <= 4:
        print("Would you like to remove an observation (y/n)")
        to_remove = input()
        if to_remove == "y":
            print("Which item would you like to remove?")
            observations.remove(input())
            print("Done!")
        else:
            items = 5

        items += 1
    item_set = set()
    for i in observations:
        tup = (i, observations.count(i))
        item_set.add(tup)

    for i in item_set:
        print(f"{i[0]} were observed {i[1]} times.")


remove_observations()
