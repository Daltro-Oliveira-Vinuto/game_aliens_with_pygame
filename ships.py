from __future__ import annotations
from typing import Any

class Projectile:
    def __init__(self, x: float, y:float, pygame: Any, surface: Any,\
        image_path: str, speed: float=10.0) -> None:

        self.x: float = x
        self.y: float = y 
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
        self.surface.blit(\
            self._image,\
            (self.x-self.image_width, self.y-self.image_height))  

    def update_pos(self, position: tuple[float,float]) -> None:
        self.x = position[0]
        self.y = position[1]

    def get_pos(self) -> tuple[float, float]:
        return (self.x, self.y)

    def get_x(self) -> float:
        return self.x
    
    def get_y(self) -> float:
        return self.y

    def move_up(self) -> None:
        self.y -= self.speed
    
    def move_down(self) -> None:
        self.y += self.speed 

    def move_left(self) -> None:
        self.x -= self.speed

    def move_right(self) -> None:
        self.x += self.speed 


class Ship(Projectile):
    def __init__(self,x: float, y:float , pygame: Any ,surface: Any ,\
        image_path: str, image_bullet_path: str) -> None:
       Projectile.__init__(self, x,y,pygame, surface, image_path)
       self.image_bullet_path: str = image_bullet_path
       self.bullets_fired: list[Projectile] = []

    def __del__(self) -> None:
        return None 

    def fire(self) -> None:
        fire_position: tuple[float,float] = \
            (self.x - self.image_width/(2.0), self.y-self.image_height)
        x: float = fire_position[0]
        y: float = fire_position[1]

        new_bullet_fired: Projectile = \
            Projectile(x, y, self.pygame,self.surface, self.image_bullet_path,speed=10)

        self.bullets_fired.append(new_bullet_fired)


