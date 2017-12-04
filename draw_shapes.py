"""Module draws different geometric shapes."""

import turtle


def create_draw_pointer(shape, color):
    """Create a pointer for drawing a shape.
    
    Args:
       shape - str, name of shape for pointer
       color - str, color for pointer

    Returns:
       pointer, instance of turtle.Turtle()
    """
    draw_pointer = turtle.Turtle()
    draw_pointer.shape(shape)
    draw_pointer.color(color)
    return draw_pointer


def draw_circle(pointer):
    """Draws a circle."""
    radius = 100
    pointer.circle(radius)


def draw_square(pointer):
    """Draws a square."""
    number_of_sides = 4
    distance = 100
    angle = 90

    for i in range(number_of_sides):
       pointer.forward(distance)
       pointer.right(angle)
        

def draw_triangle(pointer):
    """Draws a triangle."""
    number_of_sides = 3
    distance = 170
    angle = 120

    for i in range(number_of_sides):
        pointer.forward(distance)
        pointer.left(angle)


def draw_circle_of_squares(pointer):
    pointer.penup()
    pointer.setposition(250,200)
    pointer.pendown()
    for i in range(37):
        draw_square(pointer)
        pointer.right(10)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    square_pointer = create_draw_pointer('circle', 'yellow')
    draw_square(square_pointer)

    circle_pointer = create_draw_pointer('arrow', 'blue')
    draw_circle(circle_pointer)

    triangle_pointer = create_draw_pointer('turtle', 'green')
    draw_triangle(triangle_pointer)

    draw_circle_of_squares(square_pointer)

    window.exitonclick()


draw_art()
