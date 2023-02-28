class Controller:
    def __init__(self, device_frequency, switching_frequency, time_step):
        self.device_frequency = device_frequency
        self.switching_frequency = switching_frequency
        self.pre_scaler = 0
        self.time_step = time_step
        self.inner_time = 0

    def time_tick(self):
        self.inner_time += self.time_step
        if self.inner_time % self.device_frequency == 0 or self.inner_time > 0:
            self.inner_time = 0
            self.pre_scaler += 1
