from turtle import Turtle
POSITIONS = [(0,0), (-20,0), (-40,0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake :
    
    def __init__(self):
        self.segments = []
        self.createSnake()

    def createSnake(self):
        for position in POSITIONS:
           self.add_segment(position) 

    def add_segment(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x,y)
        self.segments[0].forward(20)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        