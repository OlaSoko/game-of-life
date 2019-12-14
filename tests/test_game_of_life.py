from gameoflife import GameOfLife


def test_init():
    seed = [(1, 4), (6, 7)]
    gof = GameOfLife(seed=seed)
    assert seed == gof.state
    # assert all(cell in gof.state for cell in seed)


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
    assert alive_cell not in gof.state


def test_live():
    alive_cell = (1, 4)
    seed = [(6, 7)]
    gof = GameOfLife(seed=seed)
    gof.live(alive_cell)
    assert alive_cell in gof.state


@pytest.mark.parametrize(['neighbors', 'count'], (
    ([(2, 2), (3, 4), (4, 3)], 3),
    ([(2, 2), (3, 4), (8, 9)], 2),
    ([], 0),
    ([(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)], 8),
    ([(1, 1), (1, 8), (6, 7)], 0)
))
def test_get_neighbors_count(neighbors, count):
    alive_cell = (3, 3)
    seed = [alive_cell] + neighbors
    gof = GameOfLife(seed=seed)
    assert gof.get_neighbors_count(alive_cell) == count
