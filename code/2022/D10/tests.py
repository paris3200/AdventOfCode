from d10 import Register, CRT, Parser, part_one


def test_no_opp_increments_one_cycle() -> None:
    r = Register()

    assert r.cycle == 0
    r.execute_cycle()
    assert r.cycle == 1


def test_addx_increments_two_cycles() -> None:
    r = Register()

    assert r.cycle == 0
    r.addx(3)
    assert r.cycle == 2
    assert r.value == 4


def test_signal_strength_triggered_at_20() -> None:
    r = Register()
    r.value = 21
    r.cycle = 19
    r.addx(-1)
    assert r.signal_strength[0] == 420


def test_signal_strength_triggered_at_60() -> None:
    r = Register()
    r.value = 19
    r.cycle = 59
    r.noop()
    assert r.signal_strength[0] == 1140


def test_register_small_test_data() -> None:
    r = Register()
    r.noop()
    r.addx(3)
    r.addx(-5)

    assert r.value == -1


def test_part_one():
    assert part_one("data/test_input") == 13140
