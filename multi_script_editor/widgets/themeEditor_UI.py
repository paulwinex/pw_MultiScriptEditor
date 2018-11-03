# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_prefs\RnD\tools\pw_scriptEditor\widgets\themeEditor.ui'
#
# Created: Mon Mar 16 10:29:57 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_themeEditor(object):
    def setupUi(self, themeEditor):
        themeEditor.setObjectName(_fromUtf8("themeEditor"))
        themeEditor.resize(724, 461)
        self.verticalLayout_3 = QtGui.QVBoxLayout(themeEditor)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(themeEditor)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.colors_lwd = QtGui.QListWidget(self.widget)
        self.colors_lwd.setObjectName(_fromUtf8("colors_lwd"))
        self.verticalLayout_2.addWidget(self.colors_lwd)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.textSize_spb = QtGui.QSpinBox(self.widget)
        self.textSize_spb.setMinimum(9)
        self.textSize_spb.setMaximum(25)
        self.textSize_spb.setProperty("value", 11)
        self.textSize_spb.setObjectName(_fromUtf8("textSize_spb"))
        self.horizontalLayout_3.addWidget(self.textSize_spb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.themeList_cbb = QtGui.QComboBox(self.layoutWidget)
        self.themeList_cbb.setObjectName(_fromUtf8("themeList_cbb"))
        self.horizontalLayout.addWidget(self.themeList_cbb)
        self.save_btn = QtGui.QPushButton(self.layoutWidget)
        self.save_btn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.horizontalLayout.addWidget(self.save_btn)
        self.del_btn = QtGui.QPushButton(self.layoutWidget)
        self.del_btn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.del_btn.setObjectName(_fromUtf8("del_btn"))
        self.horizontalLayout.addWidget(self.del_btn)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.preview_ly = QtGui.QVBoxLayout()
        self.preview_ly.setObjectName(_fromUtf8("preview_ly"))
        self.verticalLayout.addLayout(self.preview_ly)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.splitter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.apply_btn = QtGui.QPushButton(themeEditor)
        self.apply_btn.setObjectName(_fromUtf8("apply_btn"))
        self.horizontalLayout_2.addWidget(self.apply_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(0, 1)

        self.retranslateUi(themeEditor)
        QtCore.QMetaObject.connectSlotsByName(themeEditor)

    def retranslateUi(self, themeEditor):
        themeEditor.setWindowTitle(_translate("themeEditor", "Code Theme Editor", None))
        self.label.setText(_translate("themeEditor", "Completer text size", None))
        self.save_btn.setText(_translate("themeEditor", "Save", None))
        self.del_btn.setText(_translate("themeEditor", "Del", None))
        self.apply_btn.setText(_translate("themeEditor", "Save", None))

