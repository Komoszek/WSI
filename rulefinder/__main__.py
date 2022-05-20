from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
            QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView,
            QLabel, QListWidget, QProgressBar)
from PyQt6.QtCore import (Qt, QThreadPool, QRunnable, QObject, pyqtSignal, pyqtSlot)
from .helpers import readCSVFile, getRules, PatientsTableData

APPLICATION_NAME = 'Rule Finder'

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    Supported signals are:
    - progress: `tuple` indicating progress metadata
    - result: `object` indicating result data
    '''
    progress = pyqtSignal(tuple)
    result = pyqtSignal(object)

class Worker(QRunnable):
    def __init__(self, fn, data):
        super().__init__()
        self.fn = fn
        self.data = data
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        result = self.fn(self.data, self.signals.progress)
        self.signals.result.emit(result)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rules = []
        self.patientsTableData = PatientsTableData()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.thread_manager = QThreadPool()

        layout = QVBoxLayout(centralWidget)
        self.resize(500, 500)
        self.importFileButton = QPushButton('Import file')
        self.importFileButton.clicked.connect(self.importFileButton_handle)
        self.dataTable = QTableWidget()

        self.generateRulesButton = QPushButton('Generate rules')
        self.generateRulesButton.clicked.connect(self.generateRulesButton_handle)
        self.generateRulesButton.setDisabled(True)

        self.ruleListWidget = QListWidget()

        self.progressBarLabel = QLabel()
        self.progressBar = QProgressBar()

        self.progressBar.setMaximum(7)

        layout.addWidget(self.importFileButton)

        layout.addWidget(QLabel('Patients data'))
        layout.addWidget(self.dataTable)

        layout.addWidget(self.generateRulesButton)
        layout.addWidget(QLabel('Rules list'))
        layout.addWidget(self.ruleListWidget)

        layout.addWidget(self.progressBarLabel)
        layout.addWidget(self.progressBar)

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

    def updateProgressBar(self, text, value):
        self.progressBarLabel.setText(text)
        self.progressBar.setValue(value)

    def disableButtons(self, state):
        self.generateRulesButton.setDisabled(state)
        self.importFileButton.setDisabled(state)


    def generateRulesButton_handle(self):
        if self.patientsTableData.data is not None:
            worker = Worker(getRules, self.patientsTableData)

            self.disableButtons(True)
            self.ruleListWidget.clear()
            worker.signals.progress.connect( lambda tup: self.updateProgressBar(tup[0], tup[1]))
            worker.signals.result.connect(self.processResults)

        self.thread_manager.start(worker)

    def processResults(self, result):
        self.rules = result
        self.updateRuleList()
        self.disableButtons(False)
    
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
                    
            self.dataTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) 


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    app.setApplicationName(APPLICATION_NAME)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())