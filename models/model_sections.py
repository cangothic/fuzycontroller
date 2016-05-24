class Section:
    def __init__(self, interval):
        """

         :type interval: list
         """
        self.interval = interval

    # Evaluate a function
    def evaluate(self, value):
        pass

    # Evaluate an integral in the defined interval
    def evaluate_integral(self):
        pass


# class responsible for defining a straight line in an interval
class Line(Section):
    def __init__(self, interval, m, b):
        #super.__init__(self,interval)
        self.interval = interval
        self.m = m
        self.b = b

    def evaluate(self, value):
        return self.m * value + self.b

    def evaluate_integral(self):
        return self.__integral(self.interval[2]) - self.__integral(self.interval[1])

    def __integral(self, value):
        return (self.m / 2) * value ** 2 + self.b * value


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
