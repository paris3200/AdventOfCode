import pytest


def setup_game(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    drawn_numbers = []
    first_line = data.pop(0)
    for num in first_line.strip().split(","):
        drawn_numbers.append(int(num))

    boards = []
    current_board = -1
    for index, line in enumerate(data):
        if line == "\n":
            current_board += 1
            boards.append(Bingoboard())
        else:
            row = line.rstrip().split()
            for x, num in enumerate(row):
                row[x] = int(num)
            boards[current_board].add_row(row)

    marked_nums = []
    for num in drawn_numbers:
        marked_nums.append(num)
        for board in boards:
            board.mark_number(num)
            if board.bingo is True:
                return board


class Bingoboard:
    def __init__(self):
        self.board = []
        self.matched = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.bingo = False
        self.last_number = 0

    def add_row(self, row):
        self.board.append(row)

    def mark_number(self, number):
        xcor = ""
        ycor = ""
        for x, row in enumerate(self.board):
            for y, col in enumerate(row):
                if col == number:
                    xcor = x
                    ycor = y

        if xcor != "" and ycor != "":
            for y, row in enumerate(self.matched):
                if y == ycor:
                    for x, col in enumerate(row):
                        if x == xcor:
                            self.matched[x][y] = 1
                            self.last_number = number
                            return self.score_board()

    def score_board(self):
        self.score_rows()
        self.score_columns()

        if self.bingo is True:
            return True

    def score_rows(self):
        for row in self.matched:
            sum = 0
            for item in row:
                sum += item
            if sum == 5:
                self.bingo = True

    def score_columns(self):
        sums = [0, 0, 0, 0, 0]
        for y in range(0, 5):
            for x in range(0, 5):
                sums[y] += self.matched[y][x]

        for sum in sums:
            if sum == 5:
                self.bingo = True

    def get_score(self):
        """Returns the sum of the numbers remaining multipled by the last number called."""
        return self.get_sums() * self.last_number

    def get_sums(self):
        sum = 0
        for y, row in enumerate(self.matched):
            for x, col in enumerate(row):
                if col == 0:
                    sum += self.board[y][x]
        return sum

    def __repr__(self):
        board = ""
        for row in self.board:
            board += str(row) + "\n"
        board += "\n"
        return board


def part_one(data):
    return setup_game(data)


def part_two(data):
    pass


def test_bingoboard_gets_bingo():
    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = Bingoboard()
    for line in card:
        board.add_row(line)
    numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True
    assert board.get_score() == 4512

    matched = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    assert board.matched == matched


def test_bingoboard_sums():
    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = Bingoboard()
    for line in card:
        board.add_row(line)

    assert board.get_sums() == 325
    board.matched = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert board.get_sums() == 302


def test_part_one_with_sample_data():
    data = "data/04_test.data"
    result = part_one(data)
    assert result.get_score() == 4512
    assert result.get_sums() == 188
    assert result.last_number == 24


def test_part_one_with_sample_data_v2():
    data = "data/04_tests_v2.data"
    result = part_one(data)
    assert result.get_score() == 4862
    assert result.get_sums() == 187
    assert result.last_number == 26


@pytest.mark.skip()
def test_part_one_with_sample_data():
    data = "data/04.data"
    result = part_one(data)
    assert result.get_score() != 24814


@pytest.mark.skip()
def test_part_two():
    data = "data/04_test.data"
    result = part_two(data)
    assert result is True


if __name__ == "__main__":
    data = "data/04.data"
    print("Part One")
    print(part_one(data).get_score())
    print("Part Two")
    print(part_two(data))
