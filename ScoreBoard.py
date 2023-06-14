from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_value = 0  # Use a different name for the attribute
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):  # Rename the method to update the scoreboard
        self.clear()
        self.write(f"Score: {self.score_value}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):  # Add a method to increase the score
        self.score_value += 1
        self.update_scoreboard()


    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))