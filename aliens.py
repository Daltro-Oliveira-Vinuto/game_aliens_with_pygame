from __future__ import annotations
import sys
import pygame
import pygame.locals
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_RETURN, K_ESCAPE # type: ignore
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_f # type: ignore
from typing import Any

from ships import Ship

class Directions:
    def __init__(self, left: bool=False, right:bool=False, \
        up:bool =False, down:bool =False) -> None:
        self.left: bool = left
        self.right: bool  = right 
        self.up: bool= up 
        self.down: bool = down 

class Keyboard:

    def __init__(self, directions: Directions) -> None:
        self.directions = directions 
        self.state: bool = False
        self.state = self.get_state()

    def get_state(self) -> bool:
        if self.directions.up or\
        self.directions.down or\
        self.directions.left or\
        self.directions.down or \
        self.state:
            self.state = True
        else:
            self.state = False 

        return self.state 

pygame.init()
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
    pygame.quit()
    sys.exit()

def start_game() -> tuple[Ship, list[Ship], Keyboard]:
    global game_started, game_ended

    keyboard: Keyboard = Keyboard(Directions())
    game_started = True
    game_ended = False
    player: Ship = \
        Ship(surface_width/2.0, surface_height, pygame, surface, \
        image_player_path, image_bullet_player_path)

    enemies: list[Ship] = []
    return player, enemies, keyboard

def update_game(player: Ship, enemies: list[Ship], mouse_pos: tuple[int,int], mouse_pressed: tuple[bool,...], keyboard: Keyboard) -> None:

    if mouse_pressed[0]:
        # just for debugging
        #print(player.bullets_fired)
        player.fire()
        keyboard.state = False

    if  keyboard.get_state():
        if keyboard.directions.left: player.move_left()
        if keyboard.directions.right: player.move_right()
        if keyboard.directions.up: player.move_up()
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


player: Ship
enemies: list[Ship]
keyboard: Keyboard
player, enemies, keyboard = start_game()
game_started = False # because start game sets this for True


while True:

    mouse_pressed: tuple[bool,...] = pygame.mouse.get_pressed()
    mouse_pos: tuple[int,int] = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT: 
            quit_game()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit_game()
            elif event.key == K_RETURN:
                player,enemies, keyboard  = start_game()
            if game_started and event.key == K_f:
                player.fire()
            if event.key == K_UP:
                keyboard.directions.up = True     
            if event.key == K_DOWN:
                keyboard.directions.down = True
            if event.key == K_LEFT:
                keyboard.directions.left= True 
            if event.key == K_RIGHT:
                keyboard.directions.right = True

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                keyboard.directions.left = False
            elif event.key == K_RIGHT:
                keyboard.directions.right = False
            elif event.key == K_UP:
                keyboard.directions.up = False  
            elif event.key == K_DOWN:
                keyboard.directions.down = False
            
    if not game_started and not game_ended:
        surface.blit(start_image,(0,0))
    elif game_started and not game_ended:

        update_game(player, enemies, mouse_pos, mouse_pressed, keyboard)
        draw_game(player, enemies)

    pygame.time.Clock().tick(40)
    pygame.display.update()


    