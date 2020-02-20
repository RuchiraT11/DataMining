import random
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
import numpy as np
from numpy import mean
from numpy import std
from scipy import stats
import statistics
# CODE STARTS HERE: appending contents of file 2 to file 1
# Read the contents of file two:dist1_500_2.txt of 1st distribution set
print("Preparing first dataset...")
dist1_2= open(r"E:\Distribution Sets\dist1_500_2.txt","r")
distdata1_2=dist1_2.read()
dist1_2.close()
# # # Open 1st distribution set:dist1_500_1.txt and write the contents of dist1_500_2.txt to it
dist1_1= open(r"E:\Distribution Sets\dist1_500_1.txt","a")
dist1_1.write(distdata1_2)
print("First Data set ready!")
dist1_1.close()
# # # Read the contents of file two:dist1_500_2.txt of 1st distribution set
print("Preparing second dataset...")
dist2_2= open(r"E:\Distribution Sets\dist2_500_2.txt","r")
distdata2_2=dist2_2.read()
dist2_2.close()
# # # Open 1st distribution set:dist2_500_1.txt and write the contents of dist2_500_2.txt to it
dist2_1= open(r"Distribution Sets\dist2_500_1.txt","a")  
dist2_1.write(distdata2_2)
print("Second Data set ready!")
dist2_1.close()
# # CODE ENDS HERE
# # SELECT 10 RANDOM SAMPLES FROM THE DATASET 1 AND DATASET 2 AND EXPORT THEM TO THE EXCEL SHEET

SampleData= r"E:\Distribution Sets\SampleData.xlsx"
SampleData2= r"E:Distribution Sets\SampleData2.xlsx"
# #Selecting 10 random samples from dataset 1  ***WITHOUT MEAN***
inputdataset1= r"E:\Distribution Sets\dist1_500_1.txt" 
print("Now selecting 10 random data samples from dataset 1...")  
df=pd.read_csv(inputdataset1, index_col= False, sep=' ', skip_blank_lines= True, skipinitialspace=True).dropna(axis=0, how='any').sample(n=10)
print("samples selected... now exporting them to excel...")
df.to_excel(SampleData, 'Sheet1', index=False, startrow=0, startcol=0,header=False)
print("Successfully selected and exported 10 data samples from dataset 1")
# GRAPHICAL REPRESENTATION OF DATASET 1 TO DETERMINE THE DISTRIBUTION TYPE
print("Plotting graph to determine the distribution type..")
plt.hist(df)    #histogram of the dataset
plt.show()
plt.savefig("Dataset1 Final Graph.png")
print("graph plotted successfully...")
print("Distribution Parameters for Dataset 1 samples are:\n")

# # #Calculate min and max value of each data samples
for i in range(10):
   min_v= min(df.iloc[i])
   max_v= max(df.iloc[i])
   print("Sample ",i,": Min is ",min_v,"| Max is ", max_v)


#Selecting 10 random samples from dataset 2 ***WITHOUT MEAN*** 
inputdataset2= r"E:\Distribution Sets\dist2_500_1.txt" 
print("Now selecting 10 random data samples from dataset 2...")  
df2=pd.read_csv(inputdataset2, index_col= False, sep=' ', skip_blank_lines= True, skipinitialspace=True).dropna(axis=0, how='any').sample(n=10)
print("samples selected... now exporting them to excel...")

df2.to_excel(SampleData2, 'Sheet1', index=False, startrow=0, startcol=0,header=False)
print("Successfully selected and exported 10 data samples from dataset 2")
# CODE SUCCESSFULLY EXECUTED TILL HERE ON 05-10-2019 AT 22.06PM
#Calculate mean, median, mode and standard deviation of each data samples
print("Distribution Parameters for Dataset 2 samples are:\n")
for i in range(10):
   mean= np.mean(df2.iloc[i])
   median= np.median(df2.iloc[i])
   mode= stats.mode(df2.iloc[i])
   stdeviation= statistics.stdev(df2.iloc[i])
   print("Sample ",i,": Mean is ",mean,"| Median is ", median, "| Mode is ", mode, "| Standard deviation is ", stdeviation)
# # GRAPHICAL REPRESENTATION OF DATASET 2 TO DETERMINE THE DISTRIBUTION TYPE
plt.hist(df2)
plt.show()
plt.savefig("Dataset2 Final Graph.png")
##Plotted and calculated the distribution parameters for DataSet 2

