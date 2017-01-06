#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import pandas as pd
import numpy as np
import sys
file1,file2=sys.argv[1:]
df1=pd.read_csv(file1,index_col=0)
df2=pd.read_csv(file2,index_col=0)
df11=df1.drop(['EMPAI','HeavySpec','LightSpec'],axis=1)
df22=df2.drop(['EMPAI','HeavySpec','LightSpec'],axis=1)
df11.rename(columns={'seq coverage':'seqcov1','seq count':'seq count1','spec count':'spec count1','NSAF':'NSAF1','Description':'Description1'},inplace=True)
df22.rename(columns={'seq coverage':'seqcov2','seq count':'seq count2','spec count':'spec count2','NSAF':'NSAF2','Description':'Description2'},inplace=True)
result=pd.concat([df11,df22],axis=1,join='outer') # axis is dataset dimension, start from 0
result1=result.fillna(0)#if not permitted, change result name
oa=result1[(result1['seqcov1']>0)&(result1['seqcov2']==0)]
ob=result1[(result1['seqcov1']==0)&(result1['seqcov2']>0)]
common=result1[(result1['seqcov1']>0)&(result1['seqcov2']>0)]
result11=pd.concat([oa,ob])
result111=pd.concat([result11,common])
result111.to_csv('E:\\python\\result\\compare2.csv')# same name is not allowed