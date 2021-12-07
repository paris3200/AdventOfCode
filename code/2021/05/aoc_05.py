def create_line(start, stop):
    line = []
    # Horizontal Lines
    if start[0] == stop[0]:
        delta = stop[1] - start[1]
        for  x, y in enumerate(range(start[1], delta+1)):
            line.append([start[0], y])
        line.append(stop)

    # Vertical Lines
    elif start[1] == stop[1]:
        for  x, y in enumerate(range(stop[0], start[0])):
            line.append([y, start[1]])
        line.append(start)
        line.reverse()
    return line


def get_list_limits(coordinates):
    """
    Determines the x,y coordinates of the lower right corner of a grid 
    that will contain all points in the coordinates list.

    Args:
        coordinates (list): List of coordinates [x,y]

    Returns:
        list: Starting point and end point of coordinate grid.  [[0,0], [9,9]]
    """
    x = 0
    y = 0
    for point in coordinates:
        if point[0] > x:
            x = point[0]
        if point[1] > y:
            y = point[1]

    return [[0, 0], [x, y]]
