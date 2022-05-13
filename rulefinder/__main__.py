from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
            QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView,
            QLabel, QListWidget)
from PyQt6.QtCore import Qt
from .helpers import readCSVFile, getRules, PatientsTableData

APPLICATION_NAME = 'Rule Finder'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rules = []
        self.patientsTableData = PatientsTableData()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout(centralWidget)
        self.resize(500, 500)
        self.importFileButton = QPushButton('Import file')
        self.importFileButton.clicked.connect(self.importFileButton_handle)
        self.dataTable = QTableWidget()

        self.generateRulesButton = QPushButton('Generate rules')
        self.generateRulesButton.clicked.connect(self.generateRulesButton_handle)
        self.generateRulesButton.setDisabled(True)

        self.ruleListWidget = QListWidget()

        layout.addWidget(self.importFileButton)

        layout.addWidget(QLabel('Patients data'))
        layout.addWidget(self.dataTable)

        layout.addWidget(self.generateRulesButton)
        layout.addWidget(QLabel('Rules list'))
        layout.addWidget(self.ruleListWidget)

    def importFileButton_handle(self):
        dialog = QFileDialog(self)

        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("CSV file (*.csv)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if dialog.exec():
            filePath = dialog.selectedFiles()[0]
            self.patientsTableData = readCSVFile(filePath)
            self.updatepatientsTableDataTable()
            self.generateRulesButton.setDisabled(False)

    def generateRulesButton_handle(self):
        if self.patientsTableData.data is not None:
            self.rules = getRules(self.patientsTableData)
            self.updateRuleList()
    
    def updateRuleList(self):
        self.ruleListWidget.clear()
        self.ruleListWidget.addItems(self.rules)

    def updatepatientsTableDataTable(self):
        self.dataTable.clearSpans()
        if self.patientsTableData.header is not None and self.patientsTableData.data is not None: 
            self.dataTable.setColumnCount(len(self.patientsTableData.header))

            self.dataTable.setHorizontalHeaderLabels(self.patientsTableData.header)
            for row in self.patientsTableData.data:
                newRowIdx = self.dataTable.rowCount()
                self.dataTable.insertRow(newRowIdx)

                for i in range(self.dataTable.columnCount()):
                    newCell = QTableWidgetItem(row[i])
                    newCell.setFlags(newCell.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.dataTable.setItem(newRowIdx, i, newCell)
                    
            self.dataTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) 


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    app.setApplicationName(APPLICATION_NAME)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())