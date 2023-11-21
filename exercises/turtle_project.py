"""turtle project!"""
__author__ = "730670557"

from turtle import Turtle, colormode, done
colormode(255)
turtle: Turtle = Turtle()


def penposition(shape: Turtle, x: float, y: float) -> None:
    """This function helps simplify the code in the other functions, so everytime the penup, goto, and pendown functions aren't used."""
    shape.penup()
    shape.setheading(0.0)
    shape.goto(x, y)
    shape.pendown()


def drawRectangle(rect: Turtle, x: float, y: float, length: float, width: float) -> None:
    """This function changes the color to brown and also draws a rectangle."""
    penposition(rect, x, y)
    rect.color("brown")
    i = 0
    rect.begin_fill()
    while (i < 4):
        rect.forward(length)
        rect.right(90)
        rect.forward(width)
        i = i + 1
    rect.end_fill()


def drawTriangle(trig: Turtle, x: float, y: float, length: float) -> None:
    """This function changes the color to green and also draws a triangle."""
    penposition(trig, x, y)
    trig.color("green")
    i = 0
    trig.begin_fill()
    while (i < 3):
        trig.forward(length)
        trig.left(120)
        i = i + 1
    trig.end_fill()


def draw_square(squ: Turtle, x: float, y: float, width: float) -> None:
    """This function changes the color to black and also draws a circle."""
    squ.setheading(0.0)
    penposition(squ, x, y)
    squ.color("black")
    i: int = 0
    squ.begin_fill()
    while i < 4:
        squ.forward(width)
        squ.right(90)
        i = i + 1
    squ.end_fill()


def drawCircle(circ: Turtle, x: float, y: float, radius: float) -> None:
    """This function changes the color to yellow and also draws a circle."""
    circ.color("yellow")
    penposition(circ, x, y)
    circ.begin_fill()
    circ.circle(radius, extent=360)
    circ.end_fill()


def drawPentagon(pent: Turtle, x: float, y: float, length: float) -> None:
    """Part of the small lamppost in the ground."""
    """This function changes the color to yellow and also draws a pentagon."""
    pent.color("yellow")
    penposition(pent, x, y)
    i = 0
    pent.begin_fill()
    while (i < 5):
        pent.forward(length)
        pent.right(72)
        i = i + 1
    pent.end_fill()


def main() -> None:
    """This function puts all the code together. It uses the for i in range loop to simplify the code."""
    turtle: Turtle = Turtle()
    for i in range(0, 4):
        drawTriangle(turtle, 200 - (10 * i), 0 - (75 * i), 75 + (25 * i))
    for i in range(0, 4):
        drawTriangle(turtle, -200 - (10 * i), 0 - (75 * i), 75 + (25 * i)) 
    drawRectangle(turtle, -170, -225, 50, 25)
    drawRectangle(turtle, 225, -225, 50, 25)
    for i in range(0, 3):
        drawPentagon(turtle, 115 - (65 * i), -215, 25)
    for i in range(0, 3):
        draw_square(turtle, 115 - (65 * i), -250, 25)
    drawCircle(turtle, 50, 50, 100)
    done()


turtle.screen.bgcolor("light blue")

if __name__ == "__main__":
    main()