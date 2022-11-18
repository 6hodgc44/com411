import matplotlib.pyplot as square


def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    square.plot(x, y, 'ro:')


def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    square.plot(x, y, 'gs--')


def large():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]
    square.plot(x, y, 'pb-')
    square.show()


small()
medium()
large()