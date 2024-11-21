import pygame
from pygame.locals import *
import math as m

pygame.init()

screen_width, screen_height = (1600, 900)
fps_limit = 165
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Raycasting - FPS: " + str(fps_limit))
clock = pygame.time.Clock()

map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

view_angle = 90
player_x, player_y = (1.5, 1.5)
view_rotation = 0
mouse_sensitivity = m.pi / 256
speed = 0.01
movement_precision = 0.01

move_forward, move_backward, move_left, move_right = False, False, False, False

mouse_sens = 0.002

running = True
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

def is_wall(x, y):
    if map_data[int(x)][int(y)] == 1:
        return True
    return False

while running:
    clock.tick(fps_limit)
    pygame.display.update()
    pygame.display.set_caption("Raycasting - FPS: " + str(round(clock.get_fps())))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_w:
                move_forward = True
            if event.key == pygame.K_s:
                move_backward = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
        if event.type == KEYUP:
            if event.key == pygame.K_w:
                move_forward = False
            if event.key == pygame.K_s:
                move_backward = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False

    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    view_rotation += mouse_dx * mouse_sens
    up_down_rotation = m.sin(mouse_dy * mouse_sens)

    if move_forward:
        new_x = player_x + speed * m.cos(view_rotation)
        new_y = player_y + speed * m.sin(view_rotation)
        if not is_wall(new_x, new_y):
            player_x = new_x
            player_y = new_y

    if move_backward:
        new_x = player_x - speed * m.cos(view_rotation)
        new_y = player_y - speed * m.sin(view_rotation)
        if not is_wall(new_x, new_y):
            player_x = new_x
            player_y = new_y

    if move_left:
        new_x = player_x + speed * m.cos(view_rotation - m.pi / 2)
        new_y = player_y + speed * m.sin(view_rotation - m.pi / 2)
        if not is_wall(new_x, new_y):
            player_x = new_x
            player_y = new_y

    if move_right:
        new_x = player_x + speed * m.cos(view_rotation + m.pi / 2)
        new_y = player_y + speed * m.sin(view_rotation + m.pi / 2)
        if not is_wall(new_x, new_y):
            player_x = new_x
            player_y = new_y

    screen.fill((0, 0, 0))

    for i in range(view_angle + 1):
        ray_angle = view_rotation + m.radians(i - view_angle / 2)
        x, y = player_x, player_y
        sin, cos = movement_precision * m.sin(ray_angle), movement_precision * m.cos(ray_angle)
        distance = 0
        while True:
            x, y = (x + cos, y + sin)
            distance += 1
            if map_data[int(x)][int(y)] != 0:
                tile = map_data[int(x)][int(y)]
                dist = distance
                distance = distance * m.cos(m.radians(i - view_angle / 2))
                height = (10 / distance * 2500)
                break
        if dist / 2 > 255:
            dist = 510
        pygame.draw.line(screen, (255 - dist / 2, 255 - dist / 2, 255 - dist / 2),
                         (i * (screen_width / view_angle), (screen_height / 2) + height),
                         (i * (screen_width / view_angle), (screen_height / 2) - height),
                         width=int(screen_width / view_angle))

    pygame.display.flip()

pygame.quit()
