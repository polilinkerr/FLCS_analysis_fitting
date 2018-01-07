"""
PODEJSCIE 2
INPUT: Pliki tylko po FLCS bez zadnego fitu

"""
import os
path = os.getcwd()
import numpy as np
import matplotlib.pyplot as plt

#Parametry fitowania
rangeStart = 50
rangeStep = 20
paramT = 0.5
paramTt = 0.5
paramT1 = 0.5
paramN = 0.5
n = 1


def printNormalizedAverageCurve(tau, G, GFit=None, title=None):
        plt.plot(tau,G,"b", label = "raw data")
        chisq=None
        try:
            plt.plot(tau,GFit,"r", label = "fit model")
            chisq = sum(map(lambda x,y: (x-y)**2, G, GFit))
        except ValueError:
            pass

        plt.xscale('log', nonposy='clip')

        plt.xlabel(r"$\tau$ "+  "[msec]", fontsize = 18)
        plt.ylabel(r"G($\tau$) "+title, fontsize=18)
        plt.legend(  bbox_to_anchor=(0.9, 1), fancybox=True, shadow=True)
        try:
            plt.text(1, 0.008, u'chisq = %.5f' %(chisq))
        except TypeError:
            pass
        plt.grid(True)
        plt.savefig(os.path.join(path, "AverageNormalizeFCSCurve %s.png" %(title)))
        plt.clf()

class Engine():
    """
    Input:
    1. Dwie listy G i Tau, ktore sa atrybutami w klasach poszczegolnych modeli
    2. Model - czyli rownanie ktore bedzie fitowane
    3. wartosc poczatkowa parametrow
    4. setup: czyli jak bedzie kawaleczkowac krzywa i ile iteracji zrobi
                zakres w tau gdzie beda krzywe fitowane

    OutPut:
    1. lista G_Fit
    2. wartosci parametrow fitu z bledami
    3. wartosc tesu chi kwadrat (?) - niech to bedzie wypluwane automatycznie w tej klasie
    """

    def __init__(self):
        self.listOfParametersIitials = []
        self.G_fit_List = [2,3]
        self.chiSquare = 2
        self.listofParametersFinal = [3,4]


    def wykonaj(self):
        """
        cos to bedzie...kiedys
        :return:
        """
        pass


    def referuj(self):
        self.wykonaj()
        return [self.G_fit_List,self.chiSquare,self.listofParametersFinal]




class mainFLCS_curve_data(object):

    def __init__(self,pathToFile,kappa):
       # try:
        #    tauList, G_List = self.readFile(pathToFile)
        #except:
        #    tauList = None
        #    G_List = None
        self.ModelName = "Parent Class"
        tauList, G_List = self.unPackData(pathToFile)
        self.tau_list = tauList
        self.G_List = G_List
        self.pathToFile = pathToFile
        self.kappa = kappa

       # ponizej dostaniemy z fitowania
        self.ifFitwasDone  = False
        self.G_Fit_List = []
        self.chiSquare = None
        self.listOfParameters = []


    def __str__(self):
        return self.ModelName


    def unPackData(self, pathToFile):
        linesFromFile = self.readFiles(pathToFile)
        tauList = self.parsowanieListForCurves(linesFromFile,0)
        G_List = self.parsowanieListForCurves(linesFromFile,1)
        #Funkcja czyta plik i wyrzuca zbior Tau i G
        #array =  numpy.loadtxt(pathToFile, skiprows=1, unpack=True)


        return tauList,G_List

    def parsowanieListForCurves(self, filelines,column):
        indexStart = 0
        tempList = []
        for line in filelines[indexStart+1:]:
            values = line.split()
            try:
                tempList.append(float(values[column].replace(",",".")))
            except IndexError:
                tempList.append(np.nan)
        return tempList

    def readFiles(self, fileName):
        pathToFIle = os.path.join(path,fileName)
        k = open(pathToFIle)
        lines = k.readlines()
        #print lines[2].split("=")[1]
        #print float(lines[2].split("=")[1].replace(" ","").replace(",","."))
        return lines

    def przyjmijWynikFita(self,tableOfResultsFromEngineClass):
        if wynikFitowania[0] and wynikFitowania[1] and wynikFitowania[2]:
            print "KB LOG: OprzyjmijWynikFita OK"
            self.G_Fit_List = tableOfResultsFromEngineClass[0]
            self.chiSquare = tableOfResultsFromEngineClass[1]
            self.listOfParameters = tableOfResultsFromEngineClass[2]
            self.ifFitwasDone = True
        else:
            print "KB LOG: PrzyjmijWyikFita FALSE"

