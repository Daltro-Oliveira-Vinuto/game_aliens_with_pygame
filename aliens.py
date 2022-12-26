"""This is the game alien invasion made in python with pygame """

from __future__ import annotations
import sys
import pygame
import pygame.locals
#from pygame.locals import QUIT, KEYDOWN, KEYUP, K_RETURN, K_ESCAPE # type: ignore
#from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_f # type: ignore
from typing import Any

from ships import Ship

class Directions:
    "This class allow simple access to directions to other objects"
    def __init__(self, left: bool=False, right:bool=False, \
        upp:bool =False, down:bool =False) -> None:
        self._left: bool = left
        self._right: bool = right
        self._upp: bool = upp
        self._down: bool = down

    @property
    def upp(self) -> bool:
        "encapusulate self._upp variable"
        return self._upp
    @property
    def down(self) -> bool:
        "encapusulate self._down variable"
        return self._down
    @property
    def right(self) -> bool:
        "encapusulate self._right variable"
        return self._right
    @property
    def left(self) -> bool:
        "encapusulate self._left variable"
        return self._left


class Keyboard:
    "This class allows a convenient access to Keyboard to other objects using Directions"
    def __init__(self, directions: Directions) -> None:
        self.directions = directions
        self._state: bool = False
        self._state = self.get_state()

    def get_state(self) -> bool:
        "Return the actual state of Directions using a boolean"
        if self.directions.upp or\
        self.directions.down or\
        self.directions.left or\
        self.directions.down or \
        self._state:
            self._state = True
        else:
            self._state = False

        return self._state

    @property
    def state(self) -> bool:
        "encapusulate self._state variable"
        return self._state

surface_width: int = 1024
surface_height: int  = 614
surface: Any = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption("aliens!")
background_image: Any = pygame.image.load("./assets/background.png")
start_image: Any = pygame.image.load("./assets/start_screen.png")

game_started: bool = False
game_ended: bool = False

image_player_path: str = "./assets/you_ship.png"
image_bullet_player_path: str = "./assets/you_pellet.png"


def quit_game() -> None:
    "free the resources of the game"
    sys.exit()

def start_game() -> tuple[Ship, list[Ship], Keyboard]:
    "function called when the game start to initialize objects"

    start_keyboard: Keyboard = Keyboard(Directions())
    game_started = True
    game_ended = False
    start_player: Ship = \
        Ship(surface_width/2.0, surface_height, pygame, surface, \
        image_player_path, image_bullet_player_path)

    start_enemies: list[Ship] = []
    return start_player, start_enemies, start_keyboard

def update_game(player: Ship, enemies: list[Ship], mouse_pos: tuple[int,int],\
 mouse_pressed: tuple[bool,...], keyboard: Keyboard) -> None:

    if mouse_pressed[0]:
        # just for debugging
        #print(player.bullets_fired)
        player.fire()
        keyboard.state = False

    if  keyboard.get_state():
        if keyboard.directions.left: player.move_left()
        if keyboard.directions.right: player.move_right()
        if keyboard.directions.upp: player.move_up()
        if keyboard.directions.down: player.move_down()
    else:
        player.update_pos(mouse_pos)

    bullets_fired_to_remove: list[int] = []
    for id, bullet_fired in enumerate(player.bullets_fired):
        bullet_fired.move_up()
        if bullet_fired.get_y() < 0.0:
            bullets_fired_to_remove.append(id)

    for id in bullets_fired_to_remove:
        player.bullets_fired.pop(id)


def draw_game(player: Ship, enemies: list[Ship]) -> None:
    surface.blit(background_image,(0,0))
    player.draw()
    for bullet_fired in player.bullets_fired:
        bullet_fired.draw()


while True:

    mouse_pressed: tuple[bool,...] = pygame.mouse.get_pressed()
    mouse_pos: tuple[int,int] = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            quit_game()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                quit_game()
            elif event.key == pygame.locals.K_RETURN:
                player,enemies, keyboard  = start_game()
            if game_started and event.key == pygame.locals.K_f:
                player.fire()
            if event.key == pygame.locals.K_UP:
                keyboard.directions.upp = True
            if event.key == pygame.locals.K_DOWN:
                keyboard.directions.down = True
            if event.key == pygame.locals.K_LEFT:
                keyboard.directions.left= True
            if event.key == pygame.locals.K_RIGHT:
                keyboard.directions.right = True

        elif event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_LEFT:
                keyboard.directions.left = False
            elif event.key == pygame.locals.K_RIGHT:
                keyboard.directions.right = False
            elif event.key == pygame.locals.K_UP:
                keyboard.directions.upp = False
            elif event.key == pygame.locals.K_DOWN:
                keyboard.directions.down = False
    if not game_started and not game_ended:
        surface.blit(start_image,(0,0))
    elif game_started and not game_ended:

        update_game(player, enemies, mouse_pos, mouse_pressed, keyboard)
        draw_game(player, enemies)

    pygame.time.Clock().tick(40)
    pygame.display.update()
