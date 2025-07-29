class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def print_position(self):
        print(f"Robot is at position ({self.x}, {self.y})")

    def set_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

# --- Example usage ---
if __name__ == "__main__":
    robot = Robot(0, 0)
    robot.print_position()
    robot.set_position(2, 3)
    robot.print_position()
    print("Directly from position():", robot.position())