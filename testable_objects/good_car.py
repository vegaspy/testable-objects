class Engine(object):
    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def is_running(self):
        raise NotImplementedError

    def set_accelerator_percent(self, percentage_of_max):
        raise NotImplementedError


class ElectricEngine(Engine):
    MAX_AMPERAGE = 80
    CLOSED = True
    OPEN = False

    def __init__(self):
        self.__amperage = 0
        self.__circuit = self.OPEN

    def __open_circuit(self):
        self.__circuit = self.OPEN

    def __close_circuit(self):
        self.__circuit = self.CLOSED

    def stop(self):
        self.__amperage = 0
        self.__open_circuit()

    def start(self):
        self.__close_circuit()

    def is_running(self):
        return self.__circuit is self.OPEN

    def set_accelerator_percent(self, percentage_of_max):
        target_amperage = percentage_of_max * self.MAX_AMPERAGE
        step = (target_amperage - self.__amperage) / 10
        for i in range(1, 10):
            self.__amperage += step


class PetrolEngine(Engine):
    OFF = False
    ON = True
    MAX_LITRES_PER_SECOND = .23
    MIN_LITRES_PER_SECOND = .01
    CRANK_LITRES_PER_SEC = .03

    def __init__(self):
        self.__fuel_rate = 0
        self.__ignition = self.OFF
        self.__running = False

    def stop(self):
        self.__fuel_rate = 0
        self.__ignition = self.OFF
        self.__running = False

    def start(self):
        if not self.__running:
            self.__ignition = self.ON
            self.__fuel_rate = self.CRANK_LITRES_PER_SEC
            self.__engage_starter()
            self.__spin_starter()
            self.__fuel_rate = self.MIN_LITRES_PER_SECOND
            self.__disengage_starter()

    def is_running(self):
        return self.__ignition is self.ON and self.__fuel_rate >= self.MIN_LITRES_PER_SECOND

    def set_accelerator_percent(self, percentage_of_max):
        self.__fuel_rate = percentage_of_max * (self.MAX_LITRES_PER_SECOND - self.IDLE_PER_SECOND)

    def __spin_starter(self):
        pass

    def __engage_starter(self):
        pass

    def __disengage_starter(self):
        pass


class GoodCar(object):
    def __init__(self, engine):
        """

        :param Engine engine:
        :return:
        """
        self.engine = engine

    def accelerate(self, percentage_of_max):
        if self.engine.is_running():
            self.engine.set_accelerator_percent(percentage_of_max)

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()
