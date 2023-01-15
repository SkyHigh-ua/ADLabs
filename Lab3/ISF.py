import fileinput
import re
import os
import math

class IndexStraightFile:
    def __init__(self, filepath):
        if not os.path.exists(f"{filepath}/db"):
            os.mkdir(f"{filepath}/db")
        self.indexfilename = f"{filepath}/db/index.csv"
        self.datafilename = f"{filepath}/db/data.csv"
        self.overloadfile = f"{filepath}/db/overload.csv"
        open(self.datafilename, 'w').close()
        open(self.overloadfile, 'w').close()
        self.lenth = 1000
        self.id = 0
        self.genindex()
    
    def genindex(self):
        with open(self.indexfilename, 'w') as f:
            for _ in range(self.lenth):
                f.write("0;0\n")

    def input(self, data):
        with open(self.datafilename, 'a') as f:
            f.write(f'{self.id};0;{data}\n')
        printed = False
        for line in fileinput.input(self.indexfilename, inplace=True):
            if line[0] == '0' and not printed:
                key = fileinput.filelineno()
                print(f'{key};{self.id}')
                printed = True
            else:
                print(line, end='')
        if not printed:
            with open(self.overloadfile, 'a') as f:
                key = fileinput.filelineno()+self.id+1-fileinput.filelineno()
                f.write(f'{key};{self.id}\n')
        self.id += 1
        return key
    
    def delete(self, id):
        for line in fileinput.input(self.datafilename, inplace=True):
            data = re.findall(f'^{id};0;(.*)', line)
            if data:
                print(f'{id};1;{data[0]}')
            else:
                print(line, end='')
        matched = False
        for line in fileinput.input(self.indexfilename, inplace=True):
            if re.match(f'^[0-9]+;{id}', line):
                matched = True
                print(f'0;0')
            else:
                print(line, end='')
        if not matched:
            for line in fileinput.input(self.overloadfile, inplace=True):
                if re.match(f'^[0-9]+;{id}', line):
                    pass
                else:
                    print(line, end='')

    def edit(self, id, data):
        for line in fileinput.input(self.datafilename, inplace=True):
            if re.match(f'^{id};0;.*', line):
                print(f'{id};0;{data}')
            else:
                print(line, end='')

    def searchalgorithm(self, dct, id):
        if len(dct) == 0:
            return None
        lenth = len(dct)
        k = int(math.floor(math.log(lenth, 2)))
        i = 2**k
        if dct[i][1] == int(id):
            return dct[i][0]
        elif dct[i][1] > int(id):
            j = 1
            delta = 2**(k-j) 
            while delta > 0 and i in dct:
                if dct[i][1] == int(id):
                    return dct[i][0]
                elif dct[i][1] > int(id):
                    i = i - (int(math.floor(delta/2))+1)
                else:
                    i = i + (int(math.floor(delta/2))+1)
                j+=1
                delta = 2**(k-j)
        else:
            j = 1
            l = int(math.floor(math.log(lenth-i+1,2)))
            delta = 2**(l-j) 
            i = lenth + 1 - 2**l
            if dct[i][1] == int(id):
                return dct[i][0]
            while delta > 0 and i in dct:
                if dct[i][1] == int(id):
                    return dct[i][0]
                elif dct[i][1] > int(id):
                    i = i - (int(math.floor(delta/2))+1)
                else:
                    i = i + (int(math.floor(delta/2))+1)
                j+=1
                delta = 2**(l-j)
        if i in dct:
            if dct[i][1] == int(id):
                return dct[i][0]
        else:
            return None

    def searchinfile(self, filename, id):
        dct = {}
        i=1
        with open(filename, 'r') as f:
            for line in f:
                if len(dct) < self.lenth/10 and line != '0;0\n':
                    val, key = line.split(';')
                    dct[i] = (int(key), int(val))
                    i+=1
                else:
                    res = self.searchalgorithm(dct, id)
                    if res is not None:
                        return str(res), id
                    else:
                        dct.clear()
                        i=1
                        if line != '0;0\n':
                            val, key = line.split(';')
                            dct[i] = (int(key), int(val))
                            i+=1
        res = self.searchalgorithm(dct, id)
        if res is not None:
            return str(res), id
        return None

    def search(self, id):
        res = self.searchinfile(self.indexfilename, id)
        if res is None:
            res = self.searchinfile(self.overloadfile, id)
        if res is not None:
            with open(self.datafilename, 'r') as f:
                for line in f:
                    if re.match(f"{res[0]};0;.*", line):
                        data = line.split(';')[2].replace("\n", "")
                        return res[0], res[1], data
        else:
            return res

    def GetId(self):
        return self.id