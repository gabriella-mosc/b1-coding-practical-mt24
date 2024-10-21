import numpy as np

class PDController:
    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd

        # initiate a value for the previous error
        self.prev_error = 0

    def compute_output(self, position, reference):
        pos_y = position[1]

        error = reference - pos_y 
        error_difference = error - self.prev_error

        # update previous error for next iteration
        self.prev_error = error

        # Proportional term
        P = self.Kp * error
        # Derivative term
        D = self.Kd * error_difference
        # Control output
        output = P + D
        return output
    

