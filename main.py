from models.model_sections import Line
from models.variable import Tag,Variable,Status_variable,Control_variable
from views.mainview import *
from models.piecewise_functions import Piecewise_funtion
import copy

lineaTA = Line([0,10],0,1)
lineaTB = Line([10,15],-0.2,3)
funcionTMuyBaja = Piecewise_funtion(lineaTA)
funcionTMuyBaja.unir(lineaTB)

lineaTC = Line([10,15],0.2,-2)
lineaTD = Line([15,20],-0.2,4)
funcionTBaja = Piecewise_funtion(lineaTC)
funcionTBaja.unir(lineaTD)

lineaTE = Line([18,20],0.5,-9)
lineaTF = Line([20,22],-0.5,11)
funcionTNormal = Piecewise_funtion(lineaTE)
funcionTNormal.unir(lineaTF)

lineaTG = Line([20,25],0.2,-4)
lineaTH = Line([25,30],-0.2,6)
funcionTAlta = Piecewise_funtion(lineaTG)
funcionTAlta.unir(lineaTH)

lineaTI = Line([25,30],0.2,-5)
lineaTJ = Line([30,40],0,1)
funcionTMuyAlta = Piecewise_funtion(lineaTI)
funcionTMuyAlta.unir(lineaTJ)

status_variable_Temperatura = Status_variable()
tagTA = Tag("MB",funcionTMuyBaja)
tagTB = Tag("B",funcionTBaja)
tagTC = Tag("N",funcionTNormal)
tagTD = Tag("A",funcionTAlta)
tagTE = Tag("MA",funcionTMuyAlta)
status_variable_Temperatura.add_tag(tagTA)
status_variable_Temperatura.add_tag(tagTB)
status_variable_Temperatura.add_tag(tagTC)
status_variable_Temperatura.add_tag(tagTD)
status_variable_Temperatura.add_tag(tagTE)

lineaHA = Line([0,10],0,1)
lineaHB = Line([10,20],-0.1,2)
funcionHMuyBaja = Piecewise_funtion(lineaHA)
funcionHMuyBaja.unir(lineaHB)

lineaHC = Line([10,25],1/15,-2/3)
lineaHD = Line([25,40],-1/15,8/3)
funcionHBaja = Piecewise_funtion(lineaHC)
funcionHBaja.unir(lineaHD)

lineaHE = Line([30,40],0.1,-3)
lineaHF = Line([40,50],-0.1,5)
funcionHNormal = Piecewise_funtion(lineaHE)
funcionHNormal.unir(lineaHF)

lineaHG = Line([40,45],1/15,-8/3)
lineaHH = Line([55,70],-1/15,14/3)
funcionHAlta = Piecewise_funtion(lineaHG)
funcionHAlta.unir(lineaHH)

lineaHI = Line([60,70],0.1,-6)
lineaHJ = Line([70,100],0,1)
funcionHMuyAlta = Piecewise_funtion(lineaHI)
funcionHMuyAlta.unir(lineaHJ)

status_variable_Humedad = Status_variable()
tagHA = Tag("MB",funcionHMuyBaja)
tagHB = Tag("B",funcionHBaja)
tagHC = Tag("N",funcionHNormal)
tagHD = Tag("A",funcionHAlta)
tagHE = Tag("MA",funcionHMuyAlta)
status_variable_Humedad.add_tag(tagHA)
status_variable_Humedad.add_tag(tagHB)
status_variable_Humedad.add_tag(tagHC)
status_variable_Humedad.add_tag(tagHD)
status_variable_Humedad.add_tag(tagHE)

variables = []
variables.append(status_variable_Temperatura)
variables.append(status_variable_Humedad)

control_variable_Variacion_Temperatura = Control_variable(variables)

#print(control_variable_Variacion_Temperatura.FAM)
lineaVA = Line([-15,-10],0.2,3)
lineaVB = Line([-10,-7.5],-0.4,-3)
funcionBajadaGrande =Piecewise_funtion(lineaVA)
funcionBajadaGrande.unir(lineaVB)

lineaVC = Line([-10 -5],0.2,2)
lineaVD = Line([-5,-2.5],-0.4,-1)
funcionBajadaNormal = Piecewise_funtion(lineaVC)
funcionBajadaNormal.unir(lineaVD)

lineaVE = Line([-7.5,-2.5],0.2,1.5)
lineaVF = Line([-2.5,0],-0.4,0)
funcionBajadaPequeña = Piecewise_funtion(lineaVE)
funcionBajadaPequeña.unir(lineaVF)

