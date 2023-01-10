

class Physics:
    def __init__(self):
        self.gravity = 5                    # Fixe les paramêtres de gravité, accélération, vitesse
        self.acceleration_x = 0             # et position
        self.acceleration_y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.position_x = 0
        self.position_y = 0
        self.dt = 1

    def update_position(self, delta_time):
        self.acceleration_x = 0
        self.acceleration_y = self.gravity
        self.velocity_x = 0.05 * self.acceleration_x * delta_time + self.velocity_x  # Calcul de la vitesse en x
        self.velocity_y = 0.05 * self.acceleration_y * delta_time + self.velocity_y  # Calcul de la vitesse en y
        self.position_x = 0.05 * self.velocity_x * delta_time  # Calcul du déplacement en x
        self.position_y = 0.05 * self.velocity_y * delta_time  # Calcul du déplacement en y
        return self.position_x, self.position_y

    def vertical_mouvments_stop(self):          # Méthode pour stopper le mouvement vertical
        self.gravity = 0
        self.acceleration_y = 0
        self.velocity_y = 0
        self.position_y = 0