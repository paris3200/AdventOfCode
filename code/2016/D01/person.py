class Person:

    current_pos: [int, int]
    direction: str
    origin: [int, int]

    def __init__(self):
        self.origin = [0, 0]
        self.current_pos = [0, 0]
        self.direction = "N"
        self.visited = []

    def move(self, instruction) -> None:
        self.rotate(instruction)
        distance = int(instruction[1:])
        if self.direction == "N":
            for x in range(0, distance):
                if [self.current_pos[0], self.current_pos[1]+x] in self.visited:
                    return 
                self.visited.append([self.current_pos[0], self.current_pos[1]+x])
            self.current_pos[1] += distance
        elif self.direction == "S":
            for x in range(0, distance):
                if [self.current_pos[0], self.current_pos[1]-x] in self.visited:
                    return 
                self.visited.append([self.current_pos[0], self.current_pos[1]-x])
            self.current_pos[1] -= distance
        elif self.direction == "E":
            for x in range(0, distance):
                if [self.current_pos[0]+x, self.current_pos[1]] in self.visited:
                    return 
                self.visited.append([self.current_pos[0]+x, self.current_pos[1]])
            self.current_pos[0] += distance
        elif self.direction == "W":
            for x in range(0, distance):
                if [self.current_pos[0]-x, self.current_pos[1]] in self.visited:
                    return 
                self.visited.append([self.current_pos[0]-x, self.current_pos[1]])
            self.current_pos[0] -= distance
        

    def rotate(self, instruction):
        turn = instruction[0]
        if self.direction == "N" and turn == "R":
            self.direction = "E"

        elif self.direction == "N" and turn == "L":
            self.direction = "W"

        elif self.direction == "E" and turn == "R":
            self.direction = "S"

        elif self.direction == "E" and turn == "L":
            self.direction = "N"

        elif self.direction == "S" and turn == "R":
            self.direction = "W"

        elif self.direction == "S" and turn == "L":
            self.direction = "E"

        elif self.direction == "W" and turn == "R":
            self.direction = "N"

        elif self.direction == "W" and turn == "L":
            self.direction = "S"

    def distance_traveled(self) -> int:
        return abs(self.origin[0]) + abs(self.origin[1])

    def __str__(self):
        return f"Currently located {self.distance_traveled()} from origin at {self.current_pos}"


