#Hadjerci Mohammed Allaeddine

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newprojetia.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from preprocessing import one_hot, load_obj
from keras.models import load_model
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.isWithLabel = False
        self.data = []
        self.all_labels = []
        self.model = load_model('model/100_leaves-layersize128-layercount2.h5')

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenTest = QtWidgets.QPushButton(self.centralwidget)
        self.OpenTest.setGeometry(QtCore.QRect(30, 500, 121, 31))
        self.OpenTest.setObjectName("OpenTest")
        self.OpenTest.clicked.connect(self.file_open)

        self.DataViewer = QtWidgets.QTableWidget(self.centralwidget)
        self.DataViewer.setGeometry(QtCore.QRect(170, 20, 281, 451))
        self.DataViewer.setObjectName("DataViewer")
        self.init_table()

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(480, 10, 291, 261))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 241, 191))
        self.label.setText("")
        self.label.setObjectName("label")

        self.SaveFile = QtWidgets.QPushButton(self.centralwidget)
        self.SaveFile.setGeometry(QtCore.QRect(170, 500, 131, 31))
        self.SaveFile.setObjectName("SaveFile")
        self.SaveFile.clicked.connect(self.file_save)

        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(660, 500, 111, 31))
        self.ExitButton.setObjectName("ExitButton")
        self.ExitButton.clicked.connect(self.close_application)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 290, 121, 16))
        self.label_2.setObjectName("label_2")
        self.ClassResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.ClassResult.setGeometry(QtCore.QRect(480, 320, 291, 31))
        self.ClassResult.setObjectName("ClassResult")

        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 20, 131, 451))
        self.listView.setObjectName("listView")
        self.listView.itemClicked.connect(self.item_selected)

        self.ClassLab = QtWidgets.QTextBrowser(self.centralwidget)
        self.ClassLab.setGeometry(QtCore.QRect(480, 440, 291, 31))
        self.ClassLab.setObjectName("ClassLab")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 395, 301, 41))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label.setScaledContents(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Programme"))
        self.OpenTest.setText(_translate("MainWindow", "Open File"))
        self.groupBox.setTitle(_translate("MainWindow", "ImageViewer"))
        self.SaveFile.setText(_translate("MainWindow", "Save File With Labels"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Classification Result :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Label : displays the true label in case where you</span></p><p><span style=\" font-size:9pt; font-weight:600;\">load a file with labels </span></p></body></html>"))

    def close_application(self):
        sys.exit()

    def init_table(self):
        self.DataViewer.setColumnCount(0)
        self.DataViewer.setRowCount(0)

        self.DataViewer.setColumnCount(1)
        self.DataViewer.setRowCount(192)
        self.DataViewer.setHorizontalHeaderLabels(['Value'])

        head = open('header.txt','r')
        head = head.readlines()
        head = head[0].split(',')

        self.DataViewer.setVerticalHeaderLabels(head)

    def item_selected(self, item):
        item = str(item.text())
        indx = int(item.split(' ')[-1]) - 1
        feature = self.data[indx]
        self.init_table()
        i = -1
        for x in feature:
            self.DataViewer.setItem(i, 1, QtWidgets.QTableWidgetItem(x))
            i += 1
        
        labels = load_obj('labels_one_hot.pkl')
        feature = np.array([float(c) for c in feature])
        prediction = self.model.predict(feature.reshape(-1, 192))
        choice = np.argmax(prediction[0])
        choice = one_hot(100, choice)
        res = ''

        for key in labels:
            if np.array_equal(choice, labels[key]):
                self.ClassResult.setText(key)
                res = key

        res = res.replace(' ', '_')
        pixmap = QtGui.QPixmap('image/'+res+'.jpg')
        
        self.label.setPixmap(pixmap)

        if self.isWithLabel:
            self.ClassLab.setText(self.all_labels[indx])

    def file_open(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.isWithLabel = False
            self.ClassLab.clear()
            self.label.clear()
            self.ClassResult.clear()
            self.init_table()
            self.data = []
            f = open(fileName, 'r')
            self.listView.clear()
            i = 1
            for line in f:
                line = (line.replace('\n','')).split(',')

                if len(line) == 193:
                    self.isWithLabel = True
                    self.all_labels.append(line[0])
                    del line[0]

                self.data.append(line)
                self.listView.addItem('row '+str(i))
                i += 1
    
    def file_save(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            f = open(fileName, 'w')

            labels = load_obj('labels_one_hot.pkl')
            for feature in self.data:
                featureX = feature
                feature = np.array([float(c) for c in feature])
                prediction = self.model.predict(feature.reshape(-1, 192))
                choice = np.argmax(prediction[0])
                choice = one_hot(100, choice)
                res = ''

                for key in labels:
                    if np.array_equal(choice, labels[key]):
                        res = key

                f.write(res+','+','.join(featureX)+'\n')

            f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

