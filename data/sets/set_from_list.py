def observed():
    observations = []
    ask = 0
    while ask <= 6:
        print("Please enter an observation:")
        observations.append(str(input()))
        print()
        ask += 1
    return observations


def run():
    print("Counting Observations...")
    list_observed = observed()
    list_set = set()

    for i in list_observed:
        tup = (i, list_observed.count(i))
        list_set.add(tup)

    for item in list_set:
        print(f"{item[0]} was observed {item[1]} times")


run()
