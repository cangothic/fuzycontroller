from models.model_sections import Line
from models.piecewise_functions import Piecewise_funtion
lineaA = Line([1,4],1/3,-1/3)
lineaB = Line([4,6],0,1)
lineaC = Line([6,8],-1/2,3)

funcionA = Piecewise_funtion(lineaA)
funcionA.unir(lineaB)
funcionA.unir(lineaC)

for i in range (0,12):
    print (i)
    func = funcionA.buscar(i)
    print (str(func.m)+str(func.b))