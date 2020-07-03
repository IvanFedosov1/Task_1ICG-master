# -*- coding: utf-8 -*-
import math

from PIL import Image
import re
from obj import *
from revert_fun import turn

scr_x = 800  # Ширина картинки
scr_y = scr_x  # Высота картинки


def show_face(angle):
    half_scr_x = int(scr_x / 2)
    half_scr_y = int(scr_y / 2)
    texture_img = Image.open('african_head_diffuse.tga')
    texture = texture_img.load()
    f = open('face.obj', 'r')
    lines = f.read()
    points = []
    textures = []
    screen = Screen(scr_x, scr_y)
    for line in lines.split('\n'):
        try:
            v, x, y, z = re.split('\s+', line)
        except ValueError:
            continue
        if v == 'v':
            x, z = turn(float(x), float(z), angle)
            x = int((float(x) + 1) * half_scr_x)
            y = int((float(y) + 1) * half_scr_y)
            z = float(z) + 1
            points.append((x, y, z))
        if v == 'vt':
            u = float(x) * texture_img.width
            v = (1 - float(y)) * texture_img.height
            textures.append((u, v))
        if v == 'f':
            indexes = [[int(j) - 1 for j in i.split('/')] for i in (x, y, z)]
            tr_points = []
            for i in range(3):
                params = points[indexes[i][0]] + textures[indexes[i][1]]
                tr_points.append(screen.point(*params))
            screen.triangle(tr_points, texture)
    screen.img.show()


print("Введите угол поворота")
try:
    angle = int(input())
    if -90 < angle < 90:
        show_face(math.radians(angle))
    else:
        print("Нормальный угол введи")
except:
    print("Ты точно угол ввел?")
