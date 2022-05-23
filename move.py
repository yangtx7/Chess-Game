import init
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QAction, qApp, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPalette
from PyQt5.QtWidgets import QGridLayout, QStyle, QMenuBar, QMenu, QFileDialog

from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, 
                             QAction, QPlainTextEdit, QStyle, QFileDialog,QMessageBox)

from PyQt5.QtCore import Qt, QRect
import AI
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dx1 = [1, 2, 1, 2, -1, -2, -1, -2]
dy1 = [2, 1, -2, -1, 2, 1, -2, -1]
dx2 = [2, 2, -2, -2]
dy2 = [2, -2, 2, -2]
dx3 = [1, 1, -1, -1]
dy3 = [1, -1, 1, -1]


def check(rr, x: int, y: int):
    nw = init.chess(0, 0)
    nw = rr[x][y]
    ret = [[0]*10 for i in range(11)]
    if nw.op == 0:
        return ret
    if nw.id == 1:  # general
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if nw.op == 1:
                if yy < 4 or yy > 6 or xx < 1 or xx > 3:
                    continue
                if rr[xx][yy].op == 1:
                    continue
                ret[xx][yy] = 1
            if nw.op == 2:
                if yy < 4 or yy > 6 or xx < 8 or xx > 10:
                    continue
                if rr[xx][yy].op == 2:
                    continue
                ret[xx][yy] = 1
        if nw.op == 1:
            for i in range(x+1, 11):
                if rr[i][y].op == 1:
                    break
                if rr[i][y].op == 2:
                    if rr[i][y].id == 1:
                        ret[i][y] = 1
                    break
        if nw.op == 2:
            for i in range(x-1, 0, -1):
                if rr[i][y].op == 2:
                    break
                if rr[i][y].op == 1:
                    if rr[i][y].id == 1:
                        ret[i][y] = 1
                    break
    if nw.id == 2:  # advisor
        for i in range(4):
            xx = x+dx3[i]
            yy = y+dy3[i]
            if nw.op == 1:
                if yy < 4 or yy > 6 or xx < 1 or xx > 3:
                    continue
                if rr[xx][yy].op == 1:
                    continue
                ret[xx][yy] = 1
            if nw.op == 2:
                if yy < 4 or yy > 6 or xx < 8 or xx > 10:
                    continue
                if rr[xx][yy].op == 2:
                    continue
                ret[xx][yy] = 1
    if nw.id == 3:  # elephant
        for i in range(4):
            xx = x+dx2[i]
            yy = y+dy2[i]
            if nw.op == 1:
                if yy < 1 or yy > 9 or xx < 1 or xx > 5:
                    continue
                if rr[xx][yy].op == 1:
                    continue
                if rr[(x+xx) // 2][(y+yy) // 2].op != 0:
                    continue
                ret[xx][yy] = 1
            if nw.op == 2:
                if yy < 1 or yy > 9 or xx < 6 or xx > 10:
                    continue
                if rr[xx][yy].op == 2:
                    continue
                if rr[(x+xx) // 2][(y+yy) // 2].op != 0:
                    continue
                ret[xx][yy] = 1
    if nw.id == 4:  # horse
        for i in range(8):
            xx = x+dx1[i]
            yy = y+dy1[i]
            if yy < 1 or yy > 9 or xx < 1 or xx > 10:
                continue
            if rr[xx][yy].op == nw.op:
                continue
            if abs(x-xx) == 2:
                if rr[(x+xx) // 2][y].op != 0:
                    continue
            else:
                if rr[x][(y+yy) // 2].op != 0:
                    continue
            ret[xx][yy] = 1
    if nw.id == 5:  # chariot
        # (x,y)->(i,y)
        for i in range(x+1, 11):
            if rr[i][y].op != nw.op:
                ret[i][y] = 1
            if rr[i][y].op != 0:
                break
        for i in range(x-1, 0, -1):
            if rr[i][y].op != nw.op:
                ret[i][y] = 1
            if rr[i][y].op != 0:
                break
        # (x,y)->(x,i)
        for i in range(y+1, 10):
            if rr[x][i].op != nw.op:
                ret[x][i] = 1
            if rr[x][i].op != 0:
                break
        for i in range(y-1, 0, -1):
            if rr[x][i].op != nw.op:
                ret[x][i] = 1
            if rr[x][i].op != 0:
                break
    if nw.id == 6:  # cannon
        # fl: if cannon can find a midpoint
        # (x,y)->(i,y)
        fl = 0
        for i in range(x+1, 11):
            if rr[i][y].op != 0:
                if fl == 0:
                    fl = 1
                    continue
                if rr[i][y].op != nw.op:
                    ret[i][y] = 1
                break
            else:
                if fl == 0:
                    ret[i][y] = 1
        fl = 0
        for i in range(x-1, 0, -1):
            if rr[i][y].op != 0:
                if fl == 0:
                    fl = 1
                    continue
                if rr[i][y].op != nw.op:
                    ret[i][y] = 1
                break
            else:
                if fl == 0:
                    ret[i][y] = 1
        # (x,y)->(x,i)
        fl = 0
        for i in range(y+1, 10):
            if rr[x][i].op != 0:
                if fl == 0:
                    fl = 1
                    continue
                if rr[x][i].op != nw.op:
                    ret[x][i] = 1
                break
            else:
                if fl == 0:
                    ret[x][i] = 1
        fl = 0
        for i in range(y-1, 0, -1):
            if rr[x][i].op != 0:
                if fl == 0:
                    fl = 1
                    continue
                if rr[x][i].op != nw.op:
                    ret[x][i] = 1
                break
            else:
                if fl == 0:
                    ret[x][i] = 1
    if nw.id == 7:  # soldier
        # forward
        if nw.op == 1:
            if x != 10 and rr[x+1][y].op != 1:
                ret[x+1][y] = 1
        if nw.op == 2:
            if x != 1 and rr[x-1][y].op != 2:
                ret[x-1][y] = 1
        # move left/right
        if (nw.op == 1 and x >= 6) or (nw.op == 2 and x <= 5):
            if y > 1 and rr[x][y-1].op != nw.op:
                ret[x][y-1] = 1
            if y < 9 and rr[x][y+1].op != nw.op:
                ret[x][y+1] = 1
    return ret


def mov(QW, r, x, y, xx, yy, np: int, r2: list):
    if r[xx][yy].id == 1:
        QW.end = 1
    r[xx][yy] = r[x][y]
    r[x][y] = init.chess(0, 0)
    r2[np][0] = x
    r2[np][1] = y
    r2[np][2] = xx
    r2[np][3] = yy
    np += 1
    print("player ",2-QW.tur,":(",x,",",y,")->(",xx,",",yy,")",sep='')
    print("current evaluation =",AI.eval(r))
    return np, r2
