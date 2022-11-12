def observed():
    # List is created:
    observations = []
    # Counter is created:
    x = 0
    while x <= 4:
        print("Please enter an observation:")
        # Add the input to the list:
        observations.append(input())
        # Add one to the counter
        x += 1
    return observations


def remove_observations():
    # Return observations list into this function
    observations = observed()
    # Create counter for loop
    items = 0
    while items <= 4:
        print("Would you like to remove an observation (y/n)")
        to_remove = input()
        if to_remove == "y":
            print("Which item would you like to remove?")
            # Remove item from list
            observations.remove(input())
            print("Done!")
        else:
            items = 5
        # Add one to counter
        items += 1
    # Convert list to set to condense list to (item, number of said item) format
    item_set = set()
    for i in observations:
        # Create a tuple from the list to be inserted into newly created set
        tup = (i, observations.count(i))
        item_set.add(tup)

    for i in item_set:
        # Print out how many of each item there are in the set entries
        print(f"{i[0]} were observed {i[1]} times.")


remove_observations()
