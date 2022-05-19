'''
Created on: 20220519

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
import math
import matplotlib.pyplot as plt
import numpy as np
p_0 = 101325
R = 8.314
F = 96485

class alkaline_ele():
    def __init__(self, T=300, p=30, A=0.37, i=1000):
        '''
        Initialize an alkaline electrolyser

        :param T: Temperature (K)
        :param p: Pressure (bar)
        :param A: Cell area (m2)
        :param i: Current density (A/m2)
        '''
        self.T = T
        self.p = p * p_0
        self.A = A
        self.i = i
        self.I = i * A # Current

    #-----------These two functions calculates the reversible voltage. You don't have to understand them--------
    def E_rev(self, p_H2O=10**(-0.645) * p_0):
        '''
        Reversible potential
        '''
        E_rev = self.E_rev_0() + R * self.T / (2 * F) * math.log((self.p - p_H2O) ** 1.5 / (p_H2O))
        return E_rev

    def E_rev_0(self):
        '''
        Standard reversible potential
        Refer to : Low-temperature electrolysis system modelling: A review
        '''
        E_0_T = 1.5184 - 1.5421e-3 * self.T + 9.523e-5 * self.T * math.log(self.T) + 9.84e-8 * self.T ** 2
        return E_0_T
    #-----------------------------------------------------------------------------------------------------------

    def E_cell_empirical(self,
                         r1=8.05e-5,  # ohm m2
                         r2=-2.5e-7,  # ohm m2/celcius
                         s=0.19,  # V
                         t1=1.002,  # A-1 m2
                         t2=8.424,  # A-1 m2 celcius
                         t3=247.3,  # A-1 m2 celcius **2
                         ):
        """
        An empirical model from Ulleberg

        :param r1: Electrolyte ohmic resistive parameter
        :param r2: Electrolyte ohmic resistive parameter
        :param s: over voltage parameter of electrode
        :param t1: empirical over voltage parameter of electrode
        :param t2: empirical over voltage parameter of electrode
        :param t3: empirical over voltage parameter of electrode
        :return: cell voltage
        """
        assert (t1 + t2 / (self.T - 273.15) + t3 / (self.T - 273.15) ** 2) * self.i + 1 > 0, \
            'The term within Log function should be positive'
        U = self.E_rev() + (r1 + r2 * (self.T - 273.15)) * self.i + s * math.log(
            (t1 + t2 / (self.T - 273.15) + t3 / (self.T - 273.15) ** 2) * self.i + 1, 10)
        return U

if __name__ == '__main__':
    # Add new methods in the alkaline_ele class that return different efficiencies or write your own codes.


    # Use the following codes to generate a picture or use others as you prefer
    x = np.linspace(1, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, label= 'sin(x)')
    plt.legend()
    plt.show()
    pass