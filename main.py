from turtle import Turtle, Screen


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    snake_segments = []
    position = 0

    for snake_segment in range(3):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.setposition(position, 0)
        snake_segments.append(snake_segment)
        position -= 20

    still_playing = True

    while still_playing:
        still_playing = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
