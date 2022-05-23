import time
class chess():
    def __init__(self, op: int, id: int):
        self.op = op
        self.id = id


def load(QW, filepath):
    QW.statusBar().showMessage('Loading...')
    time.sleep(0.5)
    filer = open(filepath, "r")
    da = filer.readlines()
    filer.close()
    r = [[chess(0, 0) for j in range(10)] for i in range(11)]
    r2 = [[0]*4 for i in range(500)]
    tur = (int)(da[0].split(' ')[0])
    for i in range(10):
        for j in range(9):
            r[i+1][j+1].op = (int)(da[i+1].split(' ')[2*j])
            r[i+1][j+1].id = (int)(da[i+1].split(' ')[2*j+1])
    np = (int)(da[11].split(' ')[0])
    for i in range(np):
        for j in range(4):
            r2[i][j] = (int)(da[12+i].split(' ')[j])
    return tur, r, np, r2


def save(filepath, tur, r, np, r2):
    filew = open(filepath, "w")
    filew.write(str(tur)+'\n')
    for i in range(10):
        for j in range(9):
            filew.write(str(r[i+1][j+1].op)+' '+str(r[i+1][j+1].id)+' ')
        filew.write('\n')
    filew.write(str(np)+'\n')
    for i in range(np):
        for j in range(4):
            filew.write(str(r2[i][j])+' ')
        filew.write('\n')
    filew.close()

def convert(r):
    pos = [[0]*2 for i in range(32)]
    for i in range(10):
        for j in range(9):
            if r[i+1][j+1].op == 0:
                continue
            if r[i+1][j+1].op == 2:
                temp = 16
            else:
                temp = 0
            if r[i+1][j+1].id == 1:
                pos[temp][0] = i+1
                pos[temp][1] = j+1
            else:
                tep = temp + r[i+1][j+1].id*2 - 3
                # print(r[i+1][j+1].op, r[i+1][j+1].id, tep)
                while pos[tep][0] != 0:
                    tep += 1
                # print(tep)
                pos[tep][0] = i+1
                pos[tep][1] = j+1
    return pos
