"""This is the game alien invasion made in python with pygame """

from __future__ import annotations
from typing import Any
import sys
import pygame
import pygame.locals
from library import Position, Keyboard, Directions
from ships import Ship


surface_width: int = 1024
surface_height: int  = 614
surface: Any = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption("aliens!")
background_image: Any = pygame.image.load("./assets/background.png")
start_image: Any = pygame.image.load("./assets/start_screen.png")

image_player_path: str = "./assets/you_ship.png"
image_bullet_player_path: str = "./assets/you_pellet.png"

game_started: bool = False
game_ended: bool = False

def quit_game() -> None:
    "free the resources of the game"
    sys.exit()

def start_game() -> tuple[Ship, list[Ship], Keyboard, bool, bool]:
    "function called when the game start to initialize objects"
    start_keyboard: Keyboard = Keyboard(Directions())
    state_game_started = True
    state_game_ended = False
    start_player: Ship = \
        Ship(Position(surface_width/2.0, surface_height), [pygame, surface], \
        image_player_path, image_bullet_player_path)

    start_enemies: list[Ship] = []
    return start_player, start_enemies, start_keyboard, state_game_started, state_game_ended

def update_game(player: Ship, enemies: list[Ship], mouse_pos: tuple[int,int],\
 mouse_pressed: tuple[bool,...], keyboard_object: Keyboard) -> None:
    "This function update the objects of the game"
    if mouse_pressed[0]:
        # just for debugging
        #print(player.bullets_fired)
        player.fire()
        keyboard_object.state = False

    if  keyboard.get_state():
        if keyboard_object.directions.left:
            player.move_left()
        if keyboard_object.directions.right:
            player.move_right()
        if keyboard_object.directions.upp:
            player.move_up()
        if keyboard_object.directions.down:
            player.move_down()
    else:
        player.update_pos(Position(mouse_pos[0], mouse_pos[1]))

    bullets_fired_to_remove: list[int] = []
    for index, bullet_fired in enumerate(player.bullets_fired):
        bullet_fired.move_up()
        if bullet_fired.get_pos_y() < 0.0:
            bullets_fired_to_remove.append(index)

    for index in bullets_fired_to_remove:
        player.bullets_fired.pop(index)

    print(enemies)

def draw_game(player: Ship, enemies: list[Ship]) -> None:
    """Print player object and his bullets. Print enemies and the bullets
       of each enemy """
    surface.blit(background_image,(0,0))
    player.draw()
    for bullet_fired in player.bullets_fired:
        bullet_fired.draw()

    print(enemies)

while True:

    mouse_pressed_list: tuple[bool,...] = pygame.mouse.get_pressed()
    mouse_pos_list: tuple[int,int] = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == getattr(pygame.locals, "QUIT"):
            quit_game()
        elif event.type == getattr(pygame.locals, "KEYDOWN"):
            if event.key == getattr(pygame.locals, "K_ESCAPE"):
                quit_game()
            elif event.key == getattr(pygame.locals, "K_RETURN"):
                player_object,enemies_list, keyboard, \
                game_started, game_ended  = start_game()
            if game_started and event.key == getattr(pygame.locals, "K_f"):
                player_object.fire()
            if event.key == getattr(pygame.locals, "K_UP"):
                keyboard.directions.upp = True
            if event.key == getattr(pygame.locals, "K_DOWN"):
                keyboard.directions.down = True
            if event.key == getattr(pygame.locals, "K_LEFT"):
                keyboard.directions.left= True
            if event.key == getattr(pygame.locals, "K_RIGHT"):
                keyboard.directions.right = True
        elif event.type == getattr(pygame.locals, "KEYUP"):
            if event.key == getattr(pygame.locals, "K_LEFT"):
                keyboard.directions.left = False
            elif event.key == getattr(pygame.locals, "K_RIGHT"):
                keyboard.directions.right = False
            elif event.key == getattr(pygame.locals, "K_UP"):
                keyboard.directions.upp = False
            elif event.key == getattr(pygame.locals, "K_DOWN"):
                keyboard.directions.down = False
    if not game_started and not game_ended:
        surface.blit(start_image,(0,0))
    elif game_started and not game_ended:

        update_game(player_object, enemies_list, mouse_pos_list,\
                     mouse_pressed_list, keyboard)
        draw_game(player_object, enemies_list)

    pygame.time.Clock().tick(20)
    pygame.display.update()
