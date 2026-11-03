# def greet():
#     print("hello user")

# greet()



# def sum(a,b):

#     print(a + b)

# sum(12,10)    



# num1 = int(input("enter first num: "))
# operation = input("+,-,*,/")
# num2 = int(input("enter second num: "))
# sum(num1,num2)


# def users(name : str, age : int ):
#     print("Name: ", name)
#     print("Age: " ,age )
# # users()
# users("john", 21)


# def user(name = "user"):
#     print(f'hello {name}')

# user("ali")    





# def add(a,b):

#     return a + b

# result = add(5,5)    
# print(result)

from turtle import *
from colorsys import hsv_to_rgb

colormode(1.0)
penup()
setposition(0, 0)
pendown()
speed(0)
bgcolor('black')
pensize(3)

n = 100
h = 0

for j in range(120):        
    for i in range(4):      
        color(hsv_to_rgb(h, 1, 1))
        h += 0.003
        circle(40 + i * 5, 90)
        forward(250)
        left(90)
    rt(10)

hideturtle()
done()

# import pygame
# import math

# pygame.init()

# WIDTH, HEIGHT = 1000, 650
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Mouse Follow Skeleton")

# clock = pygame.time.Clock()
# BG = (8, 4, 30)
# BONE = (205, 225, 255)
# GLOW = (90, 100, 255)

# # Creature body segments
# segments = [
#     [500 - i * 8, 320] for i in range(48)
# ]

# head_x, head_y = 500.0, 320.0
# running = True


# def draw_line(a, b, color=BONE, width=2):
#     pygame.draw.line(
#         screen, color,
#         (int(a[0]), int(a[1])),
#         (int(b[0]), int(b[1])), width
#     )


# def draw_creature():
#     # Backbone and ribs
#     for i in range(len(segments) - 1):
#         p = segments[i]
#         q = segments[i + 1]

#         draw_line(p, q, BONE, 2)

#         dx = q[0] - p[0]
#         dy = q[1] - p[1]
#         angle = math.atan2(dy, dx)

#         rib_len = max(4, 17 - i * 0.22)

#         for side in (-1, 1):
#             a = angle + side * 1.15
#             end = (
#                 p[0] + math.cos(a) * rib_len,
#                 p[1] + math.sin(a) * rib_len
#             )
#             draw_line(p, end, BONE, 1)

#         # Small legs
#         if i % 7 == 0 and i < 34:
#             side = 1 if i % 14 == 0 else -1
#             a = angle + side * 1.6

#             joint = (
#                 p[0] + math.cos(a) * 22,
#                 p[1] + math.sin(a) * 22
#             )
#             foot = (
#                 joint[0] + math.cos(a + 0.8) * 12,
#                 joint[1] + math.sin(a + 0.8) * 12
#             )

#             draw_line(p, joint)
#             draw_line(joint, foot)

#     # Skull
#     hx, hy = segments[0]
#     pygame.draw.circle(screen, BONE, (int(hx), int(hy)), 7)
#     pygame.draw.circle(
#         screen, BG, (int(hx + 2), int(hy - 2)), 2
#     )


# while running:
#     clock.tick(60)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Follow mouse cursor
#     mx, my = pygame.mouse.get_pos()

#     dx = mx - segments[0][0]
#     dy = my - segments[0][1]
#     distance = math.hypot(dx, dy)

#     if distance > 1:
#         speed = min(5, distance)
#         head_x = segments[0][0] + dx / distance * speed
#         head_y = segments[0][1] + dy / distance * speed

#     segments[0] = [head_x, head_y]

#     # Each bone follows the previous bone
#     for i in range(1, len(segments)):
#         px, py = segments[i - 1]
#         x, y = segments[i]

#         dx = x - px
#         dy = y - py
#         distance = math.hypot(dx, dy)

#         if distance > 0:
#             target_dist = 8
#             segments[i][0] = px + dx / distance * target_dist
#             segments[i][1] = py + dy / distance * target_dist

#     # Background
#     screen.fill(BG)

#     # Purple glow
#     glow_surface = pygame.Surface(
#         (WIDTH, HEIGHT), pygame.SRCALPHA
#     )
#     pygame.draw.circle(
#         glow_surface, (65, 45, 180, 35),
#         (WIDTH // 2, HEIGHT // 2), 270
#     )
#     screen.blit(glow_surface, (0, 0))

#     draw_creature()
#     pygame.display.flip()

# pygame.quit()

