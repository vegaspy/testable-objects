class BadCar(object):
    class Engine(object):
        running = False
        fuel_rate = 0
        max_fuel_rate = 23

        def start(self):
            if self.running: raise Exception("Grind")
            self.running = True

        def stop(self):
            self.running = False

        def set_fuel_rate(self, rate):
            self.fuel_rate = rate

    def __init__(self):
        self.engine = self.Engine()

    def accelerate(self, percentage_of_max):
        self.engine.set_fuel_rate(self.engine.max_fuel_rate * percentage_of_max)

    def start(self):
        if not self.engine.running: self.engine.start()

    def stop(self):
        if self.engine.running: self.engine.stop()
