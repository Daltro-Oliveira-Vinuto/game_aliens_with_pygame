"Module with the classes for Projectiles and Ships objects"
from __future__ import annotations
from typing import Any
from library import Position

class Projectile:
    "Class with the attributes and behaviors of the Projectile objects"
    speed = 10
    def __init__(self, position: Position, stage: list[Any], image_path: str) -> None:
        self.position: Position = position
        self.pygame: Any  = stage[0]
        self.surface: Any = stage[1]
        self.image_path: str = image_path
        self._image: Any = self.pygame.image.load(self.image_path)
    def __del__(self) -> None:
        return None

    def draw(self) -> None:
        "Draw projectile object"
        self.surface.blit(self._image,\
            (self.position.pos_x-self._image.get_size()[0],
             self.position.pos_y-self._image.get_size()[1])
            )


    def update_pos(self, position: Position) -> None:
        "update position of the object"
        self.position.pos_x = position.pos_x
        self.position.pos_y = position.pos_y

    def get_pos(self) -> tuple[float, float]:
        "return position of the object"
        return (self.position.pos_x, self.position.pos_y)

    def get_pos_x(self) -> float:
        "return vertical position(position.pos_x) of the object"
        return self.position.pos_x

    def get_pos_y(self) -> float:
        "return horizontal position(position.pos_y) of the object"
        return self.position.pos_y

    def move_up(self) -> None:
        "move the object up"
        self.position.pos_y -= Projectile.speed

    def move_down(self) -> None:
        "move the object down"
        self.position.pos_y += Projectile.speed

    def move_left(self) -> None:
        "move the object left"
        self.position.pos_x -= Projectile.speed

    def move_right(self) -> None:
        "move the object right"
        self.position.pos_x += Projectile.speed


class Ship(Projectile):
    "Class with the attributes and behaviors of the Ships objects"
    def __init__(self, position: Position , stage: list[Any],\
        image_path: str, image_bullet_path: str) -> None:
        Projectile.__init__(self, position, stage, image_path)
        self.image_bullet_path: str = image_bullet_path
        self.start_bullets_fired()

    def __del__(self) -> None:
        return None

    def start_bullets_fired(self) -> None:
        "initialize bullets_fired list to empty"
        self.bullets_fired: list[Projectile] = []

    def fire(self) -> None:
        "create the object projectile after each fire and append him to bullets_fired list"
        fire_position: tuple[float,float] = \
            (self.position.pos_x - self._image.get_size()[0]/(2.0),\
             self.position.pos_y-self._image.get_size()[1])
        fire_pos_x: float = fire_position[0]
        fire_pos_y: float = fire_position[1]

        new_bullet_fired: Projectile = \
            Projectile(Position(fire_pos_x, fire_pos_y), \
                [self.pygame,self.surface],self.image_bullet_path)

        self.bullets_fired.append(new_bullet_fired)
        