"Modules with the classes for Projectiles and Ships objects"
from __future__ import annotations
from typing import Any

class Projectile:
    "Class with the attributes and behaviors of the Projectile objects"
    def __init__(self, pos_x: float, pos_y:float, pygame: Any, \
        surface: Any, image_path: str, speed: float=10.0,) -> None:
        self.pos_x: float = pos_x
        self.pos_y: float = pos_y
        self.pygame: Any  = pygame
        self.surface: Any = surface
        self.image_path: str = image_path
        self.speed: float = speed
        self._image: Any = self.pygame.image.load(self.image_path)
        image_size: tuple[int,int] = self._image.get_size()
        self.image_width: int = image_size[0]
        self.image_height: int = image_size[1]

    def __del__(self) -> None:
        return None

    def draw(self) -> None:
        "Draw projectile object"
        self.surface.blit(\
            self._image,\
            (self.pos_x-self.image_width, self.pos_y-self.image_height))

    def update_pos(self, position: tuple[float,float]) -> None:
        "update position of the object"
        self.pos_x = position[0]
        self.pos_y = position[1]

    def get_pos(self) -> tuple[float, float]:
        "return position of the object"
        return (self.pos_x, self.pos_y)

    def get_pos_x(self) -> float:
        "return vertical position(pos_x) of the object"
        return self.pos_x

    def get_pos_y(self) -> float:
        "return horizontal position(pos_y) of the object"
        return self.pos_y

    def move_up(self) -> None:
        "move the object up"
        self.pos_y -= self.speed

    def move_down(self) -> None:
        "move the object down"
        self.pos_y += self.speed

    def move_left(self) -> None:
        "move the object left"
        self.pos_x -= self.speed

    def move_right(self) -> None:
        "move the object right"
        self.pos_x += self.speed


class Ship(Projectile):
    "Class with the attributes and behaviors of the Ships objects"
    def __init__(self,pos_x: float, pos_y:float , pygame: Any ,surface: Any ,\
        image_path: str, image_bullet_path: str) -> None:
        Projectile.__init__(self, pos_x,pos_y,pygame, surface, image_path)
        self.image_bullet_path: str = image_bullet_path
        self.start_bullets_fired()

    def __del__(self) -> None:
        return None

    def start_bullets_fired(self):
        "initialize bullets_fired list to empty"
        self.bullets_fired: list[Projectile] = []

    def fire(self) -> None:
        "create the object projectile after each fire and append him to bullets_fired list"
        fire_position: tuple[float,float] = \
            (self.pos_x - self.image_width/(2.0), self.pos_y-self.image_height)
        pos_x: float = fire_position[0]
        pos_y: float = fire_position[1]

        new_bullet_fired: Projectile = \
            Projectile(pos_x, pos_y, self.pygame,self.surface, self.image_bullet_path,speed=10)

        self.bullets_fired.append(new_bullet_fired)
        