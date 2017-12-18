
import os
from SingleCurveFromFLCS import SingleCurveFLCS_TripletModelOneSpecies
from SingleCurveFromFLCS import GlobalStatisticParameters
import numpy as np
path  = os.getcwd()



def readFiles(fileName):
    pathToFIle = os.path.join(path,fileName)
    k = open(pathToFIle)
    lines = k.readlines()
    #print lines[2].split("=")[1]
    #print float(lines[2].split("=")[1].replace(" ","").replace(",","."))
    return lines
    pass


def globalStatistic(LISTA_KRZYWYCH):


    pass


def letsdoSomeWork(fileName):
    linesFormFile = readFiles(fileName)
    LISTA_KRZYWYCH = []
    if linesFormFile[7].split(" ")[0][:2] == "D1":
        """Model Triplet State bez extende , bez alfy"""
        #print "Model Triplet State bez extende , bez alfy"
        Model1 = SingleCurveFLCS_TripletModelOneSpecies(fileName,linesFormFile)


    elif linesFormFile[7].split(" ")[0][:2] == "a1":
         """Model triplet extended  z alfa"""
    else:
        pass
    try:
        return  Model1
    except:
        print "Error z plikiem ", fileName
        return None

def printStatistic(GlobalStatisticParam):
    print "D1: " , np.mean(GlobalStatisticParam.D1List), "+/-", np.std(GlobalStatisticParam.D1List), "Liczba Elementow ", len(GlobalStatisticParam.D1List)
    print "tau1: ", np.mean(GlobalStatisticParam.t1List), "+/-", np.std(
        GlobalStatisticParam.t1List), "Liczba Elementow ", len(GlobalStatisticParam.t1List)
    print "<N>: ", np.mean(GlobalStatisticParam.NList), "+/-", np.std(
        GlobalStatisticParam.NList), "Liczba Elementow ", len(GlobalStatisticParam.NList)
    print "<C>: ", np.mean(GlobalStatisticParam.CList), "+/-", np.std(
        GlobalStatisticParam.CList), "Liczba Elementow ", len(GlobalStatisticParam.CList)
    pass


def CheckIfModelIsGood(Model1):
    flag = False

    if Model1.D1 < 50. and  Model1.D1>10.:
        flag = True
    return flag
def main():
    files = [f for f in os.listdir(path) if (os.path.isfile(f) & f.endswith("dat"))]
    print "Total Files Number", len(files)
    LISTA_KRZYWYCH = []
    for f in files:
         Model1 = letsdoSomeWork(f)
         if Model1 is None: break

         CheckFlag = CheckIfModelIsGood(Model1)  ####### SPRAWDZA CZY DANA KRZYWA SIE NADAJE
         if CheckFlag:
            LISTA_KRZYWYCH.append(Model1)
            del Model1
         else:
            print Model1.fileName, "was deleted due to D1: ",Model1.D1
    """NOWY KOD"""
    #print "LiczbaOgnisk", len(LISTA_KRZYWYCH)
    print "SSS", len(LISTA_KRZYWYCH)
    #for f in LISTA_KRZYWYCH:
    #    print f.fileName, len(f.time_List)

    # ponizej podglad pojedynczych krzywych z fitami
    #for f in LISTA_KRZYWYCH:
    #    f.printCurvewithFit()

    
    GlobalStatisticParam = GlobalStatisticParameters(LISTA_KRZYWYCH)

    printStatistic(GlobalStatisticParam)
    GlobalStatisticParam.printAverageCurveWithFit()
    
    # LISTA KRZYWYCH to lista. kazdy jej element dane z jednego pliku
    # oraz element klasy SingleCurveFromFLCS

    #wexzmy sobie jedna krzywa i pobawmy sie nia

    #LISTA_KRZYWYCH[0].printCurvewithFit()


    pass

if __name__ == '__main__':
    main()
