import sys
import sass

# import do PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt

# import das janelas

from ui.main import Ui_MainWindow as Main
from ui.ata import Ui_MainWindow as Ata
from ui.ata_gerar import Ui_MainWindow as AtaGerar
from ui.convocacao import Ui_MainWindow as Convoc
from ui.convocacao_gerar import Ui_MainWindow as ConvocGerar
from ui.departamentos import Ui_MainWindow as Departamentos

class gui:

    def __init__(self):
# declarações da interface gráfica
        print("Gerando a interface gráfica")

        self.app = QApplication(sys.argv)

# janela principal
        self.wMain = QMainWindow()
        self.ui = Main()
        self.ui.setupUi(self.wMain)

# janela ata
        self.wAta = QMainWindow()
        self.uiAta = Ata()
        self.uiAta.setupUi(self.wAta)

# janela gerar ata
        self.wAtaGerar = QMainWindow()
        self.uiAtaGerar = AtaGerar()
        self.uiAtaGerar.setupUi(self.wAtaGerar)

# janela convocação
        self.wConvoc = QMainWindow()
        self.uiConvoc = Convoc()
        self.uiConvoc.setupUi(self.wConvoc)

# janela gerar convocação
        self.wConvocGerar = QMainWindow()
        self.uiConvocGerar = ConvocGerar()
        self.uiConvocGerar.setupUi(self.wConvocGerar)

# janela departamentos
        self.wDepartamentos = QMainWindow()
        self.uiDepartamentos = Departamentos()
        self.uiDepartamentos.setupUi(self.wDepartamentos)
        
# seta a mesma folha de estilos e bloqueio para todas as janelas

        for janela in [
            self.wMain,
            self.wAta,
            self.wAtaGerar,
            self.wConvoc,
            self.wConvocGerar,
            self.wDepartamentos
        ]:
            janela.setWindowModality(Qt.ApplicationModal)       

# inicializa a janela
        self.wMain.show()
