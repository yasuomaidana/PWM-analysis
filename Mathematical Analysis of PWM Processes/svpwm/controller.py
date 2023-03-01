from time_calculation import time_calculator


class Controller:
    def __init__(self, device_frequency: float, switching_frequency: float, time_step: float):
        self.device_frequency = device_frequency
        self.device_period = 1 / self.device_frequency
        self.switching_frequency = switching_frequency
        self.switching_period = 1 / self.switching_frequency
        self.pre_scaler: int = 0
        self.time_step = time_step
        self.inner_time: float = 0
        self.pre_scaler_limit = int(device_frequency / switching_frequency)

    def time_tick(self):
        self.inner_time += self.time_step
        if self.inner_time / self.device_period >= 1:
            self.inner_time = 0
            self.pre_scaler += 1

    def pre_scaler_tick(self):
        if self.pre_scaler == self.pre_scaler_limit:
            self.pre_scaler = 0
            self.on_switching()

    def on_switching(self):
        pass
