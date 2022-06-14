import matplotlib.pyplot as plt


def read_file(filename, datatype):
    with open(filename, "r") as procedure:

        if datatype == "list":
            code = []
            for line in procedure:
                data = line.strip().split(",")
                for num in data:
                    code.append(int(num))

            return code


def read_lines(filename):
    """Returns an array with each line in filename as array item"""
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


def list_from_string(text):
    text = text.strip()
    return list(text.split(","))


def plotter(coordinates):
    # plt.plot(coordinates)
    plt.scatter(*zip(*coordinates), marker="_")
    plt.show()
