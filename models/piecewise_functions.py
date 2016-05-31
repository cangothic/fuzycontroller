from models.model_sections import Line


class Piecewise_funtion:
    def __init__(self, section):
        self.function = [section]
        self.sorted = True

    def unir(self, section):
        self.function.append(section)
        self.sorted = False

    def buscar(self, x):
        if(self.sorted==False):
            self.function.sort(key=lambda section: section.interval[0])
            self.sorted = True

        if (x < self.function[0].interval[0] or x > self.function[-1].interval[1]):
            return Line([x,x],0,0)

        def busquedaBinaria(self, x, left, right):
            centro = int((right + left) / 2)
            if (self.function[left] == self.function[right-1]):
                return self.function[left]
            if (self.function[centro].interval[0] > x):
                return busquedaBinaria(self, x, left, centro)
            return busquedaBinaria(self, x, centro, right)

        return busquedaBinaria(self, x, 0, len(self.function))