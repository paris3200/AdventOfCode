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
        self.number_pool.remove(number)
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
    print("Numbers Played: " + str(board.checked_numbers))
    print("Numbers Matched: " + str(board.matched_numbers))
    print("Winning Number: " + str(board.last_number))
    print("Board Sum: " + str(board.get_sum()))
    print("Total Score: " + str(board.get_score()))


if __name__ == "__main__":
    data = "data/04.data"
    part_one(data)
    part_two("data/04_test.data")
