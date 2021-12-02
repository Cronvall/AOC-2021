

class Vector2bad:
    x = 0
    y = 0
    aim = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.aim = 0

    def up(self, units):
        #self.y -= units
        self.aim -= units

    def down(self, units):
        #self.y += units
        self.aim += units

    def forward(self, units):
        self.x += units
        self.y += (units * self.aim)


def solution():
    position =  Vector2bad(0,0)
    commands = open("input.txt", "r")
    for command in commands:
        command = command.split(" ")
        dir = command[0]
        units = int(command[1])

        if dir == "forward":
            position.forward(units)
        elif dir == "down":
            position.down(units)
        if dir == "up":
            position.up(units)

    print(position.x * position.y)


if __name__ == "__main__":
    solution2()


