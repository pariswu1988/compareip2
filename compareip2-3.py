#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import pandas as pd
import numpy as np
import sys
file1,file2,file3=sys.argv[1:]
df1=pd.read_csv(file1,index_col=0)
df2=pd.read_csv(file2,index_col=0)
df3=pd.read_csv(file3,index_col=0)
df11=df1.drop(['EMPAI','HeavySpec','LightSpec'],axis=1)
df22=df2.drop(['EMPAI','HeavySpec','LightSpec'],axis=1)
df33=df3.drop(['EMPAI','HeavySpec','LightSpec'],axis=1)
df11.rename(columns={'seq coverage':'seqcov1','seq count':'seq count1','spec count':'spec count1','NSAF':'NSAF1','Description':'Description1'},inplace=True)
df22.rename(columns={'seq coverage':'seqcov2','seq count':'seq count2','spec count':'spec count2','NSAF':'NSAF2','Description':'Description2'},inplace=True)
df33.rename(columns={'seq coverage':'seqcov3','seq count':'seq count3','spec count':'spec count3','NSAF':'NSAF3','description':'Description3'},inplace=True)
result=pd.concat([df11,df22,df33],axis=2,join='outer') # axis is dataset dimension, start from 0
resultnew=result.fillna(0)#if not permitted, change result name
only1=resultnew[(resultnew['seqcov1']>0)&(resultnew['seqcov2']==0)&(resultnew['seqcov3']==0)]
only2=resultnew[(resultnew['seqcov1']==0)&(resultnew['seqcov2']>0)&(resultnew['seqcov3']==0)]
only3=resultnew[(resultnew['seqcov1']==0)&(resultnew['seqcov2']==0)&(resultnew['seqcov3']>0)]
common12=resultnew[(resultnew['seqcov1']>0)&(resultnew['seqcov2']>0)&(resultnew['seqcov3']==0)]
common13=resultnew[(resultnew['seqcov1']>0)&(resultnew['seqcov3']>0)&(resultnew['seqcov2']==0)]
common23=resultnew[(resultnew['seqcov2']>0)&(resultnew['seqcov3']>0)&(resultnew['seqcov1']==0)]
common=resultnew[(resultnew['seqcov1']>0)&(resultnew['seqcov2']>0)&(resultnew['seqcov3']>0)]
result1=pd.concat([only1,only2,only3,common12])
result2=pd.concat([common13,common23,common])
result3=pd.concat([result1,result2])
result3.to_csv('E:\\python\\result\\compare3.csv')# same name is not allowed