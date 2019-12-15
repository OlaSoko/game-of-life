import pytest

from gameoflife import GameOfLife


def test_init():
    seed = [(1, 4), (6, 7)]
    gof = GameOfLife(seed=seed)
    # assert seed == gof.state
    assert all(cell in gof.state for cell in seed)


def test_is_alive():
    alive_cell = (1, 4)
    seed = [alive_cell, (6, 7)]
    gof = GameOfLife(seed=seed)
    assert gof.is_alive(alive_cell)


def test_die():
    alive_cell = (1, 4)
    seed = [alive_cell, (6, 7)]
    gof = GameOfLife(seed=seed)
    gof.die(alive_cell)
    assert alive_cell not in gof.next_state


def test_live():
    alive_cell = (1, 4)
    seed = [(6, 7)]
    gof = GameOfLife(seed=seed)
    gof.live(alive_cell)
    assert alive_cell in gof.next_state


@pytest.mark.parametrize(['neighbours', 'count'], (
    ([(2, 2), (3, 4), (4, 3)], 3),
    ([(2, 2), (3, 4), (8, 9)], 2),
    ([], 0),
    ([(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)], 8),
    ([(1, 1), (1, 8), (6, 7)], 0)
))
def test_get_neighbours_count(neighbours, count):
    alive_cell = (3, 3)
    seed = [alive_cell] + neighbours
    gof = GameOfLife(seed=seed)
    assert gof.get_neighbours_count(alive_cell) == count


def test_tick_live_cell_2_3_neighbours_lives():
    start_state = [(3, 3), (3, 2), (4, 3), (2, 4)]
    end_state = [(3, 3), (3, 2), (4, 3)]
    gof = GameOfLife(start_state)
    gof.tick()
    assert all(cell in gof.state for cell in end_state)


def test_tick_dead_cell_3_neighbours_live():
    start_state = [(3, 3), (3, 2), (4, 3), (2, 4)]
    end_state = [(3, 3), (3, 2), (4, 3), (4, 2)]
    gof = GameOfLife(start_state)
    gof.tick()
    assert all(cell in gof.state for cell in end_state)


def test_tick_live_cell_dies():
    start_state = [(3, 3), (3, 2), (4, 3), (2, 4)]
    end_state = [(2, 4)]
    gof = GameOfLife(start_state)
    gof.tick()
    assert all(cell not in gof.state for cell in end_state)


def test_tick_dead_cell_stays_dead():
    start_state = [(3, 3), (3, 2), (4, 3), (2, 4)]
    end_state = [(2, 2), (4, 4)]
    gof = GameOfLife(start_state)
    gof.tick()
    assert all(cell not in gof.state for cell in end_state)


def test_tick_blinker():
    state_1 = [(1, 0), (1, 1), (1, 2)]
    state_2 = [(0, 1), (1, 1), (2, 1)]
    gof = GameOfLife(seed=state_1)
    gof.tick()
    assert all(cell in gof.state for cell in state_2)
    gof.tick()
    assert all(cell in gof.state for cell in state_1)


def test_tick_glider():
    state_0 = [(0, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
    state_1 = [(2, 0), (0, 1), (2, 1), (1, 2), (2, 2)]
    state_2 = [(1, 0), (2, 1), (3, 1), (1, 2), (2, 2)]
    state_3 = [(2, 0), (3, 1), (1, 2), (2, 2), (3, 2)]
    state_4 = [(1, 1), (3, 1), (2, 2), (3, 2), (2, 3)]

    gof = GameOfLife(seed=state_0)
    gof.tick()
    assert all(cell in gof.state for cell in state_1)
    gof.tick()
    assert all(cell in gof.state for cell in state_2)
    gof.tick()
    assert all(cell in gof.state for cell in state_3)
    gof.tick()
    assert all(cell in gof.state for cell in state_4)
