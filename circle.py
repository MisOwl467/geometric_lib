import math


def area(r):
    """
    Вычисляет площадь круга.

    :param r: радиус круга
    :return: площадь круга (pi * r^2)

    Пример вызова:
        area(2)  # 12.566370614359172
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности.

    :param r: радиус круга
    :return: длина окружности (2 * pi * r)

    Пример вызова:
        perimeter(2)  # 12.566370614359172
    """
    return 2 * math.pi * r

