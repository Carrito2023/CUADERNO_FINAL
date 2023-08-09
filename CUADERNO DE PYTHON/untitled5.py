# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:37:48 2023

@author: Neymar
"""
 def __init__(self,v = 2):

         self.v = v

      def set(self,v = 1):

         self.v += v

          return self.v

   a = A()

   b = a

   b.set()

   print(a.v)