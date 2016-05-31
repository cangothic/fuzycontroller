import random
from PyQt4 import QtCore, QtGui
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated
        self._instance = None

    def instance(self):
        if self._instance is not None:
            return self._instance
        else:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class ControllerView(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle("Fuzzy Controller")
        self.setObjectName("ControllerView")
        with open("views/css/styles.css") as f:
            self.setStyleSheet(f.read())
        self.resize(800, 600)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.__windows = {}

    def add_new_window(self, widget):
        self.__windows[widget.name] = widget
        self.central_widget.addWidget(self.__windows[widget.name])

    def change_window(self, name):
        self.central_widget.setCurrentWidget(self.__windows[name])


class GraphicInterface(FigureCanvas):
    """esto es una interfaz para crear una grafica figureCanvas hereda de Qwidget"""

    def __init__(self, parent=None, width=5, height=4, dpi=100, inicial=0.0, final=100.0, intervalo=0.01,
                 functions=lambda x: x * x, singletons=[],name="grafica"):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor='None', edgecolor='None')
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        fig.patch.set_alpha(0)
        self.inicial = inicial
        self.final = final
        self.intervalo = intervalo
        self.functions = functions
        self.singletons = singletons
        self.name = name
        self.compute_initial_figure()

    def compute_initial_figure(self):
        pass


class StaticGraphic(GraphicInterface):
    """esto es una clase implementada de la interfaz GraphicInterface"""

    def __init__(self, *args, **kwargs):
        super(StaticGraphic, self).__init__(*args, **kwargs)

    def compute_initial_figure(self):
        x = arange(self.inicial, self.final, self.intervalo)
        self.axes.hold()
        self.axes.set_ylim([0.0,1.0])
        i=0
        for function in self.functions:
            i=i+1
            y=list(map(function, x))
            self.axes.plot(x, y, label=str(i))
            self.axes.legend(loc=2)
            if len(self.singletons) != 0:
                for singleton in self.singletons:
                    self.axes.axvline(singleton, color='k')


class DynamicGraphic(GraphicInterface):
    """esto es una clase implementada de la interfaz GraphicInterface"""

    def __init__(self, *args, **kwargs):
        GraphicInterface.__init__(self, *args, **kwargs)
        self.name = "grafica dinamica"
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()


class GraphicContainer(QtGui.QWidget):
    "clase creaga para contener objetos de  la  clase Graphic interface y visualizarlos con Pyqt4"

    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self)
        self.grafica = StaticGraphic(self, *args, **kwargs)
        self.aplication = ControllerView.instance()
        self.name = self.grafica.name
        self.setFocus()
        self.botton = QtGui.QPushButton("devolverse a menu",self)
        self.botton.move(500,40)
        self.botton.clicked.connect(lambda: self.aplication.change_window("menu"))


class Menu(QtGui.QWidget):
    def __init__(self,parent=None):
        self.aplication = ControllerView.instance()
        self.viajes = self.aplication._ControllerView__windows
        QtGui.QWidget.__init__(self,parent)
        self.name = "menu"
        self.combobox = QtGui.QComboBox(self)
        self.combobox.setGeometry(0,0,400,30)
        for viaje in self.viajes:
            self.combobox.addItem(viaje)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizarclaves)
        self.timer.start(1000)
        self.botton = QtGui.QPushButton("ir a grafica", self)
        self.botton.move(0,40)
        self.botton.clicked.connect(lambda: self.aplication.change_window(self.combobox.currentText()))

    def actualizarclaves(self):
        self.viajes = self.aplication._ControllerView__windows
        for viaje in self.viajes:
            if viaje != "menu":
                self.combobox.addItem(viaje)
        self.timer.stop()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = ControllerView.instance()
    w1 = GraphicContainer(width=5, height=5, dpi=100, functions=lambda x: sin(x))
    window.add_new_window(w1)
    window.show()
    app.exec_()
