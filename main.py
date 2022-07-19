from turtle import Turtle, Screen


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    turtle_squares = []
    position = 0

    for turtle_square in range(3):
        turtle_square = Turtle()
        turtle_square.shape("square")
        turtle_square.color("white")
        turtle_square.setposition(position, 0)
        position -= 20

    still_playing = True

    while still_playing:
        still_playing = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
