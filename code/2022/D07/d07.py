from parser import Parser, Directory


class FileSystem:
    def __init__(self, root: Directory, threshold: int = None) -> None:
        self.root = root
        self.threshold = threshold
        self.dir_below_threshold = []
        self.dir_above_threshold = []

    def get_size(self, directory: Directory) -> int:
        sum = 0
        for dir in directory.child_dirs:
            size = self.get_size(dir)
            if self.threshold is not None:
                if size <= self.threshold:
                    self.dir_below_threshold.append(size)
                if size > self.threshold:
                    self.dir_above_threshold.append(size)
            sum += size

        for file in directory.child_files:
            sum += file.size

        return sum

    def sum_below_threshold(self) -> int:
        total = 0
        for sum in self.dir_below_threshold:
            total += sum

        return total


def part_one(input: str):
    parser = Parser(input)
    root = parser.process_input()
    fs = FileSystem(root=root, threshold=100000)
    fs.get_size(root)
    return fs.sum_below_threshold()


def part_two(input: str):
    total_capacity = 70000000

    # Get the current used size
    parser = Parser(input)
    root = parser.process_input()
    fs = FileSystem(root=root, threshold=None)
    used_size = fs.get_size(root)

    freespace = total_capacity - used_size
    needed_size = 30000000 - freespace
    fs = FileSystem(root=root, threshold=needed_size)

    fs.get_size(root)
    fs.dir_above_threshold.sort()
    return fs.dir_above_threshold[0]


if __name__ == "__main__":
    print(part_one("input"))
    print(part_two("input"))
