# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:50:21 2023

@author: Neymar
"""

def a(self):

    print("a")

def a(self):

    print("b")

    class C(B,A):

        def c(self):
            self.a()

    o = C()

    o.c()