import sys
import os
import init
import settings
import middleware
import move
import main
import time
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QAction, qApp, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPalette
from PyQt5.QtWidgets import QGridLayout, QStyle, QMenuBar, QMenu, QFileDialog

from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, 
                             QAction, QPlainTextEdit, QStyle, QFileDialog,QMessageBox)

from PyQt5.QtCore import Qt, QRect

che = []
hi = []
manual = str(os.path.split(os.path.realpath(__file__))[0]+"\README.md")

class START(QMainWindow):
    def initData(self):
        self.tur, self.r, self.np, self.r2 = init.load(self, "start.che")
        self.pos_ = init.convert(self.r)
    def __init__(self):
        super().__init__()
        self.state = 0 + 0
        self.initData()
        self.initUI()
        self.end = 0
        self.tur, self.r, self.np, self.r2 = middleware.checkturn(self, self.tur, self.r, self.np, self.r2)
    def initMenu(self):
        self.path = None
        menub = self.menuBar()
        fileMenu = menub.addMenu('&File') 
        setMenu = menub.addMenu('&Settings')
        helpMenu = menub.addMenu('&Help')
        style = QApplication.style()
        newAct = QAction('New', self)
        newAct.setIcon(style.standardIcon(QStyle.SP_FileIcon))
        newAct.triggered.connect(self.FNew)
        loadAct = QAction('Load', self)
        loadAct.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        loadAct.triggered.connect(self.FLoad)
        saveAct = QAction('Save', self)
        saveAct.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        saveAct.triggered.connect(self.FSave)
        saveasAct = QAction('Save as', self)
        saveasAct.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        saveasAct.triggered.connect(self.FSaveas)
        quitAct = QAction(QIcon('img/exit24.png'),'Quit', self)
        quitAct.triggered.connect(self.close)

        set1 = QMenu('Set player 1 as AI', self)
        set1.setIcon(style.standardIcon(QStyle.SP_ComputerIcon))
        set2 = QMenu('Set player 2 as AI', self)
        set2.setIcon(style.standardIcon(QStyle.SP_ComputerIcon))

        set11 = QAction('Level 1', self)
        set11.setIcon(style.standardIcon(QStyle.SP_ArrowUp))
        set11.triggered.connect(self.chg11)
        set12 = QAction('Level 2', self)
        set12.setIcon(style.standardIcon(QStyle.SP_ArrowUp))
        set12.triggered.connect(self.chg12)
        set13 = QAction('Level 3', self)
        set13.setIcon(style.standardIcon(QStyle.SP_ArrowUp))
        set13.triggered.connect(self.chg13)
        set10 = QAction('Cancel', self)
        set10.setIcon(style.standardIcon(QStyle.SP_DialogCancelButton))
        set10.triggered.connect(self.chg10)
        set21 = QAction('Level 1', self)
        set21.setIcon(style.standardIcon(QStyle.SP_ArrowUp))
        set21.triggered.connect(self.chg21)
        set22 = QAction('Level 2', self)
        set22.setIcon(style.standardIcon(QStyle.SP_ArrowUp))
        set22.triggered.connect(self.chg22)
        set23 = QAction('Level 3', self)
        set23.setIcon(style.standardIcon(QStyle.SP_ArrowUp))
        set23.triggered.connect(self.chg23)
        set20 = QAction('Cancel', self)
        set20.setIcon(style.standardIcon(QStyle.SP_DialogCancelButton))
        set20.triggered.connect(self.chg20)

        manu = QAction('User manual', self)
        manu.setIcon(style.standardIcon(QStyle.SP_MessageBoxQuestion))
        manu.triggered.connect(self.openman)
        about = QAction('About', self)
        about.setIcon(style.standardIcon(QStyle.SP_MessageBoxInformation))
        about.triggered.connect(self.info)
        
        fileMenu.addAction(newAct)
        fileMenu.addAction(loadAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveasAct)
        fileMenu.addAction(quitAct)
        setMenu.addMenu(set1)
        setMenu.addMenu(set2)
        helpMenu.addAction(manu)
        helpMenu.addAction(about)
        set1.addAction(set11)
        set1.addAction(set12)
        set1.addAction(set13)
        set1.addAction(set10)
        set2.addAction(set21)
        set2.addAction(set22)
        set2.addAction(set23)
        set2.addAction(set20)

    def openman(self):
        os.startfile(manual)
    def info(self):
        QMessageBox.about(self, "About", "Author: Tianxing Yang\nEmail: talexyeung@gmail.com")
    def chg11(self):
        settings.setAI(1, 1)
    def chg12(self):
        settings.setAI(1, 2)
    def chg13(self):
        settings.setAI(1, 3)
    def chg10(self):
        settings.setAI(1, 0)
    def chg21(self):
        settings.setAI(0, 1)
    def chg22(self):
        settings.setAI(0, 2)
    def chg23(self):
        settings.setAI(0, 3)    
    def chg20(self):
        settings.setAI(0, 0)
    def initFrameWork(self):
        self.resize(815, 960)
        self.setWindowTitle('China Chess') 
        self.setWindowIcon(QIcon('img/web.png'))
    def initUI(self):  

        self.initFrameWork()
        self.center()
        self.initMenu()
        
        # background chessboard
        
        labelbg = QLabel(self)
        
        labelbg.setGeometry(QRect(-5, 30, 820, 903))
        labelbg.setPixmap(QPixmap("img/chessboard2.png"))
        self.setMouseTracking(True)
        self.initchess()
        self.drawc()
        self.show()
    def mousePressEvent(self, e):
        if self.state == 0:
            self.px, self.py = middleware.getpos(e.x(), e.y())
            if self.px>0 and self.py>0 and self.tur+1 == self.r[self.px][self.py].op:
                # print(self.px, self.py)
                self.state = 1
                self.HI = move.check(self.r, self.px, self.py)
                self.statusBar().showMessage("You have chosen a chess. Now select a target.")
        else:
            gx, gy = middleware.getpos(e.x(), e.y())
            if self.HI[gx][gy] == 1:
                
                self.np, self.r2 = move.mov(self, self.r, self.px, self.py, gx, gy, self.np, self.r2)
                self.tur = 1-self.tur
                self.pos_ = init.convert(self.r)
                self.drawc()
                self.show()
                if self.end == 1:
                    reply = QMessageBox.question(self, 'Message',"Player "+str(1+self.tur)+" has won the game. Would you like to save the record?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        self.FSaveas()
                    self.close()
            self.state = 0
            self.tur, self.r, self.np, self.r2 = middleware.checkturn(self, self.tur, self.r, self.np, self.r2)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def FNew(self):
        self.tur, self.r, self.np, self.r2 = init.load(self, "start.che")
        self.path = None
        self.pos_ = init.convert(self.r)
        self.drawc()
        self.tur, self.r, self.np, self.r2 = middleware.checkturn(self, self.tur, self.r, self.np, self.r2)
    def FLoad(self):
        self.path,_ = QFileDialog.getOpenFileName(self, 'Load Game', '', 'chess file (*.che)')
        self.pos_ = init.convert(self.r)
        self.drawc()
        self.tur, self.r, self.np, self.r2 = init.load(self, self.path)
        self.pos_ = init.convert(self.r)
        self.drawc()
    def FSave(self):
        if self.path is None:
            return self.FSaveas()
        init.save(self.path, self.tur, self.r, self.np, self.r2)
    def FSaveas(self):
        self.path,_ = QFileDialog.getSaveFileName(self, 'Save Game', '', 'chess file (*.che)')
        if not self.path:
            return
        init.save(self.path, self.tur, self.r, self.np, self.r2)
    def initchess(self):
        for i in range(32):
            che.append(QLabel(self))
            if i<16:
                if i>10:
                    che[i].setPixmap(QPixmap("img/BC/7.png"))
                else:
                    che[i].setPixmap(QPixmap("img/BC/"+str((i+3)//2)+".png"))
            else:
                if i>26:
                    che[i].setPixmap(QPixmap("img/RC/7.png"))
                else:
                    che[i].setPixmap(QPixmap("img/RC/"+str((i-13)//2)+".png"))
            che[i].setVisible(False)
    def drawc(self):
        for i in range(32):
            if self.pos_[i][0] == 0:
                che[i].setVisible(False)
            else:
                che[i].setGeometry(QRect(settings.chessAdjX+settings.posSize*self.pos_[i][1], settings.chessAdjY+settings.posSize*self.pos_[i][0], settings.chessSize, settings.chessSize))
                che[i].setVisible(True)