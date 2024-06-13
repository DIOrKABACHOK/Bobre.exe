# coding: utf-8
# license: GPLv3

import math

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    force = 0
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj or body.type == obj.type:
            continue
        dx = obj.x - body.x
        dy = obj.y - body.y
        r = (dx ** 2 + dy ** 2) ** 0.5
        if r == 0:
            continue
        if body.system != obj.system or (body.con != obj.con and ((body.con != 'no' and obj.con.startswith('pr')) or (body.con.startswith('pr') and obj.con != 'no'))) or (body.type == 'satellite' and obj.type == 'star') or (body.type == 'star' and obj.type == 'satellite'):
            force = 0
        elif body.system == obj.system and body.con == obj.con and ((body.type == 'planet' and obj.type == 'satellite') or (body.type == 'satellite' and obj.type == 'planet')):
            force = 3.5433230893149516e+22
        elif body.system == obj.system and ((body.type == 'planet' and obj.type == 'star') or (body.type == 'star' and obj.type == 'planet')) and (body.con != obj.con and (body.con == 'no' or obj.con == 'no')):
            force = gravitational_constant * ((body.m * obj.m) / r ** 2)
        # print(body.type, obj.type)
        # print(force)
        # print('-----------')
        theta = math.atan2(dy, dx)
        body.Fx += force * math.cos(theta)
        body.Fy += force * math.sin(theta)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.x += body.Vx * dt + 0.5 * ax * dt ** 2
    body.Vx += ax * dt
    body.y += body.Vy * dt + 0.5 * ay * dt ** 2
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
