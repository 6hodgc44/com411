def observed():
    observations = []
    ask = 0
    while ask <= 6:
        print("Please enter an observation:\n")
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
    loop = 0

# Need to finish. Needs to print out: There were x number of item y and x number of item b etc. Use a loop with print statements

#    for x in list_set:
#       print(f"There were {})

run()