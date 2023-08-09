# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:41:17 2023

@author: Neymar
"""

import numpy as np



unos=np.ones((3,4))
print(unos)
ceros=np.zeros((3))
print(ceros)
aleatorio=np.random.random((2,2))
print(aleatorio)

mt1=np.full((2,2),100)
print(mt1)

mt3=np.arange(0,30,5 )
print(mt3)

import numpy as np
a=np.array([(1,2,3,4),
             (3,4,5,6)])
print(a)
print("\n"*1)    
print(a[1,2])         

import numpy as np
unos = np.zeros((8,8))
print(unos)

import numpy as np
a=np.array([(1,2,3),(3,4,5,)])
print("\n"*2)
print(np.sqrt(a))
print("\n"*2)
print(np.std(a))
print("\n"*2)
b= np.array([2,4,8])
print(b.min())
print(b.max())
print(b.sum())