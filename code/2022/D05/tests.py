from d05 import CargoHold, part_one, part_two


def test_get_stack_names_reads_file_correctly() -> None:
    cargo = CargoHold("test_input")
    assert cargo.get_stack_names("test_input") == [1, 2, 3]


def test_stacks_created_in_init() -> None:
    cargo = CargoHold("test_input")
    assert cargo.stacks == {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}


def test_correct_answer_part_one() -> None:
    assert part_one() == "QPJPLMNNR"


def test_correct_answer_part_two() -> None:
    assert part_two() == "BQDNWJPVJ"
