#! usr/bin/env python
#! coding:utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data and cut data #
pds = pd.read_csv('../dataset/dataset_1.csv')
pdsv = pds.values
pdsv = pdsv[0:250,1]
testarray = np.random.random_sample((250,1))
# read data and cut data end #

############################ revert array ###################
#pdv = np.zeros((250,))
#pdsvc = pdsv.copy()
#for i in range(len(pdsv)):
#    pdv[i] = pdsv[250-1-i]
pdsv = pdsv[::-1]
pdsv = pdsv.reshape((250,1)).astype(np.float64)

############################# revert array end #############

####################### fft filter #######################################
#plt.subplot(121),plt.plot(pdsv,label="market",color="red",linewidth=1) 
#plt.title('origial')
#plt.xticks([]),plt.yticks([])
#plt.show()
rows = pdsv.shape[0]
mask = np.zeros(pdsv.shape,np.uint8)
mask[rows/2-20:rows/2+20] = 1

f1 = np.fft.fft2(pdsv)
f1shift = np.fft.fftshift(f1)
f1shift = f1shift * mask
f2shift = np.fft.ifftshift(f1shift)
furier = np.fft.ifft2(f2shift)
furier = np.abs(furier)
######################fft filter end ####################################

################# plot ##############################################

plt.subplot(111),plt.plot(pdsv,label="market",color="red",linewidth=1) 
plt.title('origial')
plt.subplot(111)
plt.plot(furier,color="blue",linewidth=1)
plt.xticks([]),plt.yticks([])
plt.show()
