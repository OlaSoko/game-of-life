

class GameOfLife:

    def __init__(self, seed):
        self._state = set(seed)

    @property
    def state(self):
        return self._state

    def tick(self):
        """
        Inspects the surroundings of all alive cells and changes their
        state to alive (2 or 3 neighbours present) or dead (other
        number of neighbours).

        Musi wiedzieć jaki jest stan, sprawdzić sąsiadów każdej żywej
        komórki i odpowiednio zmienić ich stany.
        Zaimplementować na niedzielę.
        """
        pass

    def die(self, cell):
        """
        Changes the state of a cell to 'dead' (deletes it from _state)
        """
        self._state.remove(cell)

    def live(self, cell):
        """
        Changes the state of a cell to 'alive' (adds it to _state)
        """
        self._state.add(cell)

    def is_alive(self, cell):
        """
        Checks if a given cell is alive or not.
        """
        return cell in self._state

    def get_neighbours(self, cell):
        """
        Returns coordinates of all neighbours of a given cell.
        """
        pass

    def get_neighbors_count(self, cell):
        """
        Version 1
        Counts the number of alive cells around a given cell.
        """
        x, y = cell
        counter = 0
        for i in range(-1, 2):  # (-1, 0, 1)
            for j in range(-1, 2):  # (-1, 0, 1)
                neighbour = (x + i, y +j)
                if self.is_alive(neighbour): # neighbour in self._state
                    if neighbour == cell:
                        continue
                    counter += 1
        return counter

    def get_neighbours_count(self, cell):
        """
        Version 2
        Counts the number of alive cells around a given cell.
        """
        x, y = cell

        possible_neighbours = [
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y),                 (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
        ]

        # possible_neighbours = [
        #     (x + i, y +j)
        #     for i in range(-1, 2)
        #     for j in range(-1, 2)
        #     if i != 0 and j!= 0
        # ]

        return sum(self.is_alive(n) for n in possible_neighbours)

    def __str__(self):
        """
        Returns a representation of the current state of the game.
        """
        pass
