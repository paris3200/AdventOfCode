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
        self.grid = [[default_value for x in range(x)] for y in range(y)]
        self.max_x = x
        self.max_y = y

    def set_point(self, x: int, y: int, value: int) -> None:
        """Sets the point at location x,y to value.

        Paramaters
        ----------
        x: int
            horizontal position of point
        y: int
            vertical position of point
        value: int
            Value of point
        """
        self.grid[y][x] = value


    def get_point(self, x: int, y: int) -> None:
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

    def increase_point(self, x: int, y: int, increase: int = 1) -> None:
        """Increases the value at point x,y by the amount of increase.

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


    def __repr__(self):
        grid_str = ""
        for y in range(0, self.max_y):
            grid_str = f"{self.grid[y]}\n" + grid_str
        return grid_str
