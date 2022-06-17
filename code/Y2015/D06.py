if __name__ != "__main__":
    from Y2015 import utils
else:
    import utils


class Grid:
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
        self.grid = [[0 for y in range(y)] for x in range(x)]
        self.max_x = x - 1
        self.max_y = x - 1

    def turn_on_point(self, x: int, y: int) -> None:
        """Sets the point x,y to 1 to signify on.

        Paramaters
        ----------
        x: int
            X value of point
        y: int
            Y value of point
        """
        self.grid[x][y] = 1

    def turn_off_point(self, x: int, y: int) -> None:
        """Sets the point x,y to 0 to signify off.

        Paramaters
        ----------
        x: int
            X value of point
        y: int
            Y value of point
        """
        self.grid[x][y] = 0

    def toggle_point(self, x: int, y: int) -> None:
        """Switches the point x,y from 1 to 0 or from 0 to 1.

        Paramaters
        ----------
        x: int
            X value of point
        y: int
            Y value of point
        """
        if self.grid[x][y] == 0:
            self.turn_on_point(x, y)
        else:
            self.turn_off_point(x, y)

    def switch_range(
        self, x_start: int, y_start: int, x_end: int, y_end: int, action: str
    ) -> None:
        """Turns on points in a rectangle with the top most being defined by x_start, y_start and the bottom right being x_end, y_end.

        Paramaters
        ----------
        x_start: int
            X value of top left point
        y_start: int
            Y value of top left point
        x_end: int
            X value of bottom right point
        y_end: int
            Y value of bottom right point
        action: str
            Action to preform on the point(on, off, toggle)
        """
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                if action == "on":
                    self.turn_on_point(x, y)
                elif action == "off":
                    self.turn_off_point(x, y)
                elif action == "toggle":
                    self.toggle_point(x, y)

    def stats(self) -> dict:
        """Returns a dict containing the number of gird points turned on and turned off."""
        status = {"on": 0, "off": 0}
        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x + 1):
                if self.grid[x][y] == 0:
                    status["off"] += 1
                else:
                    status["on"] += 1
        return status


def process_instruction(instruction) -> dict:
    """turn off 660,55 through 986,197"""


def part_one(data):
    grid = Grid(1000, 1000)


def part_two(data):
    pass


if __name__ == "__main__":
    data = "../data/06.data"
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
