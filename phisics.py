import pygame
import math
import random

width, height = 1920, 1080
ppm = height/4
g = (9.81 *ppm)/(60**2)
friction = 0.80
schaal = 1/ppm

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 20, False)
font_stats = pygame.font.SysFont("Arial", 30, True)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

y_pos = random.uniform(0, height)
x_pos = random.uniform(0, width)
y_speed = random.uniform(-30, 30)
x_speed = random.uniform(-30, 30)
radius = 0.0327
radius_draw = radius*ppm
p = 1.225
A = math.pi * radius**2
c = 0.47

f_y = 0
f_x = 0

m = 0.057

y_speed_0 = 0
x_speed_0 = x_speed

c_rr = 0.04

a_rr = c_rr * g

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x_speed += random.uniform(-30, 30)
                y_speed += random.uniform(-30, -15)

    #krachten
    safe_x_speed = min(abs(x_speed), 100)
    safe_y_speed = min(abs(y_speed), 100)

    x_air_res = (0.5 * p * safe_x_speed ** 2 * A * c)*schaal
    y_air_res = (0.5 * p * safe_y_speed ** 2 * A * c)*schaal

    f_g = (m * g)

    if x_speed > 0:
        a_x = -x_air_res / m
    elif x_speed < 0:
        a_x = x_air_res / m
    else:
        a_x = 0

    a_y = f_g/m
    if y_speed > 0:
        a_y += -y_air_res / m
    elif y_speed < 0:
        a_y += y_air_res / m

    x_speed += a_x
    y_speed += a_y

    x_pos += x_speed
    y_pos += y_speed

    if y_pos + radius_draw >= height:
        y_pos = height - radius_draw
        if abs(y_speed) > 0.5:
            y_speed *= friction
            y_speed *= -1
        else:
            y_pos = height - radius_draw
            y_speed = 0
            if x_speed > 0:
                x_speed -= a_rr
            if x_speed < 0:
                x_speed += a_rr


            if abs(x_speed) < 0.1:
                x_speed = 0


    if y_pos - radius_draw <= 0:
        y_pos = radius_draw
        y_speed = -(y_speed * friction)
        x_speed = x_speed * friction

    if x_pos + radius_draw > width:
        x_pos = width - radius_draw

        y_speed =  (y_speed * friction)
        x_speed =  - (x_speed * friction)

    if x_pos - radius_draw <= 0:
        x_pos = radius_draw

        y_speed = (y_speed * friction)
        x_speed = - (x_speed * friction)




    if y_speed == 0:
        g = 0
    else:
        g = (9.81 *ppm)/(60**2)

    red = (255, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, green, (int(x_pos), int(y_pos)), radius_draw)
    pygame.draw.line(screen, red, (0, height/2),(20,height/2) ,5)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 4), (20, height / 4), 5)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 4 * 3), (20, height / 4 * 3), 5)
    pygame.draw.line(screen, (255, 0, 0), (0, height), (20, height), 5)
    pygame.draw.line(screen, (255, 0, 0), (0, 0), (20, 0), 5)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20), (10, height / 20), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 2), (10, height / 20 * 2), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 3), (10, height / 20 * 3), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 4), (10, height / 20 * 4), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 6), (10, height / 20 * 6), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 7), (10, height / 20 * 7), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 8), (10, height / 20 * 8), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 9), (10, height / 20 * 9), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 11), (10, height / 20 * 11), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 12), (10, height / 20 * 12), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 13), (10, height / 20 * 13), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 14), (10, height / 20 * 14), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 16), (10, height / 20 * 16), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 17), (10, height / 20 * 17), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 18), (10, height / 20 * 18), 2)
    pygame.draw.line(screen, (255, 0, 0), (0, height / 20 * 19), (10, height / 20 * 19), 2)

    pygame.draw.line(screen, red, (int(x_pos), int(y_pos)), (int(x_pos) + x_speed * 60, int(y_pos) + y_speed * 60), 2)

    screen.blit(font.render("0m", True, white), (40, height - 13))
    screen.blit(font.render("1m", True, white), (40, height/4*3 - 13))
    screen.blit(font.render("2m", True, white), (40, height/2 - 13))
    screen.blit(font.render("3m", True, white), (40, height/4 - 13))
    screen.blit(font.render("4m", True, white), (40, 0 - 13))
    #screen.blit(font.render(f"x: {round(x_pos)}, y: {round(y_pos)}, v: {(((x_speed)**2 + (y_speed)**2)**0.5):.2f}ms^-1", True, white), (width/2, 13))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
