# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Informatics_plugin_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InformaticsPluginDialogBase(object):
    def setupUi(self, InformaticsPluginDialogBase):
        InformaticsPluginDialogBase.setObjectName("InformaticsPluginDialogBase")
        InformaticsPluginDialogBase.resize(562, 325)
        InformaticsPluginDialogBase.setAutoFillBackground(True)
        self.tab = QtWidgets.QTabWidget(InformaticsPluginDialogBase)
        self.tab.setGeometry(QtCore.QRect(10, 10, 541, 261))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.tab.setFont(font)
        self.tab.setAutoFillBackground(True)
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.General = QtWidgets.QWidget()
        self.General.setAutoFillBackground(True)
        self.General.setObjectName("General")
        self.groupBox = QtWidgets.QGroupBox(self.General)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 211))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Select_layer = QtWidgets.QLabel(self.groupBox)
        self.Select_layer.setGeometry(QtCore.QRect(10, 20, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer.setFont(font)
        self.Select_layer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer.setScaledContents(False)
        self.Select_layer.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer.setObjectName("Select_layer")
        self.mMapLayerComboBox = QgsMapLayerComboBox(self.groupBox)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(220, 20, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.mMapLayerComboBox.setFont(font)
        self.mMapLayerComboBox.setAutoFillBackground(False)
        self.mMapLayerComboBox.setStyleSheet("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushbutton_count\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>20</x>\n"
"     <y>160</y>\n"
"     <width>93</width>\n"
"     <height>28</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>count</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.Select_layer_2 = QtWidgets.QLabel(self.groupBox)
        self.Select_layer_2.setGeometry(QtCore.QRect(10, 90, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer_2.setFont(font)
        self.Select_layer_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer_2.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer_2.setScaledContents(False)
        self.Select_layer_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer_2.setObjectName("Select_layer_2")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 65, 481, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushbutton_count = QtWidgets.QPushButton(self.groupBox)
        self.pushbutton_count.setGeometry(QtCore.QRect(10, 120, 93, 28))
        self.pushbutton_count.setObjectName("pushbutton_count")
        self.label_select = QtWidgets.QLabel(self.groupBox)
        self.label_select.setGeometry(QtCore.QRect(280, 90, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_select.setFont(font)
        self.label_select.setText("")
        self.label_select.setObjectName("label_select")
        self.tab.addTab(self.General, "")
        self.Description = QtWidgets.QWidget()
        self.Description.setAutoFillBackground(True)
        self.Description.setObjectName("Description")
        self.label_active = QtWidgets.QLabel(self.Description)
        self.label_active.setGeometry(QtCore.QRect(180, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_active.setFont(font)
        self.label_active.setText("")
        self.label_active.setObjectName("label_active")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Description)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 511, 211))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.Select_layer_3 = QtWidgets.QLabel(self.groupBox_2)
        self.Select_layer_3.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer_3.setFont(font)
        self.Select_layer_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer_3.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer_3.setScaledContents(False)
        self.Select_layer_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer_3.setObjectName("Select_layer_3")
        self.Select_layer_4 = QtWidgets.QLabel(self.groupBox_2)
        self.Select_layer_4.setGeometry(QtCore.QRect(10, 50, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer_4.setFont(font)
        self.Select_layer_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer_4.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer_4.setScaledContents(False)
        self.Select_layer_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer_4.setObjectName("Select_layer_4")
        self.listObjects = QtWidgets.QTextEdit(self.groupBox_2)
        self.listObjects.setGeometry(QtCore.QRect(10, 70, 331, 131))
        self.listObjects.setObjectName("listObjects")
        self.pushbutton_showcoordinates = QtWidgets.QPushButton(self.groupBox_2)
        self.pushbutton_showcoordinates.setGeometry(QtCore.QRect(350, 170, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_showcoordinates.setFont(font)
        self.pushbutton_showcoordinates.setObjectName("pushbutton_showcoordinates")
        self.groupBox_2.raise_()
        self.label_active.raise_()
        self.tab.addTab(self.Description, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 511, 211))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.Select_layer_7 = QtWidgets.QLabel(self.groupBox_3)
        self.Select_layer_7.setGeometry(QtCore.QRect(10, 10, 321, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer_7.setFont(font)
        self.Select_layer_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer_7.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer_7.setScaledContents(False)
        self.Select_layer_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer_7.setObjectName("Select_layer_7")
        self.listoHigh = QtWidgets.QLabel(self.groupBox_3)
        self.listoHigh.setGeometry(QtCore.QRect(10, 40, 451, 71))
        self.listoHigh.setText("")
        self.listoHigh.setWordWrap(True)
        self.listoHigh.setObjectName("listoHigh")
        self.pushbutton_hight = QtWidgets.QPushButton(self.groupBox_3)
        self.pushbutton_hight.setGeometry(QtCore.QRect(400, 170, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_hight.setFont(font)
        self.pushbutton_hight.setObjectName("pushbutton_hight")
        self.tab.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 511, 211))
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.Select_layer_8 = QtWidgets.QLabel(self.groupBox_4)
        self.Select_layer_8.setGeometry(QtCore.QRect(10, 10, 441, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer_8.setFont(font)
        self.Select_layer_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer_8.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer_8.setScaledContents(False)
        self.Select_layer_8.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer_8.setObjectName("Select_layer_8")
        self.comboBox_unit = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_unit.setGeometry(QtCore.QRect(10, 40, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_unit.setFont(font)
        self.comboBox_unit.setEditable(True)
        self.comboBox_unit.setObjectName("comboBox_unit")
        self.comboBox_unit.addItem("")
        self.comboBox_unit.addItem("")
        self.comboBox_unit.addItem("")
        self.Select_layer_9 = QtWidgets.QLabel(self.groupBox_4)
        self.Select_layer_9.setGeometry(QtCore.QRect(10, 80, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer_9.setFont(font)
        self.Select_layer_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer_9.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer_9.setScaledContents(False)
        self.Select_layer_9.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer_9.setObjectName("Select_layer_9")
        self.label_area = QtWidgets.QLabel(self.groupBox_4)
        self.label_area.setGeometry(QtCore.QRect(120, 80, 381, 31))
        self.label_area.setText("")
        self.label_area.setWordWrap(True)
        self.label_area.setObjectName("label_area")
        self.label_crs = QtWidgets.QLabel(self.groupBox_4)
        self.label_crs.setGeometry(QtCore.QRect(180, 120, 141, 21))
        self.label_crs.setText("")
        self.label_crs.setObjectName("label_crs")
        self.Select_layer_10 = QtWidgets.QLabel(self.groupBox_4)
        self.Select_layer_10.setGeometry(QtCore.QRect(10, 120, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Select_layer_10.setFont(font)
        self.Select_layer_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Select_layer_10.setTextFormat(QtCore.Qt.AutoText)
        self.Select_layer_10.setScaledContents(False)
        self.Select_layer_10.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Select_layer_10.setObjectName("Select_layer_10")
        self.pushbutton_calculate = QtWidgets.QPushButton(self.groupBox_4)
        self.pushbutton_calculate.setGeometry(QtCore.QRect(400, 170, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_calculate.setFont(font)
        self.pushbutton_calculate.setObjectName("pushbutton_calculate")
        self.tab.addTab(self.tab_2, "")
        self.pushbutton_clear = QtWidgets.QPushButton(InformaticsPluginDialogBase)
        self.pushbutton_clear.setGeometry(QtCore.QRect(10, 280, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_clear.setFont(font)
        self.pushbutton_clear.setAutoFillBackground(True)
        self.pushbutton_clear.setStyleSheet("")
        self.pushbutton_clear.setObjectName("pushbutton_clear")
        self.pushbutton_close = QtWidgets.QPushButton(InformaticsPluginDialogBase)
        self.pushbutton_close.setGeometry(QtCore.QRect(460, 280, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_close.setFont(font)
        self.pushbutton_close.setObjectName("pushbutton_close")
        self.pushbutton_report = QtWidgets.QPushButton(InformaticsPluginDialogBase)
        self.pushbutton_report.setGeometry(QtCore.QRect(180, 280, 201, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_report.setFont(font)
        self.pushbutton_report.setObjectName("pushbutton_report")

        self.retranslateUi(InformaticsPluginDialogBase)
        self.tab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(InformaticsPluginDialogBase)

    def retranslateUi(self, InformaticsPluginDialogBase):
        _translate = QtCore.QCoreApplication.translate
        InformaticsPluginDialogBase.setWindowTitle(_translate("InformaticsPluginDialogBase", "Informatics Plugin"))
        self.tab.setWhatsThis(_translate("InformaticsPluginDialogBase", "<html><head/><body><p><br/></p></body></html>"))
        self.Select_layer.setText(_translate("InformaticsPluginDialogBase", "Select the appropriate layer:"))
        self.Select_layer_2.setText(_translate("InformaticsPluginDialogBase", "Count the number of objects selected:"))
        self.pushbutton_count.setText(_translate("InformaticsPluginDialogBase", "Count"))
        self.tab.setTabText(self.tab.indexOf(self.General), _translate("InformaticsPluginDialogBase", "General"))
        self.Select_layer_3.setText(_translate("InformaticsPluginDialogBase", "Name of active layer:"))
        self.Select_layer_4.setText(_translate("InformaticsPluginDialogBase", "Coordinates of selected points:"))
        self.pushbutton_showcoordinates.setText(_translate("InformaticsPluginDialogBase", "Show"))
        self.tab.setTabText(self.tab.indexOf(self.Description), _translate("InformaticsPluginDialogBase", "Description"))
        self.Select_layer_7.setText(_translate("InformaticsPluginDialogBase", "Calculate the elevation between the two points:"))
        self.pushbutton_hight.setText(_translate("InformaticsPluginDialogBase", "Calculate"))
        self.tab.setTabText(self.tab.indexOf(self.tab_3), _translate("InformaticsPluginDialogBase", " Elevation"))
        self.Select_layer_8.setText(_translate("InformaticsPluginDialogBase", "Please select the unit in which you wish to calculate the elevation:"))
        self.comboBox_unit.setItemText(0, _translate("InformaticsPluginDialogBase", "m^2"))
        self.comboBox_unit.setItemText(1, _translate("InformaticsPluginDialogBase", "Are"))
        self.comboBox_unit.setItemText(2, _translate("InformaticsPluginDialogBase", "Hectare"))
        self.Select_layer_9.setText(_translate("InformaticsPluginDialogBase", "Calculate area:"))
        self.Select_layer_10.setText(_translate("InformaticsPluginDialogBase", "Coordinate system:"))
        self.pushbutton_calculate.setText(_translate("InformaticsPluginDialogBase", "Calculate"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("InformaticsPluginDialogBase", "Area"))
        self.pushbutton_clear.setText(_translate("InformaticsPluginDialogBase", "Clear all"))
        self.pushbutton_close.setText(_translate("InformaticsPluginDialogBase", "Close"))
        self.pushbutton_report.setText(_translate("InformaticsPluginDialogBase", "Generate report"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InformaticsPluginDialogBase = QtWidgets.QDialog()
    ui = Ui_InformaticsPluginDialogBase()
    ui.setupUi(InformaticsPluginDialogBase)
    InformaticsPluginDialogBase.show()
    sys.exit(app.exec_())
