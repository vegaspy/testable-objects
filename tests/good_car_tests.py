import unittest, six

if six.PY2:
    from mock import MagicMock
else:
    from unittest.mock import MagicMock

from testable_objects.good_car import ElectricEngine, GoodCar


class GoodCarBadTest(unittest.TestCase):
    def tearDown(self):
        self.car = None

    def setUp(self):
        self.car = GoodCar(ElectricEngine())

    def test_start(self):
        self.car.start()

    def test_stop(self):
        self.car.stop()

    def test_accelerate(self):
        self.car.accelerate(.1)


class GoodCarGoodTest(unittest.TestCase):
    def tearDown(self):
        self.engine = None
        self.car = None

    def setUp(self):
        self.engine = MagicMock()
        self.engine.is_running.return_value = True
        self.car = GoodCar(self.engine)

    def test_start_starts_engine(self):
        self.car.start()
        self.engine.start.assert_called_once_with()

    def test_stop_stops_engine(self):
        self.car.stop()
        self.engine.stop.assert_called_once_with()

    def test_accelerate_sets_accelerator_percent_when_running(self):
        expected = .9
        self.car.accelerate(expected)
        self.engine.set_accelerator_percent.assert_called_once_with(expected)

    def test_accelerate_sets_accelerator_does_nothing_when_not_running(self):
        self.engine.is_running.return_value = False
        self.car.accelerate(1)
        self.engine.set_accelerator_percent.assert_not_called()

    def test_accelerate_does_not_stop_engine(self):
        self.car.accelerate(.1)
        self.engine.stop.assert_not_called()