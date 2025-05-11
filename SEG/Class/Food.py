class Food:
    def __init__(self, x, y, energy, type="plaint"):
        self.x = x
        self.y = y
        if type == "plaint":
            self.size = 3
            self.energy = energy * 1
            self.color = (0, 255, 0)
        elif type == "meat":
            self.size = 3
            self.energy = energy * 1.75
            self.color = (227, 66, 66)
        elif type == "death":
            self.size = 4
            self.energy = energy
            self.color = (227, 66, 66)

        self.type = type