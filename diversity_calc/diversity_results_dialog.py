from qgis.PyQt.QtWidgets import *
from .diversity_results_dialog_ui import Ui_Dialog


class DlgResults(QDialog, Ui_Dialog):
    def __init__(self):
        super(DlgResults, self).__init__()
        self.setupUi(self)

        self.setLayout(self.lytMain)
        self.trwResult.setColumnWidth(0, 150)
        self.trwResult.setColumnWidth(1, 80)
        self.trwResult.setColumnWidth(2, 80)
        self.trwResult.setColumnWidth(3, 80)
        self.trwResult.setColumnWidth(4, 80)
        self.trwResult.setColumnWidth(5, 80)

