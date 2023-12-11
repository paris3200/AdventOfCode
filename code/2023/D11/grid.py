from os import walk


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
        self.galaxies = []
        self.expand_rows = []
        self.expand_columns = []

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

    def find_point(self, value: str) -> list[int]:
        """
        Get the x, y location of a point with the value.

        Assumes each value is unique.

        Paramaters
        ----------
        value: str
            value of the point being located.

        Returns
        -------
        list[int]: The coordinates of the point with the value.
        """
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == value:
                    return [x, y]

    def calculate_distance(self, point1: list[int], point2: list[int]) -> int:
        """
        Calculate the distance between two points.

        Paramaters
        ----------
        point1: list[int]
            [x, y] coordinate of point 1
        point2: list[int]
            [x, y] coordinate of point 2

        Returns
        -------
        int: distance between the two points
        """
        distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        return abs(distance)


    def expand_grid(self) -> None:
        """
        Expand grid if the row or column is equal to value.

        Paramaters
        ----------
        value: str
            character that denotes an empty spot.
        """
        self.expand_row()
        self.expand_column()

    def expand_row(self) -> None:
        """
        Doubles the empty rows.
        """
        counter = 0
        for y, line in enumerate(self.grid.copy()):
            if set(line) == {"."}:
                self.grid.insert(counter + y + 1, line)
                counter += 1

        self.max_y = len(self.grid)

    def get_rows_to_expand(self) -> None:
        for y, line in enumerate(self.grid.copy()):
            if set(line) == {"."}:
                self.expand_rows.append(y)

    def get_columns_to_expand(self) -> None:
        grid_copy = self.grid.copy()
        column = []
        for x in range(0, self.max_x):
            column.clear()
            for y in range(0, self.max_y):
                column.append(grid_copy[y][x])

            if set(column) == {"."}:
                self.expand_columns.append(x)



    def expand_column(self) -> None:
        """
        Doubles the empty column.
        """
        counter = 0
        grid_copy = self.grid.copy()
        column = []
        for x in range(0, self.max_x):
            column.clear()
            for y in range(0, self.max_y):
                column.append(grid_copy[y][x])

            if set(column) == {"."}:
                x_index = x + counter + 1
                for y in range(0, self.max_y):
                    line = self.grid[y].copy()
                    line.insert(x_index, ".")
                    self.grid[y] = line
                counter += 1
        self.max_x = len(self.grid[0])

    def __repr__(self):
        grid_str = ""
        for y in range(0, self.max_y):
            line = " ".join(self.grid[y])
            grid_str = grid_str + f"{line}\n"
        return grid_str
