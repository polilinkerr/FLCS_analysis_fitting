import os


class mainFLCS_curve_data(object):

    def __init__(self,pathToFile):
        try:
            tauList, G_List = self.readFile(pathToFile)
        except:
            tauList = None
            G_List = None

        self.tau_list = tauList
        self.G_List = G_List
        self.pathToFile = pathToFile



    def readFile(self, pathToFile):
        #Funkcja czyta plik i wyrzuca zbior Tau i G
        tauList = []
        G_List = []


        return tauList,G_List




class Model1(mainFLCS_curve_data):

    def __init__(self,pathToFile):
        super(Model1,self).__init__(pathToFile)
        self.G_Fit_List = []

    """Atrybuty ktore dziedzicze
    self.tau_list
    self.G_List
    self.pathToFile

    """











