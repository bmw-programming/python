import os
class Helper:
    def __init__(self):
        pass
    def log(self,message):
        print(message)
    def filesposle25(self):
        spisocfoto = os.listdir("/home/xtrime/NewPythonBot/DB/posle25")
        elementsinarray = len(spisocfoto)
        x = 0
        var1 = []   
        while (x < elementsinarray):
            var1.append(os.path.abspath("DB/posle25//" + spisocfoto[x]))
            x = x + 1
        return var1
    def filesdo25(self):
        spisocfoto = os.listdir("/home/xtrime/NewPythonBot/DB/posle25")
        elementsinarray = len(spisocfoto)
        x = 0
        var1 = []   
        while (x < elementsinarray):
            var1.append(os.path.abspath("DB/posle25//" + spisocfoto[x]))
            x = x + 1
        return var1