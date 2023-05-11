# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_2021-08-31.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(758, 480)
        self.gridLayout = QGridLayout(Window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dirEdit = QLineEdit(Window)
        self.dirEdit.setObjectName(u"dirEdit")
        self.dirEdit.setMinimumSize(QSize(0, 30))
        self.dirEdit.setMaximumSize(QSize(16777215, 30))
        self.dirEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.dirEdit, 1, 0, 1, 2)

        self.loadFilesButton = QPushButton(Window)
        self.loadFilesButton.setObjectName(u"loadFilesButton")
        self.loadFilesButton.setMinimumSize(QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(11)
        self.loadFilesButton.setFont(font)

        self.gridLayout.addWidget(self.loadFilesButton, 1, 2, 1, 1)

        self.splitter = QSplitter(Window)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.srcFileList = QListWidget(self.layoutWidget)
        self.srcFileList.setObjectName(u"srcFileList")

        self.verticalLayout.addWidget(self.srcFileList)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.dstFileList = QListWidget(self.layoutWidget1)
        self.dstFileList.setObjectName(u"dstFileList")

        self.verticalLayout_2.addWidget(self.dstFileList)

        self.splitter.addWidget(self.layoutWidget1)

        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 3)

        self.extensionLabel = QLabel(Window)
        self.extensionLabel.setObjectName(u"extensionLabel")
        self.extensionLabel.setMinimumSize(QSize(0, 30))
        self.extensionLabel.setMaximumSize(QSize(16777215, 30))
        self.extensionLabel.setFont(font)

        self.gridLayout.addWidget(self.extensionLabel, 6, 1, 1, 1)

        self.prefixEdit = QLineEdit(Window)
        self.prefixEdit.setObjectName(u"prefixEdit")
        self.prefixEdit.setMinimumSize(QSize(0, 30))
        self.prefixEdit.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        self.prefixEdit.setFont(font1)

        self.gridLayout.addWidget(self.prefixEdit, 6, 0, 1, 1)

        self.renameFilesButton = QPushButton(Window)
        self.renameFilesButton.setObjectName(u"renameFilesButton")
        self.renameFilesButton.setMinimumSize(QSize(0, 30))
        self.renameFilesButton.setMaximumSize(QSize(16777215, 30))
        self.renameFilesButton.setFont(font)

        self.gridLayout.addWidget(self.renameFilesButton, 6, 2, 1, 1)

        self.progressBar = QProgressBar(Window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 3)

        self.label = QLabel(Window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.groupBox = QGroupBox(Window)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 87))
        self.groupBox.setMaximumSize(QSize(16777215, 87))
        self.groupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.renameTypeBox = QComboBox(self.groupBox)
        self.renameTypeBox.addItem("")
        self.renameTypeBox.addItem("")
        self.renameTypeBox.addItem("")
        self.renameTypeBox.setObjectName(u"renameTypeBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renameTypeBox.sizePolicy().hasHeightForWidth())
        self.renameTypeBox.setSizePolicy(sizePolicy)
        self.renameTypeBox.setMinimumSize(QSize(250, 30))
        self.renameTypeBox.setMaximumSize(QSize(250, 30))
        self.renameTypeBox.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.renameTypeBox.setFont(font2)

        self.gridLayout_2.addWidget(self.renameTypeBox, 0, 0, 1, 1)

        self.renameTypeLabel = QLabel(self.groupBox)
        self.renameTypeLabel.setObjectName(u"renameTypeLabel")
        self.renameTypeLabel.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.renameTypeLabel.sizePolicy().hasHeightForWidth())
        self.renameTypeLabel.setSizePolicy(sizePolicy1)
        self.renameTypeLabel.setMinimumSize(QSize(400, 30))
        self.renameTypeLabel.setMaximumSize(QSize(16777215, 30))
        self.renameTypeLabel.setFont(font2)

        self.gridLayout_2.addWidget(self.renameTypeLabel, 0, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_1, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)

        self.label_4 = QLabel(Window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 15))
        self.label_4.setMaximumSize(QSize(16777215, 15))
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"My Renamer", None))
        self.loadFilesButton.setText(QCoreApplication.translate("Window", u"&Load Files", None))
        self.label_2.setText(QCoreApplication.translate("Window", u"Files to Rename", None))
        self.label_3.setText(QCoreApplication.translate("Window", u"Renamed Files", None))
        self.extensionLabel.setText(QCoreApplication.translate("Window", u"*.jpg", None))
        self.prefixEdit.setPlaceholderText(QCoreApplication.translate("Window", u"Rename your files to...", None))
        self.renameFilesButton.setText(QCoreApplication.translate("Window", u"&Rename", None))
        self.label.setText(QCoreApplication.translate("Window", u"Last Source Directory:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Window", u"Rename Type", None))
        self.renameTypeBox.setItemText(0, QCoreApplication.translate("Window", u"Prefix Rename", None))
        self.renameTypeBox.setItemText(1, QCoreApplication.translate("Window", u"Just Add Prefix", None))
        self.renameTypeBox.setItemText(2, QCoreApplication.translate("Window", u"Upper Case", None))

        self.renameTypeLabel.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Window", u"Filename Prefix:", None))
    # retranslateUi

