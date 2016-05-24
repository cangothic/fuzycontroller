class Cartesian_plane:
    def __ini__(self):
        self.functions = []
    def unir(self,function):
        self.functions.append(function)
    def consultar(self,x):
        functions = []
        for i in range(0,len(self.functions)):
            if(self.functions[i].evaluate!=0):
                functions.append(self.functions[i])
        