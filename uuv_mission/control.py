import numpy as np
import matplotlib.pyplot as plt

class PDController:
    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd

    def compute_error(self, reference, depth):
        error = reference - depth
        return error

    def compute_ouput(self, error, error_difference):
        # Proportional term
        P = self.Kp * error
        # Derivative term
        D = self.Kd * error_difference
        # Control output
        output = P + D
        return output

