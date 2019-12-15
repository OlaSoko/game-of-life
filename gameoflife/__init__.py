import os
import random
import time
from typing import Tuple, Iterable, Set

Position = Tuple[int, int]


class GameOfLife:

    def __init__(self, seed: Iterable[Position]):
        """
        :param seed: starting state of the game
        """
        self._state = set(seed)
        self._next_state = set(self._state)

    @property
    def state(self) -> Set[Position]:
        """
        Returns current game state,
        :return:  list of living cells' positions
        """
        return self._state

    @property
    def next_state(self) -> Set[Position]:
        """
        Returns current game state,
        :return:  list of living cells' positions
        """
        return self._next_state

    def tick(self):
        """
        Inspects the surroundings of all alive cells and changes their
        state to alive (2 or 3 neighbours present) or dead (other
        number of neighbours).

        Musi wiedzieć jaki jest stan, sprawdzić sąsiadów każdej żywej
        komórki i odpowiednio zmienić ich stany.
        Zaimplementować na niedzielę.
        """
        # collect all cells to be checked
        cells_to_check = set(self._state)
        for cell in self._state:
            neighbours = self.get_neighbours(cell)
            cells_to_check.update(neighbours)
        # update cells
        for cell in cells_to_check:
            neighbours_count = self.get_neighbours_count(cell)
            if self.is_alive(cell) and neighbours_count not in (2, 3):
                self.die(cell)
            elif neighbours_count == 3:
                self.live(cell)
        self._state = set(self._next_state)

    def die(self, cell: Position):
        """
        Changes the state of a cell to 'dead' (deletes it from _state)
        """
        self._next_state.remove(cell)

    def live(self, cell: Position):
        """
        Changes the state of a cell to 'alive' (adds it to _state)
        """
        self._next_state.add(cell)

    def is_alive(self, cell: Position) -> bool:
        """
        Checks if a given cell is alive or not.
        """
        return cell in self._state

    def get_neighbours(self, cell: Position) -> Iterable[Position]:
        """
        Returns coordinates of all neighbours of a given cell.
        """
        x, y = cell

        return [
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y),                 (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
        ]

    def get_neighbours_count(self, cell: Position) -> int:
        """
        Version 2
        Counts the number of alive cells around a given cell.
        """
        possible_neighbours = self.get_neighbours(cell)
        return sum(self.is_alive(n) for n in possible_neighbours)


def print_state(game, x1, y1, x2, y2):
    state = set(
        (x, y) for x, y in game.state if x1 <= x <= x2 and y1 <= y <= y2
    )
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if (x, y) in state:
                print('⭐️', end='')
            else:
                print('⬛️', end='')
        print()
    print(f'Total cells: {len(game.state)}.')


def play(game, x1, y1, x2, y2):

    while True:
        try:
            os.system('clear')  # cls na windows
            print_state(game, x1, y1, x2, y2)
            game.tick()
            time.sleep(0.25)
        except KeyboardInterrupt:
            raise


all_cells = [(x, y) for x in range(41) for y in range(16)]

game = GameOfLife(random.sample(all_cells, 300))

play(game, 0, 0, 40, 15)

