from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot("Mike")
        self.robots.append(robot_one)
        robot_two = Robot("Dave")
        self.robots.append(robot_two)
        robot_three = Robot("Charles")
        self.robots.append(robot_three)

