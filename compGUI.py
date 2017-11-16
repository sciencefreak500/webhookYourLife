from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CompGUIWindow(object):
    def setupUi(self, CompGUIWindow):
        CompGUIWindow.setObjectName(_fromUtf8("CompGUIWindow"))
        CompGUIWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(CompGUIWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout.addWidget(self.saveButton, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 481))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(0, 60))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.triggerLine = QtGui.QLineEdit(self.widget)
        self.triggerLine.setObjectName(_fromUtf8("triggerLine"))
        self.horizontalLayout.addWidget(self.triggerLine)
        self.filepathLine = QtGui.QLineEdit(self.widget)
        self.filepathLine.setObjectName(_fromUtf8("filepathLine"))
        self.horizontalLayout.addWidget(self.filepathLine)
        self.filePathButton = QtGui.QToolButton(self.widget)
        self.filePathButton.setObjectName(_fromUtf8("filePathButton"))
        self.horizontalLayout.addWidget(self.filePathButton)
        self.RemoveEntryButton = QtGui.QPushButton(self.widget)
        self.RemoveEntryButton.setObjectName(_fromUtf8("RemoveEntryButton"))
        self.horizontalLayout.addWidget(self.RemoveEntryButton)
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)
        self.addEntryButton = QtGui.QPushButton(self.centralwidget)
        self.addEntryButton.setObjectName(_fromUtf8("addEntryButton"))
        self.gridLayout.addWidget(self.addEntryButton, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.gridLayout.addWidget(self.exitButton, 2, 1, 1, 1)
        CompGUIWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CompGUIWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        CompGUIWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CompGUIWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CompGUIWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(CompGUIWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(CompGUIWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(CompGUIWindow)
        QtCore.QMetaObject.connectSlotsByName(CompGUIWindow)

    def retranslateUi(self, CompGUIWindow):
        CompGUIWindow.setWindowTitle(_translate("CompGUIWindow", "Computer Trigger Configuration", None))
        self.saveButton.setText(_translate("CompGUIWindow", "Save", None))
        self.triggerLine.setPlaceholderText(_translate("CompGUIWindow", "Trigger Word", None))
        self.filepathLine.setPlaceholderText(_translate("CompGUIWindow", "File path of Program to execute", None))
        self.filePathButton.setText(_translate("CompGUIWindow", "...", None))
        self.RemoveEntryButton.setText(_translate("CompGUIWindow", "Remove", None))
        self.addEntryButton.setText(_translate("CompGUIWindow", "Add Entry", None))
        self.exitButton.setText(_translate("CompGUIWindow", "Exit", None))
        self.menuFile.setTitle(_translate("CompGUIWindow", "File", None))
        self.actionSave.setText(_translate("CompGUIWindow", "Save", None))
        self.actionExit.setText(_translate("CompGUIWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CompGUIWindow = QtGui.QMainWindow()
    ui = Ui_CompGUIWindow()
    ui.setupUi(CompGUIWindow)
    CompGUIWindow.show()
    sys.exit(app.exec_())

