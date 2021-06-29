#!/usr/bin/env python
# coding: utf-8


##===================  HELPER TO PROCESS STOCK DATA ===================##
##
##  Author: Oleg Y. Zakharov, 2021
##
##  GNU GENERAL PUBLIC LICENSE: https://www.gnu.org/licenses/gpl-3.0.txt
##
##
##
##
##
##
##

import yfinance as yf

import pandas as pd
import numpy as np

import io
import inspect
import datetime

from dateutil.relativedelta import relativedelta
from decimal import Decimal
import matplotlib.pyplot as plt 
from matplotlib import cm
import itertools    


## ---------------------------------------------------------------------------------------------------------- ##
## ---------- GET HISTORY OF STOKS, RETURN ARRAY OF DATAFRAMES ------------------- ##
##
def getListOfStocksByDates_(lst_ticker, dt_start, dt_end):
    
    arrDataFrame = []
    for idx in range(0, len(lst_ticker)):
        newtime_daily = yf.download(lst_ticker[idx], start = dt_start, end = dt_end)
        ## convert to a dataframe
        dfHist_stock = pd.DataFrame(newtime_daily)
        dfHist_stock['Ticker'] = lst_ticker[idx]
        arrDataFrame.append(dfHist_stock)

    return arrDataFrame
    
## ---------------------------------------------------------------------------------------------------------- ##
## --------- BUILD CROSS CORRELATION MATRIX, RETURN DATAFRAME ------------------ ##
##
def buildStockCorrelationMatrix_(df, lstCorrName):
    
    arrDfCorrelation = []
    
    for idx in range(0, len(lstCorrName)):
        mask = (df['Ticker'] == lstCorrName[idx])
        arrDfCorrelation.append( df.loc[mask].copy().reset_index() )
    
    ## Prepare dataframe for correlation statistics
    dfStockCorrelation = pd.DataFrame(lstCorrName, columns=['ticker'])
     ## Build a correlation matrix
    for idx_1 in range(0, len(lstCorrName)):   
        colNameCorr = 'Corr_' + lstCorrName[idx_1]    
        for idx_2 in range(0, len(lstCorrName)):
            c= arrDfCorrelation[idx_1]['Close'].corr(arrDfCorrelation[idx_2]['Close'])
        
            dfStockCorrelation.loc[idx_2, colNameCorr] = c #.round(2)
    
    return dfStockCorrelation

