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

    # Return points alfa corte
    def puntos_alfa_corte(self,y):
        pass


# class responsible for defining a straight line in an interval
class Line(Section):
    def __init__(self, interval, m, b):
        self.interval = interval
        self.m = m
        self.b = b

    def puntos_alfa_corte(self,y):
        puntos = []  # todos los puntos del alfacorte
        if(self.m==0):
            if(self.b== y):
                puntos.append(self.interval[0])
                puntos.append(self.interval[1])
            return puntos
        puntos.append((y-self.b)/self.m)
        return puntos

    def evaluate(self, value):
        return self.m * value + self.b

    def evaluate_integral(self):
        return self.__integral(self.interval[2]) - self.__integral(self.interval[1])

    def __integral(self, value):
        return (self.m / 2) * value ** 2 + self.b * value

    def intersectar(self,linea_b): #mejorar por interseccion general!!
        puntos = []
        if(linea_b.m!=self.m):
            x_intersectan = (linea_b.b-self.b)/(self.m-linea_b.m)
            if(x_intersectan>= self.interval[0] and x_intersectan<=self.interval[1] and x_intersectan>= linea_b.interval[0] and x_intersectan<=linea_b.interval[1]):
                puntos.append(x_intersectan)
        return puntos
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
