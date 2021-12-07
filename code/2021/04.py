import pytest


class Bingo:
    def __init__(self, filename):
        self.boards = []
        self.number_pool = []
        self.marked_numbers = []
        self.winner = None
        self.loser = None

        with open(filename, "r") as f:
            data = f.readlines()

        first_line = data.pop(0)
        for num in first_line.strip().split(","):
            self.number_pool.append(int(num))

        current_board = -1

        for line in data:
            if line == "\n":
                current_board += 1
                self.boards.append(Bingoboard())
            else:
                row = line.rstrip().split()
                for x, num in enumerate(row):
                    row[x] = int(num)
                self.boards[current_board].add_row(row)

    def play(self):
        if len(self.boards) > 0 and len(self.number_pool) > 0:
                self.draw_number(self.number_pool[0])

    def draw_number(self, number):
        self.number_pool.pop(0)
        self.marked_numbers.append(number)
        for board in self.boards:
            board.mark_number(number)
            if board.bingo:
                if self.winner is None:
                    self.winner = board
                if len(self.boards) == 1:
                    self.loser = board
                self.boards.remove(board)
        self.play()


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
        self.matched_numbers = []
        self.checked_numbers = []

    def add_row(self, row):
        self.board.append(row)

    def mark_number(self, number):
        """
        Checks to see if the drawn number is on the board.
        If it is, then updates the matched array at that coordinate.
        """
        self.checked_numbers.append(number)
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
                            self.matched_numbers.append(number)
                            self.score_board()

    def score_board(self):
        self.score_rows()
        self.score_columns()


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
                sums[x] += self.matched[y][x]

        for total in sums:
            if total == 5:
                self.bingo = True

        """Returns the sum of the numbers remaining multipled by the last number called."""
        return self.get_sum() * self.last_number

    def get_sum(self):
        sum = 0
        for y, row in enumerate(self.matched):
            for x, col in enumerate(row):
                if col == 0:
                    sum += self.board[y][x]
        return sum

    def get_score(self):
        """Returns the sum of the numbers remaining multipled by the last number called."""
        return self.get_sum() * self.last_number

    def __repr__(self):
        board = ""
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                if self.matched[y][x] == 1:
                    board += " x "
                else:
                    if len(str(col)) == 1:
                        board += " " + str(col) + " "
                    else:
                        board += str(col) + " "

            board += "\n"
        return board


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


def test_bingoboard_sum():
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

    assert board.get_sum() == 325
    board.matched = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert board.get_sum() == 302


def test_column_gets_bingo():
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
    numbers = [4, 19, 20, 5, 7]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True

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
    numbers = [24, 9, 26, 6, 3]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True

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
    numbers = [17, 15, 23, 13, 12]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True

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
    numbers = [21, 16, 8, 11, 0]
    for num in numbers:
        board.mark_number(num)
    assert board.bingo is True


def test_part_one_with_sample_data():
    data = "data/04_test.data"
    game = Bingo(data)
    game.play()
    board = game.winner
    assert board.get_score() == 4512
    assert board.get_sum() == 188
    assert board.last_number == 24


def test_Bingo_with_sample_data_v2():
    data = "data/04_tests_v2.data"
    game = Bingo(data)
    game.play()
    board = game.winner
    assert board.get_score() == 4862
    assert board.get_sum() == 187
    assert board.last_number == 26


def test_part_two_with_sample_data():
    data = "data/04_test.data"
    game = Bingo(data)
    pool = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    assert game.number_pool == pool
    game.play()
    board = game.loser
    breakpoint()
    assert board.matched_numbers == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13]
    loser_board = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    matched = [
        [0, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0],
    ]
    assert board.board == loser_board
    #assert board.matched == matched
    assert board.last_number == 13
    #assert board.get_sum() == 148
    #assert board.get_score() == 1924


def test_board_gets_bingo():
    card = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    matched = [
        [0, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0],
    ]
    numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13]

    board = Bingoboard()
    for line in card:
        board.add_row(line)
    for num in numbers:
        board.mark_number(num)
    assert board.bingo is True
    assert board.matched == matched

def test_mark_number():
    card = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    board = Bingoboard()
    for line in card:
        board.add_row(line)

    board.mark_number(16)
    matched = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    assert board.matched == matched



def part_one(data):
    game = Bingo(data)
    game.play()
    board = game.winner
    print("Part One \n")
    print("    Bingo!")
    print(board)
    print("Winning Number: " + str(board.last_number))
    print("Board Sum: " + str(board.get_sum()))
    print("Total Score: " + str(board.get_score()))


def part_two(data):
    game = Bingo(data)
    game.play()
    board = game.loser
    print("\n Part Two \n")
    print("    Bingo!")
    print(board)
    print("Winning Number: " + str(board.last_number))
    print("Board Sum: " + str(board.get_sum()))
    print("Total Score: " + str(board.get_score()))


if __name__ == "__main__":
    data = "data/04.data"
    part_one(data)
    part_two(data)