lineaVG = Line([-1,0],1,1)
lineaVH = Line([0,1],-1,1)
funcionMantener = Piecewise_funtion(lineaVG)
funcionMantener.unir(lineaVH)

lineaVI = Line([0,2.5],0.4,0)
lineaVJ = Line([2.5,7.5],-0.2,1.5)
funcionSubidaPequena = Piecewise_funtion(lineaVI)
funcionSubidaPequena.unir(lineaVJ)

lineaVK= Line([2.5,5],0.4,-1)
lineaVL= Line([5,10],-0.2,2)
funcionSubidaNormal = Piecewise_funtion(lineaVK)
funcionSubidaNormal.unir(lineaVL)

lineaVM= Line([7.5,10],0.4,-3)
lineaVN= Line([10,15],-0.2,3)
funcionSubidaGrande = Piecewise_funtion(lineaVM)
funcionSubidaGrande.unir(lineaVN)

tagVBG = Tag("BG",funcionBajadaGrande)
tagVBN = Tag("BN",funcionBajadaNormal)
tagVBP = Tag("BP",funcionBajadaPequeña)
tagVM = Tag("M",funcionMantener)
tagVSP = Tag("SP",funcionSubidaPequena)
tagVSN = Tag("SN",funcionSubidaNormal)
tagVSG = Tag("SG",funcionSubidaGrande)

control_variable_Variacion_Temperatura.add_tag(tagVBG)
control_variable_Variacion_Temperatura.add_tag(tagVBN)
control_variable_Variacion_Temperatura.add_tag(tagVBP)
control_variable_Variacion_Temperatura.add_tag(tagVM)
control_variable_Variacion_Temperatura.add_tag(tagVSP)
control_variable_Variacion_Temperatura.add_tag(tagVSN)
control_variable_Variacion_Temperatura.add_tag(tagVSG)

control_variable_Variacion_Temperatura.agregarTagFAM(tagVSN, [0, 0])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVSN, [0, 1])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVSG, [0, 2])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVSG, [0, 3])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVSG, [0, 4])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM, [1, 0])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM, [1, 1])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVSP, [1, 2])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVSP, [1, 3])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVSN, [1, 4])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM,[2,0])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM,[2,1])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM,[2,2])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM,[2,3])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBP,[2,4])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM,[3,0])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVM,[3,1])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBP,[3,2])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBP,[3,3])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBN,[3,4])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBP,[4,0])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBN,[4,1])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBN,[4,2])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBG,[4,3])
control_variable_Variacion_Temperatura.agregarTagFAM(tagVBG,[4,4])

#ejemplo
fuzzyficacionTemperatura = status_variable_Temperatura.test_tag(19.5)
fuzzyficacionHumedad = status_variable_Humedad.test_tag(65)
parametros = [fuzzyficacionTemperatura,fuzzyficacionHumedad]

#retorna arreglo de pice_wise_function
def modus_ponens_difuso(parametros,window,indice = 0,retornos = [],operandos = []): #mejorar con una cola para que sea mas optimo los operandos
    if(indice==len(parametros) and len(parametros)>0):
        minimo = operandos[0]
        etiquetas = []
        for i in range(0,len(operandos)):
            etiquetas.append(operandos[i][0])
            if(operandos[i][1]<minimo[1]):
                minimo = operandos[i]
        tag = control_variable_Variacion_Temperatura.accederTagEtiquetas(etiquetas)
        funcion = tag.picewise_function.alfa_corte(minimo[1])
        retornos.append(funcion)
        funcion_lambda = lambda x: funcion.buscar(x).evaluate(x)
        name = tag.tag + str(minimo[1])
        w1 = GraphicContainer(width=5, height=5, dpi=100, functions=[funcion_lambda], singletons=[],name= name,inicial=funcion.function[0].interval[0]-5,final = funcion.function[-1].interval[1] + 5)

        window.add_new_window(w1)

        return
    for i in range (0,len(parametros)):
        operandos.append(parametros[indice][i])
        indiceTemp = indice+1
        modus_ponens_difuso(parametros,window,indiceTemp,retornos,operandos)  #mejorar con variables por referencia el indice
        operandos.pop()
    return retornos

