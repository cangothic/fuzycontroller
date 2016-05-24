from models.model_sections import Line
class Piecewise_funtion:
    def __init__(self, section):
        self.function = [section]

    def unir(self, section):
        self.function.append(section)

    def buscar(self, x):
        if (x < self.function[0].interval[0] or x > self.function[-1].interval[1]):
            return Line([x,x],0,0)

        def busquedaBinaria(self, x, left, right):
            print ("left es "+str(left))
            print ("right es "+str(right))
            centro = int((right + left) / 2)
            print ("centro es "+str(centro))
            if (self.function[left] == self.function[right-1]):
                return self.function[left]
            if (self.function[centro].interval[0] > x):
                return busquedaBinaria(self, x, left, centro)
            return busquedaBinaria(self, x, centro, right)

        return busquedaBinaria(self, x, 0, len(self.function))