# -*- coding: utf-8 -*-


# Created: Thu Apr 02 15:51:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    

class Ui_findReplace(object):
    def setupUi(self, findReplace):
        findReplace.setObjectName("findReplace")
        findReplace.resize(246, 101)
        self.verticalLayout = QVBoxLayout(findReplace)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.replace_le = QLineEdit(findReplace)
        self.replace_le.setObjectName("replace_le")
        self.gridLayout.addWidget(self.replace_le, 1, 0, 1, 1)
        self.find_le = QLineEdit(findReplace)
        self.find_le.setObjectName("find_le")
        self.gridLayout.addWidget(self.find_le, 0, 0, 1, 1)
        self.find_btn = QPushButton(findReplace)
        self.find_btn.setObjectName("find_btn")
        self.gridLayout.addWidget(self.find_btn, 0, 1, 1, 1)
        self.replace_btn = QPushButton(findReplace)
        self.replace_btn.setObjectName("replace_btn")
        self.gridLayout.addWidget(self.replace_btn, 1, 1, 1, 1)
        self.replaceAll_btn = QPushButton(findReplace)
        self.replaceAll_btn.setObjectName("replaceAll_btn")
        self.gridLayout.addWidget(self.replaceAll_btn, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(findReplace)
        QMetaObject.connectSlotsByName(findReplace)
        findReplace.setTabOrder(self.find_le, self.replace_le)
        findReplace.setTabOrder(self.replace_le, self.find_btn)
        findReplace.setTabOrder(self.find_btn, self.replace_btn)
        findReplace.setTabOrder(self.replace_btn, self.replaceAll_btn)

    def retranslateUi(self, findReplace):
        findReplace.setWindowTitle(QApplication.translate("findReplace", "Find and Replace", None))
        self.find_btn.setText(QApplication.translate("findReplace", "Find", None))
        self.replace_btn.setText(QApplication.translate("findReplace", "Replace", None))
        self.replaceAll_btn.setText(QApplication.translate("findReplace", "Replace All", None))

