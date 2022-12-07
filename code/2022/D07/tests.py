import pytest
from parser import Directory, File, Parser
from d07 import FileSystem, part_one, part_two


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("$ cd /", True),
        ("dir a", False),
        ("584 i", False),
    ),
)
def test_is_command(line, expected) -> None:
    parser = Parser()
    assert parser.is_command(line) == expected


def test_get_size_files_only() -> None:
    d = Directory(name="d", parent=None, child_dirs=[], child_files=[])
    d.child_files.append(File(name="j", size=4060174))
    d.child_files.append(File(name="d.log", size=8033020))
    d.child_files.append(File(name="d.ext", size=5626152))
    d.child_files.append(File(name="k", size=7214296))

    filesystem = FileSystem(root=d)

    assert filesystem.get_size(d) == 24933642
   

def test_get_size_files_and_directories() -> None:
    root = Directory(name="/", parent=None, child_dirs=[], child_files=[])
    a = Directory(name="a", parent=root, child_dirs=[], child_files=[])
    e = Directory(name="e", parent=a, child_dirs=[], child_files=[])

    d = Directory(name="d", parent=root, child_dirs=[], child_files=[])
    d.child_files.append(File(name="j", size=4060174))
    d.child_files.append(File(name="d.log", size=8033020))
    d.child_files.append(File(name="d.ext", size=5626152))
    d.child_files.append(File(name="k", size=7214296))

    root.child_dirs.append(a)
    root.child_dirs.append(d)

    root.child_files.append(File(name="b.txt", size=14848514))
    root.child_files.append(File(name="c.txt", size=8504156))

    e.child_files.append(File(name="i", size=584))
    a.child_dirs.append(e)
    a.child_files.append(File(name="f", size=29116))
    a.child_files.append(File(name="g", size=2557))
    a.child_files.append(File(name="h.lst", size=62596))

    fs = FileSystem(root=root)
    assert fs.get_size(e) == 584
    assert fs.get_size(a) == 94853
    assert fs.get_size(root) == 48381165
   

def test_part_one_test_data() -> None:
    assert part_one("test_input") == 95437


def test_part_two_test_data() -> None:
    assert part_two("test_input") == 24933642
    


