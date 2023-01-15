# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerlcSpgq.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QDir, QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 420)
        MainWindow.setMinimumSize(QSize(420, 420))
        MainWindow.setMaximumSize(QSize(1080, 1080))
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setToolTipDuration(-1)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.removebtn = QPushButton(self.frame)
        self.removebtn.setObjectName(u"removebtn")
        self.removebtn.setEnabled(True)
        icon = QIcon()
        icon.addFile(u"test/Lab3/icons/minus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.removebtn.setIcon(icon)
        self.removebtn.setFlat(True)

        self.horizontalLayout.addWidget(self.removebtn)

        self.addbtn = QPushButton(self.frame)
        self.addbtn.setObjectName(u"addbtn")
        self.addbtn.setEnabled(True)

        icon1 = QIcon()
        icon1.addFile(u"test/Lab3/icons/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addbtn.setIcon(icon1)
        self.addbtn.setAutoDefault(False)
        self.addbtn.setFlat(True)

        self.horizontalLayout.addWidget(self.addbtn)

        self.textarea = QLineEdit(self.frame)
        self.textarea.setObjectName(u"textarea")

        self.horizontalLayout.addWidget(self.textarea)

        self.searchbtn = QPushButton(self.frame)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u"test/Lab3/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchbtn.setIcon(icon2)
        self.searchbtn.setAutoDefault(False)
        self.searchbtn.setFlat(True)

        self.horizontalLayout.addWidget(self.searchbtn)

        self.verticalLayout.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setMaximumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 420, 24))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionImport)

        self.retranslateUi(MainWindow)

        self.searchbtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import from csv", None))
        self.actionImport.setIcon(QIcon(u"test/Lab3/icons/upload.svg"))
        self.textarea.setPlaceholderText("Search By Key")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data", None))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

