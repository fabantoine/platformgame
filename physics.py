

class Physics:
    def __init__(self):
        self.gravity = 5
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.position_x = 0
        self.position_y = 0
        self.dt = 1

    def update_position(self, delta_time):
        self.acceleration_x = 0
        self.acceleration_y = self.gravity
        self.velocity_x = 0.05 * self.acceleration_x * delta_time + self.velocity_x
        self.velocity_y = 0.05 * self.acceleration_y * delta_time + self.velocity_y
        self.position_x = 0.05 * self.velocity_x * delta_time
        self.position_y = 0.05 * self.velocity_y * delta_time
        return self.position_x, self.position_y

    def vertical_mouvments_stop(self):
        self.gravity = 0
        self.acceleration_y = 0
        self.velocity_y = 0
        self.position_y = 0