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

class Directions:
    "This class allow simple access to directions to other objects"
    def __init__(self, left: bool=False, right:bool=False, \
    upp:bool =False, down:bool =False) -> None:
        self._left: bool = left
        self._right: bool = right
        self._upp: bool = upp
        self._down: bool = down

    def __str__(self):
        return f"(left={self.left}, right={self.right}, up={self.upp}, down={self.down})"

    @property
    def upp(self) -> bool:
        "encapusulate self._upp variable"
        return self._upp

    @upp.setter
    def upp(self, value:bool) -> None:
        self._upp = value

    @property
    def down(self) -> bool:
        "encapusulate self._down variable"
        return self._down

    @down.setter
    def down(self,value: bool) -> None:
        self._down = value

    @property
    def right(self) -> bool:
        "encapusulate self._right variable"
        return self._right

    @right.setter
    def right(self, value: bool) -> None:
        self._right = value

    @property
    def left(self) -> bool:
        "encapusulate self._left variable"
        return self._left

    @left.setter
    def left(self, value: bool) -> None:
        self._left = value

class Keyboard:
    "This class allows a convenient access to Keyboard to other objects using Directions"
    def __init__(self, directions: Directions) -> None:
        self.directions = directions
        self._state: bool = False
        self._state = self.get_real_state()

    def get_real_state(self) -> bool:
        "Return True if the self_state is True or any of the directions are True"
        if self.directions.upp or\
        self.directions.down or\
        self.directions.left or\
        self.directions.right or \
        self._state:
            self._state = True
        else:
            self._state = False

        return self._state

    @property
    def state(self) -> bool:
        "encapusulate self._state variable"
        return self._state

    @state.setter
    def state(self, value: bool) -> None:
        self._state = value

    def __str__(self):
        return self.directions.__str__()+f", state={self.state}"
