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
        InformaticsPluginDialogBase.resize(764, 578)
        self.button_box = QtWidgets.QDialogButtonBox(InformaticsPluginDialogBase)
        self.button_box.setGeometry(QtCore.QRect(300, 530, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.one = QtWidgets.QGroupBox(InformaticsPluginDialogBase)
        self.one.setGeometry(QtCore.QRect(20, 20, 241, 201))
        self.one.setTitle("")
        self.one.setObjectName("one")
        self.pushbutton_count = QtWidgets.QPushButton(self.one)
        self.pushbutton_count.setGeometry(QtCore.QRect(20, 160, 93, 28))
        self.pushbutton_count.setObjectName("pushbutton_count")
        self.mMapLayerComboBox = QgsMapLayerComboBox(self.one)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(10, 40, 160, 27))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.Select_layer = QtWidgets.QLabel(self.one)
        self.Select_layer.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.Select_layer.setObjectName("Select_layer")
        self.label_select = QtWidgets.QLabel(self.one)
        self.label_select.setGeometry(QtCore.QRect(20, 110, 55, 16))
        self.label_select.setText("")
        self.label_select.setObjectName("label_select")
        self.two = QtWidgets.QGroupBox(InformaticsPluginDialogBase)
        self.two.setGeometry(QtCore.QRect(20, 220, 241, 331))
        self.two.setTitle("")
        self.two.setObjectName("two")
        self.pushbutton_showcoordinates = QtWidgets.QPushButton(self.two)
        self.pushbutton_showcoordinates.setGeometry(QtCore.QRect(10, 290, 131, 28))
        self.pushbutton_showcoordinates.setObjectName("pushbutton_showcoordinates")
        self.name_active = QtWidgets.QLabel(self.two)
        self.name_active.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.name_active.setObjectName("name_active")
        self.coordinates_of_selected = QtWidgets.QLabel(self.two)
        self.coordinates_of_selected.setGeometry(QtCore.QRect(10, 120, 181, 16))
        self.coordinates_of_selected.setObjectName("coordinates_of_selected")
        self.listObjects = QtWidgets.QTextEdit(self.two)
        self.listObjects.setGeometry(QtCore.QRect(10, 150, 211, 131))
        self.listObjects.setObjectName("listObjects")
        self.label_active = QtWidgets.QLabel(self.two)
        self.label_active.setGeometry(QtCore.QRect(10, 60, 55, 16))
        self.label_active.setText("")
        self.label_active.setObjectName("label_active")
        self.tr = QtWidgets.QGroupBox(InformaticsPluginDialogBase)
        self.tr.setGeometry(QtCore.QRect(270, 20, 221, 241))
        self.tr.setTitle("")
        self.tr.setObjectName("tr")
        self.label_area = QtWidgets.QLabel(self.tr)
        self.label_area.setGeometry(QtCore.QRect(10, 110, 171, 61))
        self.label_area.setText("")
        self.label_area.setWordWrap(True)
        self.label_area.setObjectName("label_area")
        self.label = QtWidgets.QLabel(self.tr)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.comboBox_unit = QtWidgets.QComboBox(self.tr)
        self.comboBox_unit.setGeometry(QtCore.QRect(10, 60, 181, 22))
        self.comboBox_unit.setEditable(True)
        self.comboBox_unit.setObjectName("comboBox_unit")
        self.comboBox_unit.addItem("")
        self.comboBox_unit.addItem("")
        self.comboBox_unit.addItem("")
        self.pushbutton_calculate = QtWidgets.QPushButton(self.tr)
        self.pushbutton_calculate.setGeometry(QtCore.QRect(10, 200, 93, 28))
        self.pushbutton_calculate.setObjectName("pushbutton_calculate")
        self.fore = QtWidgets.QGroupBox(InformaticsPluginDialogBase)
        self.fore.setGeometry(QtCore.QRect(260, 270, 221, 161))
        self.fore.setObjectName("fore")
        self.pushbutton_hight = QtWidgets.QPushButton(self.fore)
        self.pushbutton_hight.setGeometry(QtCore.QRect(10, 120, 93, 28))
        self.pushbutton_hight.setObjectName("pushbutton_hight")
        self.listoHigh = QtWidgets.QLabel(self.fore)
        self.listoHigh.setGeometry(QtCore.QRect(10, 40, 191, 71))
        self.listoHigh.setText("")
        self.listoHigh.setWordWrap(True)
        self.listoHigh.setObjectName("listoHigh")
        self.five = QtWidgets.QGroupBox(InformaticsPluginDialogBase)
        self.five.setGeometry(QtCore.QRect(500, 20, 241, 171))
        self.five.setTitle("")
        self.five.setObjectName("five")
        self.label_crs = QtWidgets.QLabel(InformaticsPluginDialogBase)
        self.label_crs.setGeometry(QtCore.QRect(500, 200, 131, 61))
        self.label_crs.setText("")
        self.label_crs.setObjectName("label_crs")
        self.label_2 = QtWidgets.QLabel(InformaticsPluginDialogBase)
        self.label_2.setGeometry(QtCore.QRect(520, 310, 131, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.five.raise_()
        self.fore.raise_()
        self.tr.raise_()
        self.button_box.raise_()
        self.one.raise_()
        self.two.raise_()
        self.label_crs.raise_()
        self.label_2.raise_()

        self.retranslateUi(InformaticsPluginDialogBase)
        self.button_box.accepted.connect(InformaticsPluginDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(InformaticsPluginDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(InformaticsPluginDialogBase)

    def retranslateUi(self, InformaticsPluginDialogBase):
        _translate = QtCore.QCoreApplication.translate
        InformaticsPluginDialogBase.setWindowTitle(_translate("InformaticsPluginDialogBase", "Informatics Plugin"))
        self.pushbutton_count.setText(_translate("InformaticsPluginDialogBase", "count"))
        self.Select_layer.setText(_translate("InformaticsPluginDialogBase", "Select layer: "))
        self.pushbutton_showcoordinates.setText(_translate("InformaticsPluginDialogBase", "show coordinates"))
        self.name_active.setText(_translate("InformaticsPluginDialogBase", "Name of active layer:"))
        self.coordinates_of_selected.setText(_translate("InformaticsPluginDialogBase", "Coordinates of selected sites:"))
        self.label.setText(_translate("InformaticsPluginDialogBase", "Calculate area:"))
        self.comboBox_unit.setItemText(0, _translate("InformaticsPluginDialogBase", "m^2"))
        self.comboBox_unit.setItemText(1, _translate("InformaticsPluginDialogBase", "Ary"))
        self.comboBox_unit.setItemText(2, _translate("InformaticsPluginDialogBase", "Hektary"))
        self.pushbutton_calculate.setText(_translate("InformaticsPluginDialogBase", "calculate"))
        self.fore.setTitle(_translate("InformaticsPluginDialogBase", "Hight"))
        self.pushbutton_hight.setText(_translate("InformaticsPluginDialogBase", "hight"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InformaticsPluginDialogBase = QtWidgets.QDialog()
    ui = Ui_InformaticsPluginDialogBase()
    ui.setupUi(InformaticsPluginDialogBase)
    InformaticsPluginDialogBase.show()
    sys.exit(app.exec_())
