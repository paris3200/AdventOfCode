
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
