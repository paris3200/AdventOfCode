from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Directory:
    parent: Directory
    name: str
    child_dirs: list[Directory]
    child_files: list[File]


@dataclass
class File:
    name: str
    size: int


class Parser:
    def __init__(self, filename: str = None) -> None:

        if filename:
            with open(filename) as file:
                self.lines = file.readlines()
        
    def process_input(self) -> Directory:
        root = None
        current_dir = None

        for line in self.lines:
            if self.is_command(line) is True:
                command = line.strip().split()
                if line.strip() == "$ cd /":
                    root = Directory(
                        parent=None, name="/", child_dirs=[], child_files=[]
                    )
                    current_dir = root
                elif command[1] == "cd":
                    if command[2] == "..":
                        current_dir = current_dir.parent
                    else:
                        directory = self.get_directory(current_dir, command[2])
                        current_dir = directory
                elif command[1] == "ls":
                    pass
            else:
                part1, name = line.strip().split(" ")
                if part1 == "dir":
                    name = Directory(
                        parent=current_dir, name=name, child_dirs=[], child_files=[]
                    )
                    current_dir.child_dirs.append(name)
                elif part1.isnumeric():
                    file = File(name=name, size=int(part1))
                    current_dir.child_files.append(file)

        return root

    @staticmethod
    def is_command(line: str) -> bool:
        """True if line is a command."""
        if line[0] == "$":
            return True
        return False

    @staticmethod
    def get_directory(directory: Directory, name: str) -> Directory:
        for directory in directory.child_dirs:
            if directory.name == name:
                return directory
