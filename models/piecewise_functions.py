from models.model_sections import Line


class Piecewise_funtion:
    def __init__(self, section):  #section se envia como [] si es vacio
        if(section != None):
            self.function = [section]
        else:
            self.function = []
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

    def alfa_corte(self,y): #revisar si es alfa corte mayor o menor, es el que lo incluye revisar bien intervalos y los ciclos
        nueva_funcion =  Piecewise_funtion(None) #borrar
        ultimo_punto = self.function[0].interval[0] - 1



        for i in range (0,len(self.function)):
            section = self.function[i]
            puntos =  section.puntos_alfa_corte(y)
            for punto in puntos:
                punto_medio = (punto+ultimo_punto)/2
                if(section.evaluate(punto_medio)<=y):
                    linea = Line([ultimo_punto,punto],section.m,section.b)
                    nueva_funcion.unir(linea)
                else:
                    linea = Line([ultimo_punto,punto],0,y)
                    nueva_funcion.unir(linea)
                ultimo_punto = punto
            if(ultimo_punto!=section.interval[1]):  #se revisa hasta el final del segment
                punto_medio = (section.interval[1] + ultimo_punto) / 2
                if (section.evaluate(punto_medio) <= y):
                    linea = Line([ultimo_punto, section.interval[1]], section.m, section.b)
                    nueva_funcion.unir(linea)
                else:
                    linea = Line([ultimo_punto, section.interval[1]], 0, y)
                    nueva_funcion.unir(linea)
                ultimo_punto = section.interval[1]
        return nueva_funcion