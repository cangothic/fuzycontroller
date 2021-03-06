# aqui tenemos un claro problema de variables :P
# variable de estado o de control
class Tag:
    def __init__(self, tag, picewise_function):
        self.tag = tag
        self.picewise_function = picewise_function
        self.indice = 0


class Variable:
    def __init__(self):
        pass


class Status_variable(Variable):
    def __init__(self):
        self.tags = []
        self.cantidad = 0

    def add_tag(self, tag):
        tag.indice = self.cantidad
        self.tags.append(tag)
        self.cantidad += 1

    def test_tag(self, x):
        fuzzyficacion = []  # arreglo de pair <etiqueta, valor de verdad>
        for i in range(0, len(self.tags)):
            result = self.tags[i].picewise_function.buscar(x).evaluate(x)
            if result != 0:
                fuzzyficacion.append([self.tags[i], result])
        return fuzzyficacion


class Control_variable(Variable):
    def __init__(self, status_variables):  # status_variable es un arreglo de status_variable
        self.tags = []
        self.FAM = []
        self.status_variables = status_variables

        def crearFAM(iteracion=0):
            temp = [0] * len(self.status_variables[iteracion].tags)

            if iteracion < len(status_variables) - 1:
                iteracion += 1
                for i in range(0, len(temp)):
                    temp[i] = crearFAM(iteracion)
            return temp

        self.FAM = crearFAM()

    def agregarTagFAM(self, tag, indices, sub_arreglo=[], iteracion=0):
        if (iteracion == 0):  # Se debe mejorar para no ejecutar este codigo cada recursion
            sub_arreglo = self.FAM
        if (iteracion == len(indices) - 1):
            sub_arreglo[indices[-1]] = tag
        else:
            sub_arreglo = sub_arreglo[indices[iteracion]]
            iteracion += 1
            self.agregarTagFAM(tag, indices, sub_arreglo, iteracion)

    def accederTagIndices(self, indices, sub_arreglo=[], iteracion=0):
        if iteracion == 0:  # se debe mejorar para no ejecutar este codigo cada recursion
            sub_arreglo = self.FAM
        if iteracion == len(indices) - 1:
            return sub_arreglo[indices[-1]]
        else:
            sub_arreglo = sub_arreglo[indices[iteracion]]
            iteracion += 1
            return self.accederTagIndices(indices, sub_arreglo, iteracion)
    def accederTagEtiquetas(self, etiquetas):
        indices= []
        for etiqueta in etiquetas:
            indices.append(etiqueta.indice)
        return self.accederTagIndices(indices)

    def add_tag(self, tag):
        self.tags.append(tag)
