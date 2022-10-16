# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceenRghb.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QListWidget, QSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
from QTileLayout import QTileLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 686)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Output = QWidget(self.centralwidget)
        self.Output.setObjectName(u"Output")
        self.gridLayout_2 = QGridLayout(self.Output)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Blocks = QWidget(self.Output)
        self.Blocks.setObjectName(u"Blocks")
        self.Blocks.setStyleSheet(u"#Blocks {\n"
        "	border: 2px solid white;\n"
        "	border-radius: 40px;\n"
        "}\n"
        "\n"
        "#Blocks .QLabel {\n"
        "	border: 3px solid white;\n"
        "	border-radius: 20px;\n"
        "	font-size: 50pt;\n"
        "}")
        self.gridLayout_3 = QGridLayout(self.Blocks)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layoutblocks = QTileLayout(
            rowNumber=3,
            columnNumber=3,
            verticalSpan=200,
            horizontalSpan=200,
            verticalSpacing=5,
            horizontalSpacing=5,
        )
        for i, n in enumerate([[1,2,3],[4,5,6],[7,8]]):
            for j, m in enumerate(n):
                self.layoutblocks.addWidget(
                    widget= QLabel(str(m)),
                    fromRow=i,
                    fromColumn=j,
                    rowSpan=1,
                    columnSpan=1,
                )
        self.layoutblocks.setObjectName(u"layout")
        self.layoutblocks.acceptResizing(False)
        self.gridLayout_2.addWidget(self.Blocks, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.layoutblocks, 3, 3)

        self.horizontalLayout_2.addWidget(self.Output)

        self.OptionMenu = QWidget(self.centralwidget)
        self.OptionMenu.setObjectName(u"OptionMenu")
        self.OptionMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.OptionMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Options = QFrame(self.OptionMenu)
        self.Options.setObjectName(u"Options")
        self.Options.setMaximumSize(QSize(200, 16777215))
        self.Options.setFrameShape(QFrame.Shape.Panel)
        self.Options.setFrameShadow(QFrame.Shadow.Raised)
        self.Options.setLineWidth(2)
        self.gridLayout = QGridLayout(self.Options)
        self.gridLayout.setObjectName(u"gridLayout")
        self.RBFS = QRadioButton(self.Options)
        self.RBFS.setObjectName(u"RBFS")
        self.RBFS.setEnabled(True)
        self.RBFS.setAutoFillBackground(False)
        self.RBFS.setChecked(True)

        self.gridLayout.addWidget(self.RBFS, 1, 2, 1, 1)

        self.LDFS = QRadioButton(self.Options)
        self.LDFS.setObjectName(u"LDFS")

        self.gridLayout.addWidget(self.LDFS, 2, 2, 1, 1)
        
        self.MaxDepth = QSpinBox(self.Options)
        self.MaxDepth.setObjectName(u"MaxDepth")
        self.MaxDepth.setMinimum(1)
        self.MaxDepth.setMaximum(100)

        self.gridLayout.addWidget(self.MaxDepth, 3, 2, 1, 1)

        self.Shuffle = QPushButton(self.Options)
        self.Shuffle.setObjectName(u"Shuffle")

        self.gridLayout.addWidget(self.Shuffle, 1, 1, 1, 1)

        self.Run = QPushButton(self.Options)
        self.Run.setObjectName(u"Run")

        self.gridLayout.addWidget(self.Run, 2, 1, 1, 1)

        self.label = QLabel(self.Options)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.Options)

        self.progressBar = QProgressBar(self.OptionMenu)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.Moves = QListWidget(self.OptionMenu)
        self.Moves.setObjectName(u"Moves")

        self.Moves.setStyleSheet(u"font-size: 14pt;")
        self.verticalLayout_2.addWidget(self.Moves)


        self.horizontalLayout_2.addWidget(self.OptionMenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RBFS.setText(QCoreApplication.translate("MainWindow", u"RBFS", None))
        self.LDFS.setText(QCoreApplication.translate("MainWindow", u"LDFS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Max depth:", None))
        self.Shuffle.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        self.Run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi
