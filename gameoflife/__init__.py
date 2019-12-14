

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
        pass

    def get_neighbors_count(self, cell):
        pass

    def __str__(self):
        pass
