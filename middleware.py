import settings
import init
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QAction, qApp, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPalette
from PyQt5.QtWidgets import QGridLayout, QStyle, QMenuBar, QMenu, QFileDialog
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, 
                             QAction, QPlainTextEdit, QStyle, QFileDialog,QMessageBox)
from PyQt5.QtCore import Qt, QRect
import AI
def getpos(x, y):
    rx = 0
    ry = 0
    for i in range(10):
        for j in range(11):
            if x<settings.chessAdjX+settings.posSize*i:
                continue
            if x>settings.chessAdjX+settings.posSize*i+settings.chessSize:
                continue
            if y<settings.chessAdjY+settings.posSize*j:
                continue
            if y>settings.chessAdjY+settings.posSize*j+settings.chessSize:
                continue
            rx = i
            ry = j
    return ry, rx
def checkturn(QW, tur, r, np, r2):
    while settings.gettype(tur) != 0: # the player is AI
        QW.statusBar().showMessage("Player "+str(2-tur)+"(AI) calculating...")
        QApplication.processEvents()
        AI.mov2(QW, tur, r, settings.gettype(tur))
        QW.pos_ = init.convert(QW.r)
        QW.drawc()
        if QW.end == 1:
            reply = QMessageBox.question(QW, 'Message',"Player "+str(1+QW.tur)+" has won the game. Would you like to save the record?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                QW.FSaveas()
            QW.close()
        tur = 1-tur
    QW.statusBar().showMessage("Ready, it\'s player "+str(2-tur)+"\'s turn.")
    return tur, r, np, r2