import numpy as np


def create_line(start, stop, diagonal=False):
    """
    Creates all points on a line given the end points of the line.

    Args:
        start (list): One end point [x, y] of line.
        stop (list): Second end point [x, y] of line.
        diagonal (bool): False if diagonal numbers are to be ignored.

    Returns:
        numpy array: All points on line including the start and stop.
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

    # Diagonal Lines
    elif diagonal == True:
        xcoord = []
        ycoord = []
        if start[0] > stop[0]:
            xdelta = -1
        else:
            xdelta = 1

        if start[1] > stop[1]:
            ydelta = -1
        else:
            ydelta = 1

        for x in range(start[0]-xdelta, stop[0], xdelta):
            xcoord.append(x + xdelta)

        for y in range(start[1]-ydelta, stop[1], ydelta):
            ycoord.append(y + ydelta)

        line = list(zip(ycoord, xcoord))
        line.sort()
    else:
        return None

    return np.array(line)


def create_grid(end_point):
    """
    Creates a grid starting at [0,0] and going to the endpoint.

    Args:
        end_point (numpy array): Coordinate of lower right point in the grid.

    Returns:
        numpy array: Grid with 0 at each point on the grid.
    """
    return np.full([end_point[0] + 1, end_point[1] + 1], 0, dtype=int)


def mark_grid(grid, line):
    """
    Marks a line on the grid.

    If there is no line at that coordinate the grid displays 1.  If the line
    creates an intersection, the intersection point is incremmented.

    Args:
        grid (numpy array): Grid to be marked.
        line (numpy array): All points on the line to be marked.

    Returns:
        numpy array:  The marked grid.
    """
    for point in line:
        grid[point[1]][point[0]] += 1
    return grid


def count_intersections(grid):
    """
    Counts of the number of intersections on a grid.

    If the grid value is 2 or greater it is an intersection.

    Args:
        grid (numpy array): grid to be anaylzed.

    Returns:
        int: Number of intersections
    """
    i_list = np.nonzero(grid >= 2)
    coordinates = list(zip(i_list[0], i_list[1]))
    return len(coordinates)


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
        numpy array: list of lines starting and ending point.
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


def part_one(data, grid_size=[1000, 1000], diagonal=False):

    end_points = read_file(data)

    line_segments = []
    for item in end_points:
        line = create_line(item[0], item[1], diagonal)
        if line is not None:
            line_segments.append(line)

    grid = create_grid(grid_size)

    for line in line_segments:
        grid = mark_grid(grid, line)

    return count_intersections(grid)


if __name__ == "__main__":
    #data = "data/05.data"
    #result = part_one(data)

    #print("  Part One  \n")
    #print("Intersections: " + str(result) + "\n")

    data = "data/05.data"
    result = part_one(data, diagonal=True)
    print("  Part Two  \n")
    print("Intersections: " + str(result) + "\n")
