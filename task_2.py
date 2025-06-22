import turtle

def draw_tree(t, branch_length, level):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Зберігаємо поточну позицію і напрямок
    pos = t.position()
    heading = t.heading()

    # Ліва гілка
    t.left(45)
    draw_tree(t, branch_length * 0.8, level - 1)

    # Повертаємось
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

    # Права гілка
    t.right(45)
    draw_tree(t, branch_length * 0.8, level - 1)

    # Повертаємось у вихідну точку
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

def draw_fractal_tree(level, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)

    # Початкова позиція та напрямок (вгору)
    t.penup()
    t.goto(0, -window.window_height() // 2 + 10)
    t.setheading(90)
    t.pendown()

    draw_tree(t, size, level)
    t.hideturtle()

    window.mainloop()


if __name__ == "__main__":
# Отримання рівня рекурсії від користувача
    try:
        user_level = int(input("Введіть рівень рекурсії (наприклад: 8): "))
        draw_fractal_tree(user_level)
    except ValueError:
        print("Будь ласка, введіть число")