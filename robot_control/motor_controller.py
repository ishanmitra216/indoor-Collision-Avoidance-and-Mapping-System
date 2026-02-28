import numpy as np
from jetbot_interface import JetBotInterface

class MotorController:

    def __init__(self, wheel_base=0.1):
        self.interface = JetBotInterface()
        self.wheel_base = wheel_base

    def set_velocity(self, linear, angular):

        # Differential drive conversion
        v_l = linear - (angular * self.wheel_base / 2)
        v_r = linear + (angular * self.wheel_base / 2)

        # Clamp speeds
        v_l = np.clip(v_l, -1.0, 1.0)
        v_r = np.clip(v_r, -1.0, 1.0)

        self.interface.set_motors(v_l, v_r)

    def stop(self):
        self.interface.stop()

#v_l = v - (ω * L/2)
#v_r = v + (ω * L/2)        