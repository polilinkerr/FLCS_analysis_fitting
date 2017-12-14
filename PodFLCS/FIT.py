import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class FIT:

    def __init__(self, X, Y, initT=0.5, initTt=0.5, initT1=0.5, initN=0.5):
            self.X=np.array(X)  #ixy
            self.Y=np.array(Y)  #igreki eksperymentalne
            self.initials=[float(initT), float(initTt), float(initT1), float(initN)]     #parametry poczatkowe
            self.fitY=None                                   #igreki dopasowanej funkcji
            self.T=None                                      # dopasowane parametry
            self.Tt=None
            self.T1=None
            self.N=None
            self.errT=None                                   #bledy dopasowanych parametrow
            self.errTt=None
            self.errT1=None
            self.errN=None


    def funkcja(self, x, T, Tt, T1, N):
        y=(1-T+T*np.exp(-x/Tt))*(1.0/(N*(1-T)))*((1+x/T1)**(-1))*(1+x/(T1*3.474**2))**(-0.5) #postac funkcji fitowanej
        return y

    def fitowanie(self):
        try:
            fit= curve_fit(self.funkcja,self.X,self.Y,self.initials)             #tu fituje
        except ValueError:
            print "fitowanie nie powiodlo sie. sprawdz czy X i Y sa rowej dlugosci"
            return 1
        try:
            perr=np.sqrt(np.diag(fit[1]))   #tu wyznacza bledy standardowe z macierzy kowarjancji (nieskonczona gdy fitowanie padnie 
        except ValueError:
            print "fitowanie nie powiodlo sie"
            return 1
        self.T=fit[0][0]
        self.Tt=fit[0][1]
        self.T1=fit[0][2]
        self.N=fit[0][3]
        self.errT=perr[0]
        self.errTt=perr[1]
        self.errT1=perr[2]
        self.errN=perr[3]
        self.fitY=[self.funkcja(x,self.T, self.Tt, self.T1, self.N) for x in X] #wyznacza igreki dopasowania
        return 0

    def referuj(self):
        return[[self.T,self.Tt,self.T1, self.N],[self.errT, self.errTt, self.errT1, self.N],self.fitY]

    def wykonaj(self):
        self.fitowanie()
        return self.referuj() #zwraca liste list [[T,Tt,T1,N],[errT,errTt,errT1,errN],[igreki fitu]]
        


if __name__ == '__main__':
    
####### test
    
    X=  [ 0.0103994, 0.0103994, 0.0119993, 0.0131993, 0.0147992, 0.0163991, 0.017999, 0.0195989, 0.0211988, 0.0227987, 0.0243986, 0.0267985, 0.0299983, 0.0331981, 0.0363979, 0.0395978, 0.0427976, 0.0459974, 0.0491972, 0.0539969, 0.0603966, 0.0667962, 0.0731959, 0.0795955, 0.0859951, 0.0923948, 0.0987944, 0.1083939, 0.1211931, 0.1339924, 0.1467917, 0.159591, 0.1723903, 0.1851895, 0.1979888, 0.2171877, 0.2427863, 0.2683848, 0.2939834, 0.3195819,
         0.3451805, 0.370779, 0.3963776, 0.4347754, 0.4859725, 0.5371696, 0.5883667, 0.6395639, 0.690761, 0.741958, 0.7931551, 0.8699508, 0.9723451, 1.0747392, 1.1771334, 1.2795277, 1.3819219, 1.4843161, 1.5867103, 1.7403016, 1.9450901, 2.1498785, 2.3546669, 2.5594554, 2.7642436, 2.969032, 3.1738205, 3.4810033, 3.8905799, 4.3001571, 4.709734, 5.1193104, 5.5288873, 5.9384642, 6.3480411, 6.9624062,
         7.7815599, 8.6007137, 9.4198675, 10.2390213, 11.0581751, 11.8773289, 12.6964817, 13.9252129, 15.5635204, 17.201828, 18.8401356, 20.4784431, 22.1167488, 23.7550564, 25.393364, 27.8508263, 31.1274395, 34.4040565, 37.6806679, 40.957283, 44.2338982, 47.5105133, 50.7871284, 55.7020493, 62.2552795, 68.8085098, 75.3617401, 81.9149704, 88.4682007, 95.021431]
    Y =  [0.0035, 0.0037, 0.0006, 0.0034, -0.0016, 0.0004, 0.0033, 0.0025, 0.0101, 0.002, 0.0, 0.0054, 0.0021, 0.0046, 0.0032, 0.0067, 0.005, 0.0034, 0.0079, 0.0039, 0.0026, 0.002, 0.0068, 0.0052, 0.0031, 0.0036, 0.0068, 0.0006, 0.0018, 0.0027, 0.0038, 0.0038, 0.0045, 0.0005, 0.0024, 0.0051, 0.0033, 0.0027, 0.0009, 0.0024, 0.0014, -0.0004, 0.002, 0.0012, 0.0025, 0.0007, 0.0017, 0.002, 0.0011, 0.0018, 0.0014, 0.0009, 0.001, 0.001, 0.001, 0.0007, 0.0005, 0.0002, 0.0017, 0.0008, 0.0008, 0.0001, 0.0002, -0.0003, 0.0009, 0.0006, 0.0002, 0.0006, 0.0002, 0.0002, 0.0004, 0.0004, 0.0001, 0.0, 0.0001, 0.0, 0.0001, 0.0001, 0.0001, 0.0, 0.0, 0.0, -0.0002, 0.0, -0.0001, -0.0004, -0.0003, -0.0005, -0.0003, -0.0003, -0.0004, -0.0002, -0.0003, -0.0005, -0.0006, -0.0006, -0.0007, -0.0007, -0.0007, -0.0007, -0.0005, -0.0007, -0.0009, -0.0007, -0.0009, -0.0007]

    F=FIT(X,Y).wykonaj()
    
    print "T: ", F[0][0], " +/- ", F[1][0]
    print "Tt: ", F[0][1], " +/- ", F[1][1]
    print "T1: ", F[0][2], " +/- ", F[1][2]
    print "N: ", F[0][3], " +/- ", F[1][3]
    print ""
    print "x", "y", "fit_y"
    for i in range(len(X)):
        print X[i], Y[i],F[2][i]
    
    
