"""Draws flower of diamonds."""

import turtle


def create_pointer(shape, color):
    """Create a pointer.
    
    :Parameters:
        - shape: str, shape of pointer.
        - color: str, color of pointer.
    
    :Return:
        pointer, object of turtle.Turtle()
    """
    pointer = turtle.Turtle()
    pointer.shape(shape)
    pointer.color(color)
    return pointer


def draw_diamond(pointer):
    """Draws a diamond.
    
    :Parameters:
        - pointer: object of Turtle(), pointer for drawing a diamond."""
    for i in range(2):
        pointer.forward(100)
        pointer.right(60)
        pointer.forward(100)
        pointer.right(120)


def draw_flower():
    """Draws flower of diamonds."""
    flower_pointer = create_pointer('turtle', 'blue')
    for i in range(37):
        draw_diamond(flower_pointer)
        flower_pointer.right(10)
    flower_pointer.right(80)
    flower_pointer.forward(350)


def draw_art():
    """Main function for drawing."""
    window = turtle.Screen()
    window.bgcolor('yellow')

    draw_flower()

    window.exitonclick()


draw_art()
