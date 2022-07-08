import pytest

from Y2015 import D07
from Y2015 import utils


def test_format_instruction_when_single_applied_to_wire():
    command = {
        "input1": None,
        "input2": None,
        "gate": None,
        "shift-value": None,
        "signal": 123,
        "output": "x",
    }
    assert command == D07.format_instruction("123 -> x")



def test_format_instruction_and_gate():
    command = {
        "input1": "x",
        "input2": "y",
        "gate": "AND",
        "shift-value": None,
        "signal": None,
        "output": "z",
    }
    assert command == D07.format_instruction("x AND y -> z")


def test_format_instruction_or_gate():
    command = {
        "input1": "x",
        "input2": "y",
        "gate": "OR",
        "shift-value": None,
        "signal": None,
        "output": "z",
    }
    assert command == D07.format_instruction("x OR y -> z")


def test_format_instruction_shift_gate():
    command = {
        "input1": "p",
        "input2": None,
        "gate": "LSHIFT",
        "shift-value": 2,
        "signal": None,
        "output": "q",
    }
    assert command == D07.format_instruction("p LSHIFT 2 -> q")


def test_format_instruction_not_gate():
    command = {
        "input1": "e",
        "input2": None,
        "gate": "NOT",
        "shift-value": None,
        "signal": None,
        "output": "f",
    }
    assert command == D07.format_instruction("NOT e -> f")


def test_get_wire_signal_returns_correct_value():
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    result = D07.get_wire_signal(wires, "y")
    assert result == 456
    result = D07.get_wire_signal(wires, "x")
    assert result == 123


def test_process_instruction_with_update_to_wire():
    command = {
        "input1": "x",
        "input2": "y",
        "gate": "AND",
        "shift-value": None,
        "signal": None,
        "output": "x",
    }
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = []
    expected.append({"identifier": "x", "signal": 72})
    expected.append({"identifier": "y", "signal": 456})
    result = D07.process_instruction(command, wires)
    assert result == expected
    pass

def test_process_instruction_and():
    command = {
        "input1": "x",
        "input2": "y",
        "gate": "AND",
        "shift-value": None,
        "signal": None,
        "output": "d",
    }
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "d", "signal": 72})
    result = D07.process_instruction(command, wires)
    assert result == expected


def test_process_instruction_and_missing_signal():
    """Gate should not return a signal if any inputs are missing a signal"""
    command = {
        "input1": "x",
        "input2": "y",
        "gate": "AND",
        "shift-value": None,
        "signal": None,
        "output": "d",
    }
    wires = []
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    result = D07.process_instruction(command, wires)
    assert result == expected


def test_process_instruction_or():
    command = {
        "input1": "x",
        "input2": "y",
        "gate": "OR",
        "shift-value": None,
        "signal": None,
        "output": "e",
    }
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "e", "signal": 507})
    result = D07.process_instruction(command, wires)
    assert result == expected


def test_process_instruction_rshift():
    command = {
        "input1": "y",
        "input2": None,
        "gate": "RSHIFT",
        "shift-value": 2,
        "signal": None,
        "output": "g",
    }
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "g", "signal": 114})
    result = D07.process_instruction(command, wires)
    assert result == expected


def test_process_instruction_not():
    command = {
        "input1": "y",
        "input2": None,
        "gate": "NOT",
        "shift-value": None,
        "signal": None,
        "output": "i",
    }
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "i", "signal": 65079})
    result = D07.process_instruction(command, wires)
    assert result == expected


def test_part_one_with_sample_data():
    instructions = utils.read_lines("data/07_test.data")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    wires.append({"identifier": "d", "signal": 72})
    wires.append({"identifier": "e", "signal": 507})
    wires.append({"identifier": "f", "signal": 492})
    wires.append({"identifier": "g", "signal": 114})
    wires.append({"identifier": "h", "signal": 65412})
    wires.append({"identifier": "i", "signal": 65079})
    result = D07.part_one(instructions)
    assert result == wires


@pytest.mark.skip("Not Implemented")
def test_part_one_correct_answer():
    result = D07.part_one(wire="a")
    assert result is not None


@pytest.mark.skip("Not Implemented")
def test_part_two_correct_answer():
    pass
