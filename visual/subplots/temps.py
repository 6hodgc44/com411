import matplotlib.pyplot as plt

def read_data(txt):
    with open(txt, 'r') as file:
        data = []
        for line in file:
            data.append(int(line.strip()))
        return(data)


def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplots(1, 2)

    axs[0].plot(data)
    axs[1].bar(data)

    plt.show()

run()