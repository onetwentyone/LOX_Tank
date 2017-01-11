class Gas(object):
    def __init__(self,density,pressure,temperature):
        self.density = density
        self.pressure = pressure
        self.temp = temperature
    def vol(self):
        v = self.density * self.temp *276 / self.pressure
        print(v)

lox = Gas(1.4,22,90.4)
print(lox.vol())