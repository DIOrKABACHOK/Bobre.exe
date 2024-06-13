# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet, Satellite


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            elif object_type == "satellite":
                satellite = Satellite()
                parse_satellite_parameters(line, satellite)
                objects.append(satellite)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy> (<отношение к системе>(если есть))

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    parts = line.split()[1:]

    star.R = int(parts[0])
    star.color = parts[1]
    star.m = float(parts[2])
    star.x = float(parts[3])
    star.y = float(parts[4])
    star.Vx = float(parts[5])
    star.Vy = float(parts[6])
    star.type = 'star'
    if len(parts) > 7:
        star.system = str(parts[7])
    else:
        star.system = '0'
    if len(parts) > 8:
        star.con = str(parts[8])
    else:
        star.con = 'no'


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy> (<отношение к системе>(если есть))

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    parts = line.split()[1:]

    planet.R = int(parts[0])
    planet.color = parts[1]
    planet.m = float(parts[2])
    planet.x = float(parts[3])
    planet.y = float(parts[4])
    planet.Vx = float(parts[5])
    planet.Vy = float(parts[6])
    planet.type = 'planet'
    if len(parts) > 7:
        planet.system = str(parts[7])
    else:
        planet.system = '0'
    if len(parts) > 8:
        planet.con = str(parts[8])
    else:
        planet.con = 'pr'


def parse_satellite_parameters(line, satellite):
    """Считывает данные о спутнике из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Satellite <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy> (<отношение к системе>(если есть))

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Satellite 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание спутника.
    **satellite** — объект спутника.
    """

    parts = line.split()[1:]

    satellite.R = int(parts[0])
    satellite.color = parts[1]
    satellite.m = float(parts[2])
    satellite.x = float(parts[3])
    satellite.y = float(parts[4])
    satellite.Vx = float(parts[5])
    satellite.Vy = float(parts[6])
    satellite.type = 'satellite'
    if len(parts) > 7:
        satellite.system = str(parts[7])
    else:
        satellite.system = '0'
    if len(parts) > 8:
        satellite.con = str(parts[8])
    else:
        satellite.con = 'pr'


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Satellite <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """

    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write(f"{obj.__class__.__name__} {obj.R} {obj.color} {obj.m:.2f} {obj.x} {obj.y} {obj.Vx} {obj.Vy} {obj.system} {obj.rel}\n")


if __name__ == "__main__":
    print("This module is not for direct call!")
