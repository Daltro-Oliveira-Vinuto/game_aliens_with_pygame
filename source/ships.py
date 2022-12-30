"Module with the classes for Projectiles and Ships objects"
from __future__ import annotations
from typing import Any
from library import Position

#pylint: disable=too-many-arguments

class Projectile:
    "Class with the attributes and behaviors of the Projectile objects"
    def __init__(self, position: Position, stage: Any = None,\
     image_path: str = "", speed: float = 10) -> None:
        self.position: Position = position
        self.image_path: str = image_path
        self.speed = speed
        if stage is not None and len(stage) >= 2:
            self.pygame: Any  = stage[0]
            self.surface: Any = stage[1]
            if self.pygame is not None:
                self.image: Any = self.pygame.image.load(self.image_path)

    def __del__(self) -> None:
        return None

    def draw(self) -> None:
        "Draw projectile object"
        self.surface.blit(self.image,\
            (self.position.pos_x-self.image.get_size()[0],
             self.position.pos_y-self.image.get_size()[1])
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
        self.position.pos_y -= self.speed

    def move_down(self) -> None:
        "move the object down"
        self.position.pos_y += self.speed

    def move_left(self) -> None:
        "move the object left"
        self.position.pos_x -= self.speed

    def move_right(self) -> None:
        "move the object right"
        self.position.pos_x += self.speed


class Ship(Projectile):
    "Class with the attributes and behaviors of the Ships objects"
    def __init__(self, position: Position , stage: Any,\
        image_path: str, image_bullet_path: str, speed: float=10) -> None:
        Projectile.__init__(self, position, stage, image_path, speed)
        self.image_bullet_path: str = image_bullet_path
        self.start_bullets_fired()
        self.speed = speed

    def __del__(self) -> None:
        return None

    def start_bullets_fired(self) -> None:
        "initialize bullets_fired list to empty"
        self.bullets_fired: list[Projectile] = []

    def shoot(self, music_path: str) -> None:
        "create the object projectile after each fire and append him to bullets_fired list"
        fire_music = self.pygame.mixer.Sound(music_path)
        fire_music.set_volume(0.5)
        fire_music.play()
        fire_position: tuple[float,float] = \
            (self.position.pos_x - self.image.get_size()[0]/(2.0),\
             self.position.pos_y-self.image.get_size()[1])
        fire_pos_x: float = fire_position[0]
        fire_pos_y: float = fire_position[1]

        new_bullet_fired: Projectile = \
            Projectile(Position(fire_pos_x, fire_pos_y), \
                [self.pygame,self.surface],self.image_bullet_path, self.speed)

        self.bullets_fired.append(new_bullet_fired)

    def fire(self):
        "this function should be overrided by his sons in the inherintance hierarchy"
        self.shoot("/")

class Player(Ship):
    "This is a son of Ship class for the player objects"
    def __init__(self, position: Position, stage: Any, \
        image_path: str, image_bullet_path: str, speed: float = 10) -> None:
        Ship.__init__(self, position, stage, image_path, \
            image_bullet_path, speed)

    def fire(self):
        self.shoot("./sounds/player_laser.wav")


class Enemy(Ship):
    "This is a son of Ship class for the enemies objects"
    def __init__(self, position: Position, stage: Any, \
        image_path: str, image_bullet_path: str, speed: float = 10) -> None:
        Ship.__init__(self, position, stage, image_path, \
            image_bullet_path, speed)

    def fire(self):
        self.shoot("./sounds/enemy_laser.wav")
