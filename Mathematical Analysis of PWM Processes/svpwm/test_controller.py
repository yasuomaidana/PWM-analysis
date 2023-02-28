import unittest
import numpy as np
from controller import Controller

pi = np.pi


class TestController(unittest.TestCase):

    def setUp(self) -> None:
        simulation_time = 3
        time_step = 1e-4
        ticks = int(simulation_time / time_step)

        simulation_time = time_step * ticks
        self.t = np.linspace(0, simulation_time, ticks)
        self.time_step: float = time_step
        self.simulation_time: float = simulation_time

    def test_time_sampling(self):
        controller = Controller(1000, 100, self.time_step)
        controller_period = controller.device_period
        controller_samplings = int(self.simulation_time / controller_period)
        old_prescaling = controller.pre_scaler
        device_samplings = 0
        for _ in self.t:
            controller.time_tick()
            if old_prescaling != controller.pre_scaler:
                device_samplings += 1
                old_prescaling = controller.pre_scaler
        self.assertEqual(controller_samplings, device_samplings, "The device is not working properly")

    def test_switching_sampling(self):
        controller = Controller(1000, 100, self.time_step)
        switching_period = controller.switching_period
        expected_switching_sampling = int(self.simulation_time/switching_period)
        switching_sampling = 0
        for _ in self.t:
            controller.time_tick()
            if controller.pre_scaler == controller.pre_scaler_limit:
                switching_sampling += 1
            controller.pre_scaler_tick()
        self.assertEqual(expected_switching_sampling, switching_sampling, "The device is not working properly")


if __name__ == '__main__':
    unittest.main()