class PureDiffusion_One_ComponentsWithTripletModel(mainFLCS_curve_data):

    def __init__(self,pathToFile,kappa):
        """Atrybuty ktore dziedzicze
        self.tau_list
        self.G_List
        self.pathToFile
        """
        self.ModelName = "Pure Diffusion One Componets Triplet"
        mainFLCS_curve_data.__init__(self,pathToFile,kappa=kappa)
        #super(Model1,self).__init__(pathToFile)
        self.ModelName = "Pure Diffusion One Componets Triplet"

    def funkcja(self, x, T, Tt, T1, N):
        y=(1-T+T*np.exp(-x/Tt))*(1.0/(N*(1-T)))*((1+x/T1)**(-1))*(1+x/(T1*self.kappa**2))**(-0.5) #postac funkcji fitowanej
        return y



class PureDiffusion_Two_ComponentsWithTripletModel(mainFLCS_curve_data):
    def __init__(self,pathToFile,kappa):
        """Atrybuty ktore dziedzicze
        self.tau_list
        self.G_List
        self.pathToFile
        """
        self.ModelName = "Pure Diffusion Two Componets Triplet"
        mainFLCS_curve_data.__init__(self,pathToFile,kappa=kappa)
        #super(Model1,self).__init__(pathToFile)

    def funkcja(self):
        """
        :return: Tu trzeba wpisac cialo funkcji
        """
        return None


class PureDiffusion_Three_ComponentsWithTripletModel(mainFLCS_curve_data):
    def __init__(self,pathToFile,kappa):
        """Atrybuty ktore dziedzicze
        self.tau_list
        self.G_List
        self.pathToFile
        """
        self.ModelName = "Pure Diffusion Three Componets Triplet"
        mainFLCS_curve_data.__init__(self,pathToFile,kappa=kappa)
        #super(Model1,self).__init__(pathToFile)


    def funkcja(self):
        """Tu trzeba wpisac cialo funkcji"""
        return None

class AnomalousDiffusion_One_ComponentsWithTripletModel(mainFLCS_curve_data):

    def __init__(self,pathToFile,kappa):
        """Atrybuty ktore dziedzicze
        self.tau_list
        self.G_List
        self.pathToFile
        """
        self.ModelName = "Anomalous Diffusion One Componets Triplet"
        mainFLCS_curve_data.__init__(self,pathToFile,kappa=kappa)
        #super(Model1,self).__init__(pathToFile)


    def funkcja(self):
        """Tu trzeba wpisac cialo funkcji"""
        return None


class AnomalousDiffusion_Two_ComponentsWithTripletModel(mainFLCS_curve_data):
    def __init__(self,pathToFile,kappa):
        """Atrybuty ktore dziedzicze
        self.tau_list
        self.G_List
        self.pathToFile
        """
        self.ModelName = "Anomalous Diffusion Two Componets Triplet"
        mainFLCS_curve_data.__init__(self,pathToFile,kappa=kappa)
        #super(Model1,self).__init__(pathToFile)


    def funkcja(self):
        """Tu trzeba wpisac cialo funkcji"""
        return None

class AnomalousDiffusion_Three_ComponentsWithTripletModel(mainFLCS_curve_data):
    def __init__(self,pathToFile,kappa):
        """Atrybuty ktore dziedzicze
        self.tau_list
        self.G_List
        self.pathToFile
        """
        self.ModelName = "Anomalous Diffusion Three Componets Triplet"
        mainFLCS_curve_data.__init__(self,pathToFile,kappa=kappa)
        #super(Model1,self).__init__(pathToFile)


    def funkcja(self):
        """Tu trzeba wpisac cialo funkcji"""
        return None

if __name__ == '__main__':
    files = [f for f in os.listdir(path) if (os.path.isfile(f) & f.endswith("dat"))]
    print "Total Files Number", len(files)
    LISTA_KRZYWYCH = []
    for f in files:
        Obiekt = PureDiffusion_One_ComponentsWithTripletModel(os.path.join(path, f), kappa=3.474)
        print Obiekt.G_List
        print Obiekt
        printNormalizedAverageCurve(Obiekt.tau_list,Obiekt.G_List,None,"STARWARS")


        wynikFitowania = Engine().referuj() # [G_fit_List,  chiSquare,  listOfParametersIitials]
        Obiekt.przyjmijWynikFita(wynikFitowania)


    GlobalListOfCurves = [] #lista obiektow ktore beda robione w petli for wczesniej

    




