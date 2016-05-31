from models.model_sections import Line
from models.variable import Tag,Variable,Status_variable,Control_variable
from views.mainview import *
from models.piecewise_functions import Piecewise_funtion


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

print(control_variable_Variacion_Temperatura.FAM)
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
lineaVH = Line([0.1],-1,1)
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
fuzzyficacionHumedad =  status_variable_Humedad.test_tag(65)
parametros = [fuzzyficacionTemperatura,fuzzyficacionHumedad]

def modus_ponens_difuso(parametros,indice = 0,operandos = []): #mejorar con una cola para que sea mas optimo los operandos
    if(indice==len(parametros)):
        for i in range(0,len(operandos)):
            print(operandos[i])
        print("hasta aqui")
        return
    for i in range (0,len(parametros[indice])):
        operandos.append(parametros[indice][i])
        indiceTemp = indice+1
        modus_ponens_difuso(parametros,indiceTemp,operandos)  #mejorar con variables por referencia el indice
        operandos.pop()

modus_ponens_difuso(parametros)
#for i in range (0,5):
#    for j in range (0,5):
#        a = control_variable_Variacion_Temperatura.accederTag([i,j])
#        print(a.tag,end=' ')
#    print()



if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = ControllerView.instance()
    w1 = GraphicContainer(width=5, height=5, dpi=100, function=lambda x: funcionHMuyBaja.buscar(x).evaluate(x))
    window.add_new_window(w1)
    window.show()
    app.exec_()