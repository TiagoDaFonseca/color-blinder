from colour import colorimetry, plotting, XYZ_to_Lab, XYZ_to_sRGB, Lab_to_XYZ
import colour
import numpy as np
import math

class Diff():
    def __init__(self):
        self.dE = 0.0
        self.dL = 0.0
        self.da = 0.0
        self.db = 0.0
        self.dc = 0.0

def calc_dE (Lab1, Lab2):
    return float(colour.difference.delta_E_CMC(Lab1, Lab2))

class Color():
    def __init__(self):
        self.L = 0.0
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.h = 0.0


    def Lab2rgb (self):
        LAB = np.array([self.L,self.a,self.b])
        XYZ = colour.Lab_to_XYZ(LAB)
        RGB = colour.XYZ_to_sRGB(XYZ).tolist()
        return (RGB[0]*255,RGB[1]*255,RGB[2]*255)

    def calc_c (self):
        self.c = math.sqrt(self.a * self.a + self.b * self.b)

    def calc_h (self):
        try:
            if self.a < 0:
                self.h = math.degrees(np.arctan(self.b/self.a))+180
            else:
                if self.b < 0:
                    self.h = math.degrees(np.arctan(self.b/self.a)) + 360
                else:
                    self.h = math.degrees(np.arctan(self.b/self.a))
            #self.h = math.degrees(np.arctan(self.b / self.a))
        except ZeroDivisionError:
            print("Zero division error")

#Colorimetry
def createSPD (cdo, px):
    full_cdo = np.linspace(400, 1000, 601).tolist()
    full_sd = np.zeros(len(full_cdo)).tolist()

    data = dict(zip(cdo, px))
    sd = dict(zip(full_cdo, full_sd))

    for key1 in data:
        for key2 in sd:
            if int(key1) == int(key2):
                sd[key2] = data[key1]
    return colour.SpectralDistribution(sd)

def color_perception (sd, obs, ill):
    o = colour.STANDARD_OBSERVERS_CMFS[obs]
    l = colour.ILLUMINANTS_SDS[ill]
    return colour.sd_to_XYZ(sd, o, l)


def xyz2lab (XYZ):
    print(XYZ)
    return XYZ_to_Lab(XYZ/100)

def xyz2rgb (XYZ):
    RGB = XYZ_to_sRGB(XYZ / 100)
    print(RGB)
    return (RGB[0]*255,RGB[1]*255,RGB[2]*255)

def plot_spec (sd):
    colour.plotting.plot_single_sd(sd)

