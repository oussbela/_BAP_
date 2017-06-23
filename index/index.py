# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(710, 442)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 10, 281, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 261, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.upload = QtGui.QPushButton(Dialog)
        self.upload.setGeometry(QtCore.QRect(130, 210, 111, 41))
        self.upload.setObjectName(_fromUtf8("upload"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 170, 161, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(290, 170, 20, 101))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.start = QtGui.QToolButton(Dialog)
        self.start.setGeometry(QtCore.QRect(260, 330, 131, 51))
        self.start.setObjectName(_fromUtf8("start"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(540, 420, 161, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.krichtextedit = KRichTextEdit(Dialog)
        self.krichtextedit.setGeometry(QtCore.QRect(330, 160, 321, 111))
        self.krichtextedit.setObjectName(_fromUtf8("krichtextedit"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 340, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(290, 150, 21, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Dialog)
       # QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_formUtf8(clicked)))
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/LOGO\"/></p></body></html>", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/LOGO\"/><span style=\" font-weight:600;\">Bacterium Analysis PIpeline</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">1. Please enter your Bacteria sequence</span></p></body></html>", None))
        self.upload.setText(_translate("Dialog", "UPLOAD", None))
        self.label_3.setText(_translate("Dialog", "Upload file from computer", None))
        self.start.setText(_translate("Dialog", "BAP START", None))
        self.label_4.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#aaaaff;\">MedBiotech credits @ 2017 </span></p></body></html>", None))
        self.krichtextedit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copy and paste your sequence here</p></body></html>", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>2. RUN BAP</p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>OR</p><p><br/></p></body></html>", None))

from krichtextedit import KRichTextEdit
import ressources_rc
