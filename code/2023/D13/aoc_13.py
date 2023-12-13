from grid import Grid


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def create_grid(filename: str) -> Grid:
    lines = read_lines(filename)
    length_x = len(lines[0])
    length_y = len(lines)
    grid = Grid(length_x, length_y, default_value=".")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid.set_point(x=x, y=y, value=char)

    return grid


def check_horizontal(grid: Grid) -> int:
    match_location = 0
    count_above_fold = 0
    lines_above = []
    lines_below = []
    for x in range(1, grid.max_y-1):
        row1 = grid.get_row(x)
        row2 = grid.get_row(x+1)
        if row1 == row2:
            lines_above.append(row1)
            lines_below.append(row2)
            match_location = x
            count_above_fold += 1
    
    count = match_location
    
    x = match_location
    above= []
    below=[]
    while x > 0:
        x -= 1
        above.append(x)

    x = match_location+1
    while x < grid.max_y-1:
        x += 1
        below.append(x)

    if len(above) > len(below):
        above.pop()
    elif len(below) > len(above):
        below.pop()
    
    while len(above) != 0:
        row1 = grid.get_row(above.pop(0))
        row2 = grid.get_row(below.pop(0))
        if row1 == row2:
            count += 1
            count_above_fold += 1
    
    if (match_location + count_above_fold + 1) == grid.max_y or match_location - count_above_fold == 0:
        return count_above_fold
    return 0


