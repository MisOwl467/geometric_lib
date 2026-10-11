# Документация Geometric Lib

## Общее описание

**Geometric Lib** — лабараторная на *Python* для вычисления площади и периметра геометрических фигур.

> Каждая фигура описана в отдельном модуле. Функции принимают
> числовые параметры и возвращают результат вычислений.

Поддерживаемые фигуры:
1. Круг — `circle.py`
2. Квадрат — `square.py`
3. Прямоугольник — `rectangle.py`
4. Треугольник — `triangle.py`

## Math formulas

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Описание функций

### circle.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(r)` | `r` — радиус | площадь круга |
| `perimeter(r)` | `r` — радиус | длина окружности |

```python
import circle
circle.area(2)       # 12.566370614359172
circle.perimeter(2)  # 12.566370614359172
```

### square.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(a)` | `a` — сторона | площадь квадрата |
| `perimeter(a)` | `a` — сторона | периметр квадрата |

```python
import square
square.area(3)       # 9
square.perimeter(3)  # 12
```

### rectangle.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(a, b)` | `a`, `b` — стороны | площадь прямоугольника |
| `perimeter(a, b)` | `a`, `b` — стороны | периметр прямоугольника |

```python
import rectangle
rectangle.area(2, 3)       # 6
rectangle.perimeter(2, 3)  # 10
```

### triangle.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(a, h)` | `a` — основание, `h` — высота | площадь треугольника |
| `perimeter(a, b, c)` | `a`, `b`, `c` — стороны | периметр треугольника |

```python
import triangle
triangle.area(4, 3)          # 6.0
triangle.perimeter(3, 4, 5)  # 12
```

## История изменений

| Хеш коммита | Описание |
|---|---|
| `657afdd` | add README.md |
| `b7e1492` | add functions description to docs |
| `9593b9e` | add general description to docs |
| `46858af` | add docs to triangle.py |
| `2ed2208` | add docs to rectangle.py |
| `de79e33` | add docs to square.py |
| `60bc848` | add docs to circle.py |
| `d25e3ab` | add triangle.py and fix rectangle.py |
| `00dc1e3` | add rectangle.py |
| `d078c8d` | L-03: Docs added |
| `8ba9aeb` | L-03: Circle and square added |