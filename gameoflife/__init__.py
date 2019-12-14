

class GameOfLife:

    def __init__(self, seed):
        self._state = set(seed)

    @property
    def state(self):
        return self._state

    def tick(self):
        pass

    def die(self, cell):
        pass

    def live(self, cell):
        pass

    def is_alive(self, cell):
        if cell in self._state:
            return True
        return False

    def get_neighbors_count(self, cell):
        pass

    def __str__(self):
        pass
