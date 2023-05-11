# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-window_2021-11-10.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(783, 488)
        self.verticalLayout_3 = QVBoxLayout(Window)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dirEdit = QLineEdit(Window)
        self.dirEdit.setObjectName(u"dirEdit")
        self.dirEdit.setMinimumSize(QSize(0, 30))
        self.dirEdit.setMaximumSize(QSize(16777215, 30))
        self.dirEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.dirEdit)

        self.loadSrcButton = QPushButton(Window)
        self.loadSrcButton.setObjectName(u"loadSrcButton")
        self.loadSrcButton.setMinimumSize(QSize(120, 30))
        self.loadSrcButton.setMaximumSize(QSize(16777215, 30))
        self.loadSrcButton.setFont(font)

        self.horizontalLayout.addWidget(self.loadSrcButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 15))
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dirEdit_2 = QLineEdit(Window)
        self.dirEdit_2.setObjectName(u"dirEdit_2")
        self.dirEdit_2.setMinimumSize(QSize(0, 30))
        self.dirEdit_2.setMaximumSize(QSize(16777215, 30))
        self.dirEdit_2.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.dirEdit_2)

        self.loadXmlButton = QPushButton(Window)
        self.loadXmlButton.setObjectName(u"loadXmlButton")
        self.loadXmlButton.setMinimumSize(QSize(120, 30))
        self.loadXmlButton.setMaximumSize(QSize(16777215, 30))
        self.loadXmlButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.loadXmlButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(Window)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEnabled(False)

        self.gridLayout.addWidget(self.comboBox_2, 4, 0, 1, 1)

        self.runButton = QPushButton(self.groupBox)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setEnabled(False)
        self.runButton.setMinimumSize(QSize(0, 30))
        self.runButton.setMaximumSize(QSize(16777215, 30))
        self.runButton.setFont(font)

        self.gridLayout.addWidget(self.runButton, 5, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(180, 0))

        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Window)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_5.addWidget(self.label_3)

        self.dstFileList = QListWidget(self.groupBox_2)
        self.dstFileList.setObjectName(u"dstFileList")

        self.verticalLayout_5.addWidget(self.dstFileList)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.renameTypeLabel = QLabel(Window)
        self.renameTypeLabel.setObjectName(u"renameTypeLabel")
        self.renameTypeLabel.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renameTypeLabel.sizePolicy().hasHeightForWidth())
        self.renameTypeLabel.setSizePolicy(sizePolicy)
        self.renameTypeLabel.setMinimumSize(QSize(400, 30))
        self.renameTypeLabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.renameTypeLabel.setFont(font1)

        self.verticalLayout_3.addWidget(self.renameTypeLabel)

        self.progressBar = QProgressBar(Window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"Xml Parsing", None))
        self.label.setText(QCoreApplication.translate("Window", u"\u9078\u64c7\u7a0b\u5f0f\u6a94\u6848\u4f86\u6e90", None))
        self.loadSrcButton.setText(QCoreApplication.translate("Window", u"&Select Sources", None))
        self.label_2.setText(QCoreApplication.translate("Window", u"\u9078\u64c7XML\u6a94\u6848\u4f86\u6e90", None))
        self.loadXmlButton.setText(QCoreApplication.translate("Window", u"&Select XML file", None))
        self.groupBox.setTitle("")
        self.runButton.setText(QCoreApplication.translate("Window", u"&Copy", None))
        self.label_4.setText(QCoreApplication.translate("Window", u"Model Type", None))
        self.label_5.setText(QCoreApplication.translate("Window", u"Reserved", None))
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Window", u"Copyed Files", None))
        self.renameTypeLabel.setText(QCoreApplication.translate("Window", u"\u8907\u88fd\u6a94\u6848\u9032\u5ea6", None))
    # retranslateUi

