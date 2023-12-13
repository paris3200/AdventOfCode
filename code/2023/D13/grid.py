
class Grid:
    """
    A 2D grid that uses x for the horizontal dimensions and y for the vertical dimenions.
    """

    def __init__(self, x: int, y: int, default_value: str = "."):
        """
        Creates a grid starting with dimensions of x and y.

        Paramaters
        ----------
        x: int
            Size in horizontal direction.
        y: int
            Size in vertical direction.
        default_value: str
            Default value for each point.
        """
        self.grid = [[default_value for x in range(x)] for y in range(y)]
        self.max_x = x
        self.max_y = y

    def set_point(self, x: int, y: int, value: str) -> None:
        """Sets the point at location x,y to value.

        Paramaters
        ----------
        x: int
            horizontal position of point
        y: int
            vertical position of point
        value: str
            Value of point
        """
        self.grid[y][x] = value

    def get_point(self, x: int, y: int) -> str:
        """Get the point value at location x,y.

        Paramaters
        ----------
        x: int
            horizontal position of point
        y: int
            vertical position of point

        Returns
        -------
        int: Value of point at [x, y]
        """
        return self.grid[y][x]

    def get_row(self, y) -> str:
        """
        Get the row as a string.

        Returns
        -------
        list: Coordinates of starting point [x, y]
        """
        row = []
        for char in self.grid[y]:
            row.append(char)
        return "".join(row)

    def get_column(self, x) -> str:
        column = []
        for y in range(0, self.max_y):
            column.append(self.grid[y][x])
        return "".join(column)

    def __repr__(self):
        grid_str = ""
        for y in range(0, self.max_y):
            line = " ".join(self.grid[y])
            grid_str = grid_str + f"{line}\n"
        return grid_str
