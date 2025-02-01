import sys
import math
import turtle
from turtle import Turtle

def draw_pythagoras_tree(t: Turtle, branch_length, level):
    if level == 0:
        return

    # Малюємо стовбур
    t.forward(branch_length)

    # Зберігаємо поточну позицію і напрямок
    pos = t.position()
    angle = t.heading()

    # Малюємо ліву гілку
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Повертаємося до початкової позиції і напрямку
    t.setposition(pos)
    t.setheading(angle)

    # Малюємо праву гілку
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Повертаємося до початкової позиції і напрямку
    t.setposition(pos)
    t.setheading(angle)

def draw_pythagoras_tree_fractal(level, branch_length=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Початкова орієнтація
    t.penup()
    t.goto(0, -200)  # Початкова позиція
    t.pendown()
    try:
        draw_pythagoras_tree(t, branch_length, level)
    except Exception as _:
        print("Stop drawing")

    window.mainloop()

def main():
    if len(sys.argv) == 2:
        level = int(sys.argv[1])
        draw_pythagoras_tree_fractal(level)
    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()