def intersecciones_piece_wise_functions(piece_wise_function_a,piece_wise_function_b):
    puntos = []
    for segmento_a in piece_wise_function_a.function:
        for segmento_b in piece_wise_function_b.function:
            puntos.extend(segmento_a.intersectar(segmento_b))
    return puntos
def agregacion(piece_wise_functions,window):
    puntos = []
    for i in range (0,len(piece_wise_functions)):
        for j in range(i+1,len(piece_wise_functions)):
            piece_wise_function_a = piece_wise_functions[i]
            piece_wise_function_b = piece_wise_functions[j]
            puntos.extend(intersecciones_piece_wise_functions(piece_wise_function_a,piece_wise_function_b))


    nueva_funcion = Piecewise_funtion(None)  # borrar
    punto_pasado = piece_wise_functions[0].function[0].interval[0]
    ultimo_punto = piece_wise_functions[0].function[0].interval[1]
    for piece_wise_function in piece_wise_functions:
        if(piece_wise_function.function[0].interval[0]<punto_pasado):
            punto_pasado = piece_wise_function.function[0].interval[0]
        if(piece_wise_function.function[-1].interval[1]>ultimo_punto):
            ultimo_punto = piece_wise_function.function[-1].interval[1]
    puntos.sort()
    if(puntos[-1]<ultimo_punto):
        puntos.append(ultimo_punto)
    for punto in puntos:
        if(punto_pasado>punto):
            temp = punto
            punto = punto_pasado
            punto_pasado = temp
        punto_medio = (punto_pasado+punto)/2
        mayor = piece_wise_functions[0]
        for piece_wise_function in piece_wise_functions:
            a = piece_wise_function.buscar(punto_medio).evaluate(punto_medio)
            b = mayor.buscar(punto_medio).evaluate(punto_medio)
            if(a>=b):
                mayor = piece_wise_function
        for segmento in mayor.function:
            if(punto_pasado<=segmento.interval[0]<=punto or punto_pasado<=segmento.interval[1]<=punto):
                nuevo_segmento = copy.deepcopy(segmento)
                nuevo_segmento.interval[0] = max(nuevo_segmento.interval[0],punto_pasado)
                nuevo_segmento.interval[1] = min(nuevo_segmento.interval[1],punto)
                nueva_funcion.unir(nuevo_segmento)
        punto_pasado = punto
    funcion_lambda = lambda x: nueva_funcion.buscar(x).evaluate(x)
    w1 = GraphicContainer(width=5, height=5, dpi=100, functions=[funcion_lambda], singletons=[], name="agregacion",inicial=-8, final=12)

    window.add_new_window(w1)
if __name__ == '__main__':


    app = QtGui.QApplication([])
    window = ControllerView.instance()
    menu=Menu()
    window.add_new_window(menu)
    piece_wise_functions = modus_ponens_difuso(parametros, window)
    agregacion(piece_wise_functions,window)

    def convertirLambda(funcion):
        return lambda x: funcion.buscar(x).evaluate(x)
    arreglodefuncionestemperatura = [convertirLambda(funcionTMuyBaja),convertirLambda(funcionTBaja), convertirLambda(funcionTNormal),convertirLambda(funcionTAlta), convertirLambda(funcionTMuyAlta)]
    arreglodefuncioneshumedad = [convertirLambda(funcionHMuyBaja),convertirLambda(funcionHBaja), convertirLambda(funcionHNormal),convertirLambda(funcionHAlta), convertirLambda(funcionHMuyAlta)]
    arreglodefuncionesvtemperatura = [convertirLambda(funcionBajadaGrande),convertirLambda(funcionBajadaNormal), convertirLambda(funcionBajadaPequeña),convertirLambda(funcionMantener), convertirLambda(funcionSubidaPequena),convertirLambda(funcionSubidaNormal),convertirLambda(funcionSubidaGrande)]


    w1 = GraphicContainer(width=5, height=5, dpi=100, functions=arreglodefuncionestemperatura, singletons=[],name = "Temperatura",final = 40)
    window.add_new_window(w1)
    w2 = GraphicContainer(width=5, height=5, dpi=100, functions=arreglodefuncioneshumedad, singletons=[],name = "Humedad")
    window.add_new_window(w2)

    w3 = GraphicContainer(width=5, height=5, dpi=100, functions=arreglodefuncionesvtemperatura, singletons=[],name = "Variacion de Temperatura",inicial = -15,final = 15)
    window.add_new_window(w3)

    window.show()
    app.exec_()
    app = QtGui.QApplication([])


