"Module library has classes auxiliaries to the game aliens"

class Position:
    "Class to handle de position in 2D of a particle"
    def __init__(self, pos_x: float, pos_y: float) -> None:
        self._pos_x: float = pos_x
        self._pos_y: float = pos_y

    @property
    def pos_x(self) -> float:
        "Return _pos_y in a encapsulated manner"
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value: float) -> None:
        self._pos_x = value

    @property
    def pos_y(self) -> float:
        "Return _pos_y in a encapsulated manner"
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value: float) -> None:
        self._pos_y = value

    def __str__(self):
        return f"{(self._pos_x, self._pos_y)}"
