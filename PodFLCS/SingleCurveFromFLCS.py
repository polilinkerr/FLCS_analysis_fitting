import matplotlib
import matplotlib.pyplot as plt
import os

path = os.getcwd()

class SingleCurveFromFLCS(object):


    def __init__(self,name,filelines):
        self.fileName = name
        self.VEff = self.parsowanieParametrowFitu("VEff[fl]",filelines)
        self.Z0 =  self.parsowanieParametrowFitu("z0",filelines)
        self.W0 = self.parsowanieParametrowFitu("w0", filelines)
        self.r1 = self.parsowanieParametrowFitu("r1", filelines)
        self.t1 = self.parsowanieParametrowFitu("t1", filelines)
        self.D1 = self.parsowanieParametrowFitu("D1", filelines)
        self.N = self.parsowanieParametrowFitu("N", filelines)
        self.C = self.parsowanieParametrowFitu("<C>", filelines)
        self.kappa = self.parsowanieParametrowFitu("k=", filelines)
        self.T = self.parsowanieParametrowFitu("T =", filelines)
        self.tT = self.parsowanieParametrowFitu("tT[ms]", filelines)


        self.time_List = self.parsowanieListForCurves(filelines,0)
        self.Ex_Corr_List = self.parsowanieListForCurves(filelines,1)
        self.Fit_Corr_List = self.parsowanieListForCurves(filelines,2)
        self.Residuals_List = self.parsowanieListForCurves(filelines,3)

    def parsowanieParametrowFitu(self, key, linesFromFile):
        for i in linesFromFile:
            if key in i.split(" ")[0]:

                value = i.split(" = ")[1].replace(" ","").replace(",",".")


                if "+-" in value:
                    value = value.split("+-")[0]

                break
        try:
            return float(value)
        except:
            return None


    def odKtorejLinijkiSaDane(self,filelines):
        pattern = None
        for i in filelines:
            if "Ex. Corr. Fit Corr. Resid" in i:
                pattern = i
                break
        try:
            indexStart = filelines.index(pattern)
        except:
            print "KB Error"
        return indexStart

    def parsowanieListForCurves(self, filelines,column):
        indexStart = self.odKtorejLinijkiSaDane(filelines)
        tempList = []
        for line in filelines[indexStart+1:]:
            values = line.split()
            try:
                tempList.append(float(values[column].replace(",",".")))
            except IndexError:
                tempList.append(0)
        return tempList

    def printCurvewithFit(self):
        tau = self.time_List
        G = self.Ex_Corr_List
        GFit = self.Fit_Corr_List
        title = self.fileName

        plt.plot(tau,G,"b", label = "raw data")
        plt.plot(tau,GFit,"r", label = "fit model")
        plt.xscale('log', nonposy='clip')

        plt.xlabel(r"$\tau$ "+  u"[\u00B5sec]", fontsize = 18)
        plt.ylabel(r"G($\tau$) "+title, fontsize=18)
        plt.legend(  bbox_to_anchor=(0.8, 1), fancybox=True, shadow=True)

        plt.grid(True)
        plt.savefig(os.path.join(path, "AverageNormalizeFCSCurve %s.png" %(title)))
        matplotlib.pyplot.clf()



class SingleCurveFLCS_TripletModelOneSpecies(SingleCurveFromFLCS):

    def __init__(self,nameFile,lines):

        super(SingleCurveFLCS_TripletModelOneSpecies,self).__init__(nameFile,lines)





class GlobalStatisticParameters():

    def __init__(self, ListaKrzywych):
        self.VEffList =  []
        self.Z0List = []
        self.W0List = []
        self.r1List = []
        self.t1List = []
        self.D1List = []
        self.NList = []
        self.CList = []
        self.kappaList = []
        self.TList = []
        self.tTList = []
        self.Obliczenia(ListaKrzywych)

        self.time_List_Global = []
        self.Ex_Corr_List_Global = []
        self.Fit_Corr_List_Global = []
        self.Residuals_List_Global = []
        self.Obliczanie2(ListaKrzywych)

    def Obliczenia(self, ListaKrzywych):
        for krzywa in ListaKrzywych:
            self.VEffList.append(krzywa.VEff)
            self.Z0List.append(krzywa.Z0)
            self.W0List.append(krzywa.W0)
            self.r1List.append(krzywa.r1)
            self.t1List.append(krzywa.t1)
            self.D1List.append(krzywa.D1)
            self.NList.append(krzywa.N)
            self.CList.append(krzywa.C)
            self.kappaList.append(krzywa.C)
            self.TList.append(krzywa.T)
            self.tTList.append(krzywa.tT)

        pass

    def Obliczanie2(self, ListaKrzywych):
        for krzywa in ListaKrzywych:
            self.time_List_Global.append(krzywa.time_List)
            self.Ex_Corr_List_Global.append(krzywa.Ex_Corr_List)
            self.Fit_Corr_List_Global.append(krzywa.Fit_Corr_List)
            self.Residuals_List_Global.append(krzywa.Residuals_List)
        pass