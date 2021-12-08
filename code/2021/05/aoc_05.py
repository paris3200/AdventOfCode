def create_line(start, stop):
    """
    Creates all points on a line given the end points of the line.

    Args:
        start (list): One end point [x, y] of line.
        stop (list): Second end point [x, y] of line.

    Returns:
        list: All points on line including the start and stop.
    """
    line = []
    # Vertical Lines
    if start[0] == stop[0]:
        for y in range(min(start[1], stop[1]), max(start[1], stop[1]) + 1):
            line.append([start[0], y])

    # Horizontal Lines
    elif start[1] == stop[1]:
        for y in range(min(start[0], stop[0]), max(start[0], stop[0]) + 1):
            line.append([y, start[1]])
    else:
        return
    return line


def get_list_limits(coordinates):
    """
    Determines the x,y coordinates of the lower right corner of a grid
    that will contain all points in the coordinates list.

    Args:
        coordinates (list): List of coordinates [x,y]

    Returns:
        list: Lower right coordinate [x, y] of grid that can contain all points.
    """
    x = 0
    y = 0
    for point in coordinates:
        if point[0] > x:
            x = point[0]
        if point[1] > y:
            y = point[1]

    return [x, y]


def create_grid(end_point):
    """
    Creates a grid starting at [0,0] and going to the endpoint.

    Args:
        end_point (list): Coordinate of lower right point in the grid.

    Returns:
        list: Grid with 0 at each point on the grid.
    """
    grid = []
    for x in range(0, end_point[1] + 1):
        row = []
        for x in range(0, end_point[1] + 1):
            row.append(0)
        grid.append(row)
    return grid


def mark_grid(grid, line):
    """
    Marks a line on the grid.

    If there is no line at that coordinate the grid displays 1.  If the line
    creates an intersection, the intersection point is incremmented.

    Args:
        grid (list): Grid to be marked.
        line (list): All points on the line to be marked.

    Returns:
        list:  The marked grid.
    """
    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            for point in line:
                if point[0] == x and point[1] == y:
                    grid[y][x] += 1
    return grid


def count_intersections(grid):
    """
    Counts of the number of intersections on a grid.

    If the grid value is 2 or greater it is an intersection.

    Args:
        grid (list): grid to be anaylzed.

    Returns:
        int: Number of intersections
    """
    intersections = 0
    for row in grid:
        for point in row:
            if point >= 2:
                intersections += 1
    return intersections


def print_grid(grid):
    map = ""
    for row in grid:
        for col in row:
            map += " " + str(col) + " "
        map += "\n"
    return map


def read_file(filename):
    """
    Reads the file and converts into a list of coordinates.

    Args:
        filename (str):  file path

    Returns:
        list: list of lines starting and ending point.
    """
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        start = []
        end = []
        input = line.rstrip().split(" -> ")
        for x, point in enumerate(input):
            coor = point.split(",")
            if x == 0:
                start = [int(coor[0]), int(coor[1])]
            elif x == 1:
                end = [int(coor[0]), int(coor[1])]
        lines.append([start, end])

    return lines


def part_one(data):

    end_points = read_file(data)

    line_segments = []
    for item in end_points:
        line = create_line(item[0], item[1])
        if line is not None:
            line_segments.append(line)

    grid_size = [1000, 1000]

    grid = create_grid(grid_size)

    for line in line_segments:
        grid = mark_grid(grid, line)

    return count_intersections(grid)


if __name__ == "__main__":
    data = "data/05.data"
    result = part_one(data)

    print("  Part One  \n")
    print("Intersections: " + str(result) + "\n")
