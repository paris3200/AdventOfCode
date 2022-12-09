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
        return self.scenic_score_horizontal(x, y) * self.scenic_score_vertical(x, y)

    def scenic_score_horizontal(self, x: int, y: int) -> int:
        row = self.grid[y]
        left = row[:x]
        right = row[x + 1 :]
        if x == 0:
            scenic_left = 0
        else:
            visible = []
            for index, tree in enumerate(left):
                if index == len(left) - 1:
                    visible.append(tree)
                else:
                    if left[index] < left[index + 1]:
                        continue
                    else:
                        visible.append(tree)
            scenic_left = len(visible)

        if x == self.max_x - 1:
            scenic_right = 0
        else:
            visible = []
            # calculate right
            for index, tree in enumerate(right):
                if index == len(right) - 1:
                    visible.append(tree)
                else:
                    if right[index] < right[index + 1]:
                        visible.append(tree)

            scenic_right = len(visible)
        return scenic_left * scenic_right


    def scenic_score_vertical(self, x: int, y: int) -> int:
        column = self.get_column(x, y)

        top = column[:y]
        bottom = column[y + 1 :]

        if y == 0:
            scenic_top = 0
        else:
            visible = []
            for index, tree in enumerate(top):
                if index == len(top) - 1:
                    visible.append(tree)
                else:
                    if top[index] <= top[index + 1]:
                        continue
                    else:
                        visible.append(tree)
            scenic_top = len(visible)

        if y == self.max_x - 1:
            scenic_bottom = 0
        else:
            visible = []
            # calculate bottom
            for index, tree in enumerate(bottom):
                if index == len(bottom) - 1:
                    visible.append(tree)
                else:
                    if bottom[index] <= bottom[index + 1]:
                        visible.append(tree)

            scenic_bottom = len(visible)
        return scenic_top * scenic_bottom


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
        row = []
        for x, char in enumerate(line):
            row.append(map.scenic_score(x, y))
        scenic_score.append(row)

    breakpoint()
    scenic_score.sort()
    return scenic_score.pop()


if __name__ == "__main__":
    print(part_one("data/input"))
    print(part_two("data/input"))
