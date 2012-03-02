#!/usr/bin/env python

import csv
import sys

c_strOTUID		= "#OTU ID"
c_cOutputOTULineageDelim = "|"
c_strOutputDelimiter	="\t"

#Check for arg count
if len( sys.argv ) != 3:
	raise Exception( "Usage: abnd2pcl.py <inputfile.abnd> <outputfile.pcl>" )
strInputAbnd = sys.argv[1]
strOutputName = sys.argv[2]

print("Outputing data to the file:"+strOutputName)

#Temporarly holds lines of data to output
lstrOutputlines = []

#Holds the taxa abundance for all samples
aadData = []
astrIDs = adSums = None

#Read through tab delimited qiime output
for astrLine in csv.reader( open(strInputAbnd), csv.excel_tab ):
  #Get otu and data per sample
  strOTU, astrData = astrLine[0], astrLine[1:len(astrLine)]

  #If the OTU id is found save, if data is found save, ignore other header elements
  if strOTU[0] == "#":
    if strOTU == c_strOTUID:
      lstrOutputlines.append(c_strOutputDelimiter.join([strOTU]+astrData))
      astrIDs = []
      adSums = [0] * len( astrData )
  #If sample line has already been found, we assume we are now working with data
  elif(adSums):
    astrData = [strCur.strip( ) for strCur in astrData]
    aadData.append( adData )
    #Add to sum of data
    for i in range( len( adData ) ):
      if adData[i]:
        adSums[i] += adData[i]

#Output file handle
fhndlOutput = open(strOutputName, "w")

#Normalize each taxa per sample sum
for iRow in range( len( astrIDs ) ):
  adData = aadData[iRow]
  for iCol in range( len( adSums ) ):
    if adData[iCol]:
      adData[iCol] /= adSums[iCol]
      lstrOutputlines.append("\t".join( [astrIDs[iRow]] + [( "" if ( d == None ) else str(d) ) for d in adData] ) )

#Output to file anthing not already sent to file
fhndlOutput.write("\n".join(lstrOutputlines))
fhndlOutput.close()

print("Successfully Ended Abnd2pcl")
