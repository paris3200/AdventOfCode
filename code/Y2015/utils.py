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
    """Returns each line in a file as a list item, including new line characters."""
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


class Grid:
    """
    A 2D grid that uses x for the horizontal dimensions and y for the vertical dimenions.
    """

    def __init__(self, x: int, y: int, default_value: int = 0):
        """Creates a grid starting with dimensions of x and y.

        Paramaters
        ----------
        x: int
            Size in horizontal direction.
        y: int
            Size in vertical direction.
        default_value: int
            Default status for each point.
        """
        self.grid = [[default_value for y in range(y+1)] for x in range(x+1)]
        self.max_x = x
        self.max_y = x

    def turn_on_point(self, x: int, y: int) -> None:
        """Sets the point x,y to 1 to signify on.

        Paramaters
        ----------
        x: int
            X value of point
        y: int
            Y value of point
        """
        self.grid[y][x] = 1

    def turn_off_point(self, x: int, y: int) -> None:
        """Sets the point x,y to 0 to signify off.

        Paramaters
        ----------
        x: int
            X value of point
        y: int
            Y value of point
        """
        self.grid[y][x] = 0

    def toggle_point(self, x: int, y: int) -> None:
        """Switches the point x,y from 1 to 0 or from 0 to 1.

        Paramaters
        ----------
        x: int
            X value of point
        y: int
            Y value of point
        """
        if self.grid[y][x] == 0:
            self.turn_on_point(x, y)
        else:
            self.turn_off_point(x, y)

    def increase_point(self, x: int, y: int, increase: int = 1) -> None:
        """Sets the point x,y to 1 to signify on.

        Paramaters
        ----------
        x: int
            X value of point
        y: int
            Y value of point
        increase: int
            Amount to add to the point.  Default=1
        """
        self.grid[y][x] += increase

    def stats(self) -> dict:
        """Returns a dict containing the number of gird points turned on and turned off."""
        status = {"total_value_on": 0, "on": 0, "off": 0}
        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x + 1):
                if self.grid[y][x] == 0:
                    status["off"] += 1
                else:
                    status["on"] += 1
                    status["total_value_on"] += self.grid[y][x]
        return status

    def __repr__(self):
        grid_str = ""
        for y in range(0, self.max_y + 1):
            grid_str += f"{self.grid[y]}\n"
        return grid_str
