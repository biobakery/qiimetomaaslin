#!/usr/bin/env python

import csv
import numpy as np
import os
import sys



c_strOTUID		= "#OTU ID"
c_cOutputOTULineageDelim = "|"
c_strOutputDelimiter	="\t"


def addVectors(liAVector,liBVector):
  if len(liAVector)==len(liBVector):
    liRet = []
    for iindex in xrange(0,len(liAVector)):
      liRet.append(liAVector[iindex] + liBVector[iindex])
    return liRet
  else:
    return False

#Check for arg count
if len( sys.argv ) != 3:
	raise Exception( "Usage: otus2abnd.py <inputfile.otu> <outputfile.abnd>" )
strInputOTU = sys.argv[1]
strOutputName = sys.argv[2]

print("Outputing data to the file:"+strOutputName)

#Temporarly holds lines of data to output
lstrOutputlines = []

#Output file handle
fhndlOutput = open(strOutputName, "w")

dictClades = dict()

#Read through tab delimited qiime output
for astrLine in csv.reader( open(strInputOTU), csv.excel_tab ):
  #Get otu and data per sample
  strOTU, astrData = astrLine[0], astrLine[1:len(astrLine)]
  print("astrData")
  print(astrLine)
  print(astrData)
  #If the OTU id is found save, if data is found save, ignore other header elements
  if strOTU[0] == "#":
    if strOTU == c_strOTUID:
      lstrOutputlines.append(c_strOutputDelimiter.join([strOTU]+astrData))
  #If break the otu into lineage clades and sum per clade per sample.
  else:
    #Convert from string to float
    astrData = [float(aData) for aData in astrData]

    astrLineage = filter(None,strOTU.split(c_cOutputOTULineageDelim))
    strLineageBase = astrLineage[0]
    #Perform for first otu
    if not strLineageBase in dictClades:
      dictClades[strLineageBase] = astrData
    else:
      dictClades[strLineageBase] = addVectors(astrData, dictClades[strLineageBase])
    #Perform for all otus
    for strLineage in astrLineage[1:len(astrLineage)]:
      strLineageBase = c_cOutputOTULineageDelim.join([strLineageBase,strLineage])
      if not strLineageBase in dictClades:
        dictClades[strLineageBase] = astrData
      else:
        dictClades[strLineageBase] = addVectors(astrData, dictClades[strLineageBase])

#Pull out data from dict to outputLines for writing to file
for strClade in dictClades:
  astrCurrentClade = [str(afloat) for afloat in dictClades[strClade]]
  lstrOutputlines.append(c_strOutputDelimiter.join([strClade]+astrCurrentClade))

#Output to file anthing not already sent to file
fhndlOutput.write("\n".join(lstrOutputlines))
fhndlOutput.close()

print("Successfully Completed otus2abnd")
