class Piecewise_funtion:
    def __init__(self, section):
        self.function = self.functionstart(section)
    @staticmethod
    def unidor(section, function):
        def union(x):
            if section.interval[0] <= x <= section.interval[1]:
                return section.function(x)
            else:
                return function(x)
        return union


    def unir(self, section):
        self.function = self.unidor(section, self.function)

    @staticmethod
    def functionstart(section):
        def inicio(x):
            if section.interval[0] <= x <= section.interval[1]:
                return section.function(x)
            else:
                return 0
        return inicio
