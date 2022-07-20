from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.position = 0

        for self.snake_segment in range(3):
            self.snake_segment = Turtle(shape="square")
            self.snake_segment.penup()
            self.snake_segment.color("white")
            self.snake_segment.setposition(self.position, 0)
            self.snake_segments.append(self.snake_segment)
            self.position -= 20

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(20)
