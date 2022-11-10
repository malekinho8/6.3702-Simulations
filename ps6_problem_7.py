# -*- coding: utf-8 -*-
"""PS6-Problem-7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DGNSmseWC3Krx4i9BclPBm269Kb2q62m

# LaTEX Figure Formatting (Optional)
"""

from google.colab import output, files

! sudo apt-get install texlive-latex-recommended #1
! sudo apt-get install dvipng texlive-fonts-recommended #2
! wget http://mirrors.ctan.org/macros/latex/contrib/type1cm.zip #3
! unzip type1cm.zip -d /tmp/type1cm #4
! cd /tmp/type1cm/type1cm/ && sudo latex type1cm.ins  #5
! sudo mkdir /usr/share/texmf/tex/latex/type1cm #6
! sudo cp /tmp/type1cm/type1cm/type1cm.sty /usr/share/texmf/tex/latex/type1cm #7
! sudo texhash #8
output.clear()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib
from matplotlib import rc
import matplotlib.pyplot as plt
# %matplotlib inline

rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
!apt install texlive-fonts-recommended texlive-fonts-extra cm-super dvipng
output.clear()

"""# Import Modules"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

"""# (a) Generate 5000 samples with PDF ..."""

N = 5000
x = np.linspace(0,2,N)
px = 2/N*(x/2)
px[-1] += (1 - sum(px)) # normalization

X = np.random.choice(x,(N,),p=px)

plt.figure(1, figsize=(10,8))
plt.hist(X,bins=50)
plt.title('Histogram for part (a)')
plt.xlabel('x')
plt.ylabel('Number of Samples')
plt.show()

"""# (b) g(x)"""

def g(x):
  return 1 - sqrt(4 - x**2)/2

Y = np.array([g(x) for x in X])



plt.figure(2, figsize=(10,8))
plt.hist(Y, bins=50)
plt.show()

"""# (c) - Z_i = Y_i + W_i """

W = np.random.uniform(-1,1,(N,))

Z = W + Y

plt.figure(3,figsize=(10,8))
plt.hist(Z,bins=100)
plt.show()



"""# (d) - Calculate the correlation coefficient"""

absX = np.abs(X)
absZ = np.abs(Z)
absXZ = absX * absZ

rho = (np.mean(absXZ) - np.mean(absX)*np.mean(absZ))/sqrt((np.mean(absX**2) - np.mean(absX)**2)*(np.mean(absZ**2)-np.mean(absZ)**2))

rho