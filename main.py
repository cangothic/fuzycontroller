from models.model_sections import Line
from models.piecewise_functions import Piecewise_funtion
from models.variable import Tag


lineaC = Line([1,4],1/3,-1/3)
lineaA = Line([4,6],0,1)
lineaB = Line([6,8],-1/2,3)
funcionA = Piecewise_funtion(lineaA)
funcionA.unir(lineaB)
funcionA.unir(lineaC)

for i in range (0,12):
    print (i)
    func = funcionA.buscar(i)
    print (str(func.m)+str(func.b))