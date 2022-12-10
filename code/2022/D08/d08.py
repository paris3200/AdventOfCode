from grid import Grid
from parser import Parser


class Map(Grid):
    def __init__(self, lines: list) -> None:
        x, y = self.get_dimensions(lines)
        super().__init__(x, y, 0)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self.set_point(x, y, int(char))

    def get_dimensions(self, lines: list) -> list[int, int]:
        x = len(lines[0])
        y = len(lines)

        return [x, y]

    def is_visible(self, x: int, y: int) -> bool:
        # All edge trees are visible.
        if x == 0 or x == self.max_x - 1:
            return True
        if y == 0 or y == self.max_y - 1:
            return True

        if self.row_visible(x, y) is True or self.column_visible(x, y) is True:
            return True

        return False

    def row_visible(self, x: int, y: int) -> bool:
        row = self.grid[y]
        height = self.get_point(x, y)

        left = row[:x]
        right = row[x + 1 :]

        left_visible = True
        right_visible = True

        for tree in left:
            if tree >= height:
                left_visible = False

        for tree in right:
            if tree >= height:
                right_visible = False

        if right_visible is True or left_visible is True:
            return True

        return False

    def column_visible(self, x: int, y: int) -> bool:
        height = self.get_point(x, y)
        column = self.get_column(x, y)

        top = column[:y]
        bottom = column[y + 1 :]

        top_visible = True
        bottom_visible = True

        for tree in top:
            if tree >= height:
                top_visible = False

        for tree in bottom:
            if tree >= height:
                bottom_visible = False

        if top_visible is True or bottom_visible is True:
            return True

    def get_column(self, x: int, y: int) -> list[int]:
        column = []
        for row in self.grid:
            column.append(row[x])

        return column

    def scenic_score(self, x: int, y: int) -> int:
        if x == 0 or x == self.max_x - 1 or y == 0 or y == self.max_y - 1:
            return 0

        row = self.grid[y]
        left = row[:x]
        left.reverse()
        right = row[x + 1 :]

        column = self.get_column(x, y)
        up = column[:y]
        up.reverse()
        down = column[y + 1 :]

        height = self.get_point(x, y)

        left_score = self.scenic_cout(left, height)
        right_score = self.scenic_cout(right, height)
        up_score = self.scenic_cout(up, height)
        down_score = self.scenic_cout(down, height)

        return left_score * right_score * up_score * down_score

    def scenic_cout(self, trees: list, height: int) -> int:
        visible = []
        for tree in trees:
            if tree >= height:
                visible.append(tree)
                return len(visible)
            else:
                visible.append(tree)

        return len(visible)


def part_one(input: str) -> int:
    parser = Parser(input)
    map = Map(parser.get_lines())
    sum = 0
    visible_points = []

    for y, line in enumerate(map.grid):
        for x, char in enumerate(line):
            if map.is_visible(x, y) is True:
                sum += 1
                visible_points.append([x, y])
    return sum


def part_two(input: str) -> int:
    parser = Parser(input)
    map = Map(parser.get_lines())
    scenic_score = []

    for y, line in enumerate(map.grid):
        for x, char in enumerate(line):
            scenic_score.append(map.scenic_score(x, y))

    scenic_score.sort()
    return scenic_score.pop()


if __name__ == "__main__":
    print(part_one("data/input"))
    print(part_two("data/input"))
