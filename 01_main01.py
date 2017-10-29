#Test all sync and transfor file to iphone

import sys,os
sys.path.append(os.getcwd())
print(os.getcwd())
print(os.getcwd())
print('-------------------')
print('start stock analysis')
import pullDataModule
#pullDataModule.pullStockData()

import plotGraph
plotGraph.plotAllGraph()

import htLocation


