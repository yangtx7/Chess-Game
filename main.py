import init
import move
import GUI
import sys
import os
import AI

def demo1():
    
    app = GUI.QApplication(sys.argv)
    ex = GUI.START()
    
    sys.exit(app.exec_())
def demo0():
    tur, r, np, r2 = init.load("tmp.che")
    while 1:
        if tur == 1:
            print("It\'s RED turn. Which chess do you want to move?")
        else:
            print("It\'s BLACK turn. Which chess do you want to move?")
        inp = input()
        x = (int)(inp.split(' ')[0])
        y = (int)(inp.split(' ')[1])
        ava = move.check(r, x, y)
        print("Chess status:", r[x][y].op, r[x][y].id)
        print("Possible moves:")
        for i in range(11):
            for j in range(10):
                if ava[i][j] == 1:
                    print("(", i, " ", j, ") ", sep='', end='')
        print(" ")
        inp = input()
        xx = (int)(inp.split(' ')[0])
        yy = (int)(inp.split(' ')[1])
        np, r2 = move.mov(r, x, y, xx, yy, np, r2)
        tur = 1 - tur
        init.save("tmp.che", tur, r, np, r2)
if __name__ == '__main__':
    AI.randinit()
    demo1()
    #demo0()
