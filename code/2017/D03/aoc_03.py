def create_grid(size: int) -> dict[str:int]:
    dx = 1
    dy = 0

    segment_length = 1
    current_x = 0
    current_y = 0

    points = {"0, 0": 1}

    segment_passed = 0
    count = 1
    while count < size:
        current_x += dx
        current_y += dy

        sum = sum_adjacents(points, current_x, current_y)

        points.update({f"{current_x}, {current_y}": sum})

        segment_passed += 1
        if segment_passed == segment_length:
            segment_passed = 0

            old_dx = dx
            dx = -dy
            dy = old_dx

            if dy == 0:
                segment_length += 1

        count += 1

    return points


def sum_adjacents(grid: dict[str:int], x: int, y: int) -> int:
    sum = 0
    adjacents = [
        f"{x+1}, {y}",
        f"{x+1}, {y+1}",
        f"{x+1}, {y-1}",
        f"{x}, {y+1}",
        f"{x}, {y-1}",
        f"{x-1}, {y}",
        f"{x-1}, {y+1}",
        f"{x-1}, {y-1}",
    ]

    for point in adjacents:
        if point in grid:
            sum += grid[point]

    return sum


def part_one(size):
    dx = 1
    dy = 0

    segment_length = 1
    current_x = 0
    current_y = 0

    segment_passed = 0
    count = 1
    while count < size:
        current_x += dx
        current_y += dy

        segment_passed += 1
        if segment_passed == segment_length:
            segment_passed = 0

            old_dx = dx
            dx = -dy
            dy = old_dx

            if dy == 0:
                segment_length += 1

        count += 1

    return abs(current_x) + abs(current_y)


def part_two(size):
    grid = create_grid(size)
    for point in grid:
        if grid[point] > size:
            return grid[point]


if __name__ == "__main__":
    print("Part One")
    print(part_one(325489))

    print("Part Two")
    print(part_two(325489))
