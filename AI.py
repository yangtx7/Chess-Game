import move
import copy
import init
import time 
import random
eva2 = [[[0]*90 for i in range(90)] for j in range(11)]
turr = 0
turr2 = 0
maxstate = 4194304
eva3 = [[[0]*90 for j in range(8)] for k in range(2)]
eva4 = [[[0]*90 for j in range(8)] for k in range(2)]
class hash():
    def __init__(self, h2, re):
        self.h2 = h2
        self.re = re
class ste():
    def __init__(self, p, x, y, dx, dy):
        self.p = p
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
    def __lt__(self, other):
        return eva2[self.p][self.y-1+9*(self.x-1)][self.dy-1+9*(self.dx-1)]>eva2[other.p][other.y-1+9*(other.x-1)][other.dy-1+9*(other.dx-1)]
class mo():
    def __init__(self):
        self.x, self.y, self.dx, self.dy = 0, 0, 0, 0
        self.lim, self.count = 0, 0

ht = [hash(0, 0) for i in range(maxstate)]

def randinit():
    turr = random.randint(0, maxstate-1)
    turr2 = random.randint(0, maxstate-1)
    for i in range(2):
        for j in range(1, 8):
            for k in range(90):
                eva3[i][j][k] = random.randint(0, maxstate-1)
                eva4[i][j][k] = random.randint(0, maxstate-1)

