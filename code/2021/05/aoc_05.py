import numpy as np
from nptyping import NDArray
from typing import Any


def create_line(start, stop, diagonal=False) -> NDArray[np.int32]:
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

        # Find the leftmost point
        if start[0] < stop[0]:
            begin = start
            end = stop
        else:
            begin = stop
            end = start


        # Determine slope
        if begin[0] <= end[0] and begin[1] <= end[1]:
            m = 1
        else:
            m = -1
        b = -1 * (m * begin[0] - begin[1])

        line = []
        for x in range(min(start[0], stop[0]), max(start[0], stop[0]) + 1):
            y = m * x + b
            line.append([x, y])

    return np.array(line)


def create_grid(end_point) -> NDArray[np.int32]:
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


def print_grid(grid) -> str:
    map = ""
    for row in grid:
        for col in row:
            map += " " + str(col) + " "
        map += "\n"
    return map


def read_file(filename) -> list:
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


def part_one(data, grid_size=[1000, 1000], diagonal=False):

    end_points = read_file(data)

    line_segments = []
    for item in end_points:
        line = create_line(item[0], item[1], diagonal)
        if len(line) > 0:
            line_segments.append(line)

    grid = create_grid(grid_size)

    for line in line_segments:
        grid = mark_grid(grid, line)

    return count_intersections(grid)


if __name__ == "__main__":
    data = "data/05.data"
    result = part_one(data)

    print("  Part One  \n")
    print("Intersections: " + str(result) + "\n")

    result = part_one(data, diagonal=True)
    print("  Part Two  \n")
    print("Intersections: " + str(result) + "\n")
