# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 07:15:49 2020

Rotina para ler as imagens e transformar em gif
@author: asgun
"""


import imageio as io
import os



dirPath = 'C:\\Analytics\\Conway\\'

with io.get_writer('conway01.gif', mode='I', duration=0.05) as writer:
    for filename in os.listdir(dirPath):
        image = io.imread(dirPath + filename)
        writer.append_data(image)
writer.close()