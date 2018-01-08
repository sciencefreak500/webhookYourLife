from PyQt4 import QtCore, QtGui
from functools import partial
import json
import atexit
import os

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
        
                
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
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

        self.triggerArray = [];

        self.readJson()
        
        #button press events
        self.saveButton.clicked.connect(self.saveJson)
        self.addEntryButton.clicked.connect(partial(self.newTrigger,trigger=None,path=None))
        self.exitButton.clicked.connect(self.exitAll)

        self.actionSave.triggered.connect(self.saveJson)
        self.actionExit.triggered.connect(self.exitAll)

    def exitAll(self):
        self.saveJson()
        app.quit()
        sys.exit()
    
    def saveJson(self):
        print("saving json")
        print(self.triggerArray)
        data = {}
        for i in self.triggerArray:
            if i is not None:
                triggerText = i.findChild(QtGui.QLineEdit,"triggerLine").text()
                pathText = i.findChild(QtGui.QLineEdit,"filepathLine").text()
                if triggerText != "" or pathText != "":
                    data[triggerText] = pathText
        print("full", data)
        with open('data.json','w') as file:
            json.dump(data,file)
    
    def readJson(self):
        if not os.path.isfile('data.json'):
            file = open('data.json','w')
            file.write("{}")
            file.close()
        print("reading json")
        data = json.load(open('data.json'))
        for key in data:
            print(key, data[key])
            print("populate UI")
            self.newTrigger(key,data[key])
                

    def removeTrigger(self,num):
        remObj = self.triggerArray[num]
        self.verticalLayout.removeWidget(self.triggerArray[num])
        self.triggerArray[num].deleteLater()
        self.triggerArray[num] = None
        #print("removing button number ",num)
        #self.triggerArray.remove(remObj)

    def addFilePath(self,num):
        print("adding to filepath num ", num)
        filename = QtGui.QFileDialog.getOpenFileName(self.triggerArray[num],'Find Path')
        print("the path is", filename)
        fileline = self.triggerArray[num].findChild(QtGui.QLineEdit, "filepathLine")
        fileline.setText(_translate("CompGUIWindow",filename,None))

        #edit the json file too

        
    def newTrigger(self, trigger, path):
        triggerNum = len(self.triggerArray)
        print("creating new row # ",triggerNum)
    
        #widget properties and config
        widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        widget.setMinimumSize(QtCore.QSize(0, 60))
        widget.setObjectName(_fromUtf8("widget"))
        horizontalLayout = QtGui.QHBoxLayout(widget)
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #triggerLabel = QtGui.QLabel(str(triggerNum), widget)
        #triggerLabel.setObjectName(_fromUtf8("triggerLabel"))
        #horizontalLayout.addWidget(triggerLabel)
        triggerLine = QtGui.QLineEdit(widget)
        triggerLine.setObjectName(_fromUtf8("triggerLine"))
        horizontalLayout.addWidget(triggerLine)
        filepathLine = QtGui.QLineEdit(widget)
        filepathLine.setObjectName(_fromUtf8("filepathLine"))
        horizontalLayout.addWidget(filepathLine)
        filePathButton = QtGui.QToolButton(widget)
        filePathButton.setObjectName(_fromUtf8("filePathButton"))
        horizontalLayout.addWidget(filePathButton)
        RemoveEntryButton = QtGui.QPushButton(widget)
        RemoveEntryButton.setObjectName(_fromUtf8("RemoveEntryButton"))
        horizontalLayout.addWidget(RemoveEntryButton)

        #visual text edits
        triggerLine.setPlaceholderText(_translate("CompGUIWindow", "Trigger Word", None))
        filepathLine.setPlaceholderText(_translate("CompGUIWindow", "File path of Program to execute", None))
        filePathButton.setText(_translate("CompGUIWindow", "...", None))
        RemoveEntryButton.setText(_translate("CompGUIWindow", "Remove", None))

        if trigger:
            triggerLine.setText(_translate("CompGUIWindow",trigger,None))

        if path:
            filepathLine.setText(_translate("CompGUIWindow",path,None))
            
        #add the widget obj to the array
        self.triggerArray.append(widget)
        self.verticalLayout.addWidget(self.triggerArray[triggerNum])

        #button triggers
        RemoveEntryButton.clicked.connect(partial(self.removeTrigger,num=triggerNum))
        filePathButton.clicked.connect(partial(self.addFilePath,num=triggerNum))

        
    def retranslateUi(self, CompGUIWindow):
        CompGUIWindow.setWindowTitle(_translate("CompGUIWindow", "Computer Trigger Configuration", None))
        self.saveButton.setText(_translate("CompGUIWindow", "Save", None))
        
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
    progRun = app.exec_()
    ui.saveJson()
    sys.exit(progRun)

