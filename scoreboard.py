from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open("data.txt") as data:
            self.high_level = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}, Highest level: {self.high_level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        if self.level > self.high_level:
            self.high_level = self.level
        self.level = 1
        self.update_scoreboard()

    def game_over(self):
        if self.level > self.high_level:
            self.high_level = self.level
            with open("data.txt", "w") as data:
                data.write(f"{self.high_level}")
            self.update_scoreboard()
        self.goto(0, 0)
        self.write("Game over!", align="center", font=FONT)

