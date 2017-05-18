#This file runs a spread of simulations over a variety of SD2 conditions
#python SD2ConditionSpread.py binary directory regionfile
from __future__ import print_function

from pylab import *
from sys import *
from UCNToolsLib import *



#Temporary Variables
binary = "./a.out"
directory = "./"
Regionfile = "Regionfile"


#files
#Regionfile = argv[3]

#parameters to vary over
meanfreepaths = ["0.01","0.02","0.03","0.04"]
lifetimes = ["50.00","25.00","16.66","12.50"]

#Other parameters
sd2layers = [1]
DET = [2,1]
totalout = [[],[],[],[]]
count = 1

for i in range(0,len(meanfreepaths)):
    for j in range(0,len(lifetimes)): #Loop over parameter space
    
        print("Run {:d} of {:d}.".format(count,len(meanfreepaths)*len(lifetimes)))
        count += 1
    
        output = zeros(len(DET)+1)

        #change regionfile
        editRegion(Regionfile,sd2layers,'Scat',meanfreepaths[i])
        editRegion(Regionfile,sd2layers,'Absorb',lifetimes[j])

        #run simulation
        for ij in range(0,5):
            tempoutput = simRun(binary,directory,DET)
            for ijk in range(0,len(output)):
                output[ijk] += tempoutput[ijk]
        for ijkl in range(0,len(output)):
            output[ijkl] = output[ijkl]/5.

        totalout[i].append(output)

for d in range(0,len(DET)+1):
    print("\n\n")
    for i in range(0,len(meanfreepaths)):
        print("")
        for j in range(0,len(lifetimes)): #construct output
            print(totalout[i][j][d],end=",")
print("\n")


#Change regionfile back
editRegion(Regionfile,sd2layers,'Scat',"0.04")
editRegion(Regionfile,sd2layers,'Absorb',"25.0")

