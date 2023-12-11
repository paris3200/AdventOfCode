class Parser:
    def __init__(self, filename: str = None) -> None:

        if filename:
            with open(filename) as file:
                self.lines = file.readlines()

    
    def to_list(self):
        line = self.lines[0].replace(" ", "")
        return line.split(",")
