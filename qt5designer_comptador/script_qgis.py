from PyQt5.QtWidgets import QDialog 
from PyQt5 import uic

class Comptador(QDialog):
    def __init__(self, recuento = 0):
        QDialog.__init__(self)
        ruta_ui = '/home/josep/wa/plugin-qgis/example/qt5designer_comptador/comptador.ui'
        uic.loadUi(ruta_ui, self)
    
        self.recuento = recuento
        self.valor_contador.setText(str(recuento))
        
        self.suma.clicked.connect(self.aumentar_recuento)
        self.resta.clicked.connect(self.resta_recuento)
        
    def aumentar_recuento(self):
        self.recuento += 1
        self.actualizar_contador()
    
    def resta_recuento(self):
        self.recuento -= 1
        self.actualizar_contador()
    
    def actualizar_contador(self):
        self.valor_contador.setText(str(self.recuento))
        
comptador = Comptador(0)
comptador.show()