Mo = mo()
Bing = [
    [9,  9,  9, 11, 13, 11,  9,  9,  9],
    [19, 24, 34, 42, 44, 42, 34, 24, 19],
    [19, 24, 32, 37, 37, 37, 32, 24, 19],
    [19, 23, 27, 29, 30, 29, 27, 23, 19],
    [14, 18, 20, 27, 29, 27, 20, 18, 14],
    [7,  0, 13,  0, 16,  0, 13,  0,  7],
    [7,  0,  7,  0, 15,  0,  7,  0,  7],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0]
]
Jiang = [
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  9900,  9900,  9900,  0,  0,  0],
    [0,  0,  0,  9930,  9950,  9930,  0,  0,  0],
    [0,  0,  0, 9950, 10000, 9950,  0,  0,  0]
]
Shi_Xiang = [
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [0,  0, 20,  0,  0,  0, 20,  0,  0],  
    [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [18,  0,  0, 20, 23, 20,  0,  0, 18],  
    [0,  0,  0,  0, 23,  0,  0,  0,  0],  
    [0,  0, 20, 20,  0, 20, 20,  0,  0] 
]
Ma = [
    [90, 90, 90, 96, 90, 96, 90, 90, 90],
    [90, 96,103, 97, 94, 97,103, 96, 90],
    [92, 98, 99,103, 99,103, 99, 98, 92],
    [93,108,100,107,100,107,100,108, 93],
    [90,100, 99,103,104,103, 99,100, 90],
    [90, 98,101,102,103,102,101, 98, 90],
    [92, 94, 98, 95, 98, 95, 98, 94, 92],
    [90, 92, 95, 95, 92, 95, 95, 92, 90],
    [85, 90, 92, 93, 78, 93, 92, 90, 85],
    [88, 50, 90, 88, 90, 88, 90, 50, 88]
]
Ju = [
    [206,208,207,213,214,213,207,208,206],  
    [206,212,209,216,233,216,209,212,206],  
    [206,208,207,214,216,214,207,208,206],  
    [206,213,213,216,216,216,213,213,206],  
    [208,211,211,214,215,214,211,211,208],  
    [208,212,212,214,215,214,212,212,208],  
    [204,209,204,212,214,212,204,209,204],  
    [198,208,204,212,212,212,204,208,198],  
    [200,208,206,212,200,212,206,208,200],  
    [194,206,204,212,200,212,204,206,194] 
]
Pao = [
    [100,100, 96, 91, 90, 91, 96,100,100],
    [98, 98, 96, 92, 89, 92, 96, 98, 98],
    [97, 97, 96, 91, 92, 91, 96, 97, 97],
    [96, 99, 99, 98,100, 98, 99, 99, 96],
    [96, 96, 96, 96,100, 96, 96, 96, 96],
    [95, 96, 99, 96,100, 96, 99, 96, 95],
    [96, 96, 96, 96, 96, 96, 96, 96, 96],
    [97, 96,100, 99,101, 99,100, 96, 97],
    [96, 97, 98, 98, 98, 98, 98, 97, 96],
    [96, 96, 97, 99, 99, 99, 97, 96, 96],
]
def calz(tur, r):
    ret, ret2 = 0, 0
    if tur == 0:
        ret ^= turr
        ret2 ^= turr2
    for i in range(1, 11):
        for j in range(1, 10):
            if r[i][j].op == 0:
                continue
            ret ^= eva3[r[i][j].op-1][r[i][j].id][j-1+9*(i-1)]
            ret2 ^= eva3[r[i][j].op-1][r[i][j].id][j-1+9*(i-1)]
    return ret, ret2
def eval(r):
    ret = 0
    for i in range(1, 11):
        for j in range(1, 10):
            if r[i][j].op == 0:
                continue
            if r[i][j].op == 1:
                xx = 11-i
            else:
                xx = i
            yy = j
            if r[i][j].id == 1:
                tmp = Jiang[xx-1][yy-1]
            if r[i][j].id == 2 or r[i][j].id == 3:
                tmp = Shi_Xiang[xx-1][yy-1]
            if r[i][j].id == 4:
                tmp = Ma[xx-1][yy-1]  
            if r[i][j].id == 5:
                tmp = Ju[xx-1][yy-1]  
            if r[i][j].id == 6:
                tmp = Pao[xx-1][yy-1]
            if r[i][j].id == 7:
                tmp = Bing[xx-1][yy-1]
            if r[i][j].op == 2:
                ret += tmp
            else:
                ret -= tmp
    return ret
def alphabet(tur, r, lessdep, a, b):
    Mo.count += 1
    sq = init.chess(0, 0)
    if lessdep == 0:
        return eval(r)
    for i in range(1, 11):
        for j in range(1, 10):
            if r[i][j].op != tur+1:
                continue
            sp = copy.deepcopy(r[i][j])
            pos = move.check(r, i, j)
            for ii in range(1, 11):
                for jj in range(1, 10):
                    if pos[ii][jj] == 0:
                        continue
                    sq.op = r[ii][jj].op
                    sq.id = r[ii][jj].id
                    r[ii][jj].op = r[i][j].op
                    r[ii][jj].id = r[i][j].id
                    r[i][j].op = 0
                    r[i][j].id = 0
                    tmp = alphabet(1-tur, r, lessdep-1, a, b)

                    r[ii][jj].op = sq.op
                    r[ii][jj].id = sq.id
                    r[i][j].op = sp.op
                    r[i][j].id =sp.id
                    if tur == 1:
                        if tmp>a:
                            a = tmp
                            if lessdep == Mo.lim:
                                Mo.x, Mo.y, Mo.dx, Mo.dy = i, j, ii, jj
                        if b <= a:
                            return a
                    else:
                        if tmp<b:
                            b = tmp
                            if lessdep == Mo.lim:
                                Mo.x, Mo.y, Mo.dx, Mo.dy = i, j, ii, jj
                        if b <= a:
                            return b
    if tur == 1:
        return a
    else:
        return b


def alphabet2(tur, r, lessdep, a, b):
    Mo.count += 1
    fg = 0
    sq = init.chess(0, 0)
    if lessdep == 0:
        return eval(r)
    moves = []
    for i in range(1, 11):
        for j in range(1, 10):
            if r[i][j].op != tur+1:
                continue
            pos = move.check(r, i, j)
            for ii in range(1, 11):
                for jj in range(1, 10):
                    if pos[ii][jj] == 0:
                        continue
                    if tur == 1:
                        moves.append(ste(r[i][j].id, i, j, ii, jj))
                    else:
                        moves.append(ste(r[i][j].id, 11-i, j, 11-ii, jj))
    moves.sort()
    for bg in moves:
        if tur == 0:
            bg.x = 11-bg.x
            bg.dx = 11-bg.dx
        sp = copy.deepcopy(r[bg.x][bg.y])
        sq.op = r[bg.dx][bg.dy].op
        sq.id = r[bg.dx][bg.dy].id
        r[bg.dx][bg.dy].op = r[bg.x][bg.y].op
        r[bg.dx][bg.dy].id = r[bg.x][bg.y].id
        r[bg.x][bg.y].op = 0
        r[bg.x][bg.y].id = 0
        tmp = alphabet2(1-tur, r, lessdep-1, a, b)
        r[bg.x][bg.y].op = sp.op
        r[bg.x][bg.y].id = sp.id
        r[bg.dx][bg.dy].op = sq.op
        r[bg.dx][bg.dy].id = sq.id
        if tur == 1:
            if tmp > a:
                a = tmp
                rec = copy.deepcopy(bg)
                fg = 1
                if lessdep == Mo.lim:
                    Mo.x, Mo.y, Mo.dx, Mo.dy = bg.x, bg.y, bg.dx, bg.dy
            if b <= a:
                eva2[rec.p][rec.y-1+9*(rec.x-1)][rec.dy-1+9*(rec.dx-1)] += 16<<lessdep
                return a
        else:
            if tmp < b:
                b = tmp
                rec = copy.deepcopy(bg)
                fg = 1
                if lessdep == Mo.lim:
                    Mo.x, Mo.y, Mo.dx, Mo.dy = bg.x, bg.y, bg.dx, bg.dy
            if b <= a:
                rec.x = 11-rec.x
                rec.dx = 11-rec.dx
                eva2[rec.p][rec.y-1+9*(rec.x-1)][rec.dy-1+9*(rec.dx-1)] += 16<<lessdep
                return b
    if fg == 1:
        if tur == 0:
            rec.x = 11-rec.x
            rec.dx = 11-rec.dx
        eva2[rec.p][rec.y-1+9*(rec.x-1)][rec.dy-1+9*(rec.dx-1)] += 16<<lessdep
    if tur == 1:
        return a
    else:
        return b

def alphabet3(tur, r, lessdep, a, b, ha, ha2):
    Mo.count += 1
    fg = 0
    sq = init.chess(0, 0)
    if lessdep == 0:
        return eval(r)
    moves = []

    if tur == 1:
        if ht[ha].h2 == ha2 and ht[ha].re > a:
            a = ht[ha].re
    else:
        if ht[ha].h2 == ha2 and ht[ha].re < b:
            b = ht[ha].re
    for i in range(1, 11):
        for j in range(1, 10):
            if r[i][j].op != tur+1: 
                continue
            pos = move.check(r, i, j)
            for ii in range(1, 11):
                for jj in range(1, 10):
                    if pos[ii][jj] == 0:
                        continue
                    if tur == 1:
                        moves.append(ste(r[i][j].id, i, j, ii, jj))
                    else:
                        moves.append(ste(r[i][j].id, 11-i, j, 11-ii, jj))
    moves.sort()
    for bg in moves:
        if tur == 0:
            bg.x = 11-bg.x
            bg.dx = 11-bg.dx
        Ha, Ha2 = ha, ha2
        ha ^= eva3[r[bg.x][bg.y].op-1][r[bg.x][bg.y].id][bg.y-1+9*(bg.x-1)]
        ha2 ^= eva4[r[bg.x][bg.y].op-1][r[bg.x][bg.y].id][bg.y-1+9*(bg.x-1)]
        if r[bg.dx][bg.dy].op != 0:
            ha ^= eva3[r[bg.dx][bg.dy].op-1][r[bg.dx][bg.dy].id][bg.dy-1+9*(bg.dx-1)]
            ha2 ^= eva4[r[bg.dx][bg.dy].op-1][r[bg.dx][bg.dy].id][bg.dy-1+9*(bg.dx-1)]
        ha ^= eva3[r[bg.x][bg.y].op-1][r[bg.x][bg.y].id][bg.dy-1+9*(bg.dx-1)]
        ha2 ^= eva4[r[bg.x][bg.y].op-1][r[bg.x][bg.y].id][bg.dy-1+9*(bg.dx-1)]
        ha ^= turr
        ha2 ^= turr2
        sp = copy.deepcopy(r[bg.x][bg.y])
        sq.op = r[bg.dx][bg.dy].op
        sq.id = r[bg.dx][bg.dy].id
        r[bg.dx][bg.dy].op = r[bg.x][bg.y].op
        r[bg.dx][bg.dy].id = r[bg.x][bg.y].id
        r[bg.x][bg.y].op = 0
        r[bg.x][bg.y].id = 0
        tmp = alphabet3(1-tur, r, lessdep-1, a, b, ha, ha2)
        r[bg.x][bg.y].op = sp.op
        r[bg.x][bg.y].id = sp.id
        r[bg.dx][bg.dy].op = sq.op
        r[bg.dx][bg.dy].id = sq.id
        ha, ha2 = Ha, Ha2
        if tur == 1:
            if tmp > a:
                a = tmp
                rec = copy.deepcopy(bg)
                fg = 1
                if lessdep == Mo.lim:
                    Mo.x, Mo.y, Mo.dx, Mo.dy = bg.x, bg.y, bg.dx, bg.dy
            if b <= a:
                eva2[rec.p][rec.y-1+9*(rec.x-1)][rec.dy-1+9*(rec.dx-1)] += 16<<lessdep
                if ht[ha].h2 != ha2 or a > ht[ha].h2:
                    ht[ha].h2 = a
                return a
        else:
            if tmp < b:
                b = tmp
                rec = copy.deepcopy(bg)
                fg = 1
                if lessdep == Mo.lim:
                    Mo.x, Mo.y, Mo.dx, Mo.dy = bg.x, bg.y, bg.dx, bg.dy
            if b <= a:
                rec.x = 11-rec.x
                rec.dx = 11-rec.dx
                eva2[rec.p][rec.y-1+9*(rec.x-1)][rec.dy-1+9*(rec.dx-1)] += 16<<lessdep
                if ht[ha].h2 != ha2 or b < ht[ha].h2:
                    ht[ha].h2 = b
                return b
    if fg == 1:
        if tur == 0:
            rec.x = 11-rec.x
            rec.dx = 11-rec.dx
        eva2[rec.p][rec.y-1+9*(rec.x-1)][rec.dy-1+9*(rec.dx-1)] += 16<<lessdep
    if tur == 1:
        if ht[ha].h2 != ha2 or a > ht[ha].h2:
            ht[ha].h2 = a
        return a
    else:
        if ht[ha].h2 != ha2 or b < ht[ha].h2:
            ht[ha].h2 = b
        return b


def AI1(QW, tur, r):
    Mo.lim = 4
    Mo.count = 0
    tim1 = time.time()
    val = alphabet(tur, r, Mo.lim, -1000000, 1000000)
    tim2 = time.time()
    print("+-----------AI level=1-----------+")
    print("|"+("value = "+str(val)).center(32)+"|")
    print("|"+("time usage = "+str('%.2f'%(tim2-tim1))+"s").center(32)+"|")
    print("|"+("states count = "+str(Mo.count)).center(32)+"|")
    print("+--------------------------------+")
    QW.np, QW.r2 = move.mov(QW, r, Mo.x, Mo.y, Mo.dx, Mo.dy, QW.np, QW.r2)

def AI2(QW, tur, r):
    Mo.lim = 4
    Mo.count = 0
    tim1 = time.time()
    val = alphabet2(tur, r, Mo.lim, -1000000, 1000000)
    tim2 = time.time()
    print("+-----------AI level=2-----------+")
    print("|"+("value = "+str(val)).center(32)+"|")
    print("|"+("time usage = "+str('%.2f'%(tim2-tim1))+"s").center(32)+"|")
    print("|"+("states count = "+str(Mo.count)).center(32)+"|")
    print("+--------------------------------+")
    QW.np, QW.r2 = move.mov(QW, r, Mo.x, Mo.y, Mo.dx, Mo.dy, QW.np, QW.r2)

def AI3(QW, tur, r):
    Mo.lim = 4
    Mo.count = 0
    ha, ha2 = calz(tur, r)
    tim1 = time.time()
    val = alphabet3(tur, r, Mo.lim, -1000000, 1000000, ha, ha2)
    tim2 = time.time()
    print("+-----------AI level=3-----------+")
    print("|"+("value = "+str(val)).center(32)+"|")
    print("|"+("time usage = "+str('%.2f'%(tim2-tim1))+"s").center(32)+"|")
    print("|"+("states count = "+str(Mo.count)).center(32)+"|")
    print("+--------------------------------+")
    QW.np, QW.r2 = move.mov(QW, r, Mo.x, Mo.y, Mo.dx, Mo.dy, QW.np, QW.r2)

def mov2(QW, tur, r, level):
    if level == 1:
        AI1(QW, tur, r)
    if level == 2:
        AI2(QW, tur, r)
    if level == 3:
        AI3(QW, tur, r)