import unittest
from FLCS_klasy_modeli import PureDiffusion_One_ComponentsWithTripletModel,mainFLCS_curve_data


class TestModels(unittest.TestCase):

    def setUp(self):
        model1 = PureDiffusion_One_ComponentsWithTripletModel(pathToFile ="Path")


    def testClass_mainFLCS_curve_data(self):
        model3 = mainFLCS_curve_data(pathToFile="path")
        assert  model3.pathToFile

    def testFile(self):
        model2 = PureDiffusion_One_ComponentsWithTripletModel(pathToFile="path")
        print model2.pathToFile
        pass






if __name__=="__main__":
  unittest.main()