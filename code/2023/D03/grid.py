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

    def get_matching_points(self, value: str) -> list[list[int]]:
        """
        Get the coordinates for all points that match value.

        Returns
        -------
        list[list[int]]: List of coordinate pairs.
        """
        matched_points = []
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == value:
                    matched_points.append([x, y])

        return matched_points

    def get_adjacent_points(self, x: int, y: int) -> list[list[int]]:
        """
        Get's the Coordinates for all adjacent points.

        Paramaters
        ----------
        x: int
            horizontal value of point
        y: int
            vertical value of point

        Returns
        -------
        list[list[int]] List of Coordinate pairs.
        """
        adjacent_points = []
        adjacent_points.append([x, y - 1])
        adjacent_points.append([x - 1, y - 1])
        adjacent_points.append([x + 1, y - 1])
        adjacent_points.append([x - 1, y])
        adjacent_points.append([x + 1, y])
        adjacent_points.append([x + 1, y + 1])
        adjacent_points.append([x, y+1])
        adjacent_points.append([x - 1, y+1])

        for point in adjacent_points.copy():
            if point[0] > self.max_x or point[0] == -1 or point[1] == -1 or point[1] > self.max_y:
                adjacent_points.remove(point)

        adjacent_points.sort()
        return adjacent_points

    def __repr__(self):
        grid_str = ""
        for y in range(0, self.max_y):
            line = "".join(self.grid[y])
            grid_str = grid_str + f"{line}\n"
        return grid_str
