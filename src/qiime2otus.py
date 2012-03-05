#!/usr/bin/env python

import csv
import os
import re
import sys

c_CapMemoryUse		= 10,000 #lines of data that will be saved between sending data to the file
c_strUnclassified	= "unclassified"
c_strOTUID		= "#OTU ID"
c_cOutputOTULineageDelim = "|"
c_cOutputOTULineageDelimForRe = "\|"
c_strOutputDelimiter	="\t"

#Check for arg count
if len( sys.argv ) != 3:
	raise Exception( "Usage: qiime2otus.py <inputfile.txt> <outputfile.otu>" )
strInputQiime = sys.argv[1]
strOutputName = sys.argv[2]

print("Outputing data to the file:"+strOutputName)

#Temporarly holds lines of data to output
lstrOutputlines = []

#If output file exists, erase
if os.path.exists(strOutputName):
  os.remove(strOutputName)

#Output file handle
fhndlOutput = open(strOutputName, "a")

#Read through tab delimited qiime output
for astrLine in csv.reader( open(strInputQiime), csv.excel_tab ):
  #Get otu and data
  strOTU, astrData, strConsensusLineage = astrLine[0], astrLine[1:-1], astrLine[-1]

  #Consolidate the data
  astrData = c_strOutputDelimiter.join(astrData)

  #If the OTU id is found save, if data is found save, ignore other header elements
  if strOTU[0] == "#":
    if strOTU == c_strOTUID:
      lstrOutputlines.append(c_strOutputDelimiter.join([strOTU,astrData]))
  #If the otu name has a period in it, take everything after the period
  else:
    i = strOTU.find( "." )
    if i >= 0:
      strOTU = strOTU[( i + 1 ):]
    #Format consensus lineage
    #Remove root
#    strConsensusLineage = re.sub(r'^Root$',c_strUnclassified,strConsensusLineage)
    #Remove root #TODO is this right?
    strConsensusLineage = re.sub(r'k__',"",strConsensusLineage)
    #Change no end clade to unclassified #TODO is this right?
    strConsensusLineage = re.sub(r';.__;.__$',c_cOutputOTULineageDelim+c_strUnclassified,strConsensusLineage)
    strConsensusLineage = re.sub(r';.__$',c_cOutputOTULineageDelim+c_strUnclassified,strConsensusLineage)
    #Change out delimiters #TODO is this right?
    strConsensusLineage = re.sub(r';.__',c_cOutputOTULineageDelim,strConsensusLineage)
    #Combine with qiime consensus lineages
    strOTU = c_cOutputOTULineageDelim.join([strConsensusLineage,strOTU])
    lstrOutputlines.append(c_strOutputDelimiter.join([strOTU,astrData]))

  #If the cache of data is a certain size then output to file
  if len(lstrOutputlines)>c_CapMemoryUse:
    fhndlOutput.write("\n".join(lstrOutputlines))
    lstrOutputlines = []

#Output to file anthing not already sent to file
fhndlOutput.write("\n".join(lstrOutputlines))
fhndlOutput.close()

print("Successfully Ended Qiime2OTU")
