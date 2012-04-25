import os
import sfle
import sys

Import( "*" )

#Extensions
c_strSufPCL		= ".pcl"
c_strSufR		= ".R"
c_strSufQiime		= ".qiime"
c_strSufOTU		= ".otu"
c_strSufMetadata	= ".metadata"

#Delims
cPathDelim = "/"
cExtDelim = "."

#Scripts
#Renames the otus with the ancestry so that clades can be later summed.
progRenameOTUs = sfle.d( fileDirSrc, "qiime2otus.py")
progSumAndNormalize = sfle.d( fileDirSrc, "merge_metadata.py" )

pE = DefaultEnvironment( )

#Read in all input files in the input directory
lFileInputFiles = Glob( sfle.d( fileDirInput, "*" ) )

#Make sure they are qiime files
lQiimeFiles = []
for fileName in lFileInputFiles:
  strPathPieces = [filter(None,strPathPiece) for strPathPiece in (fileName.get_abspath().split(cExtDelim))]
  sExtension = cExtDelim+strPathPieces[-1]
  if sExtension[0:len(c_strSufQiime)] == c_strSufQiime:
    if(not "~" in sExtension):
      lQiimeFiles.append(fileName)

#Call program with an input and output file parameter
def funcFormat( target, source, env ):
  strT, astrSs = sfle.ts( target, source )
  strProg, strInputFile = astrSs[0], astrSs[1]
  return sfle.ex([strProg, strInputFile, strT])

def funcSumNormalize( target, source, env ):
  print("funcSumNormalize")
  strT, astrSs = sfle.ts( target, source )
  strProg, strInputFile = astrSs[0], astrSs[1]
  return sfle.ex([strProg, "-m","0.0","-t","-1","-i", strInputFile, ">", strT])

def funcSumNormalizeAndAddMetada( target, source, env ):
  print("funcSumNormalizeAndAddMetadata")
  strT, astrSs = sfle.ts( target, source )
  strProg, strInputFile, strMetadataFile = astrSs[0], astrSs[1], astrSs[2]
  return sfle.ex([strProg, "-m","0.0","-t","-1","-i", strInputFile, strMetadataFile, ">", strT])

#Put this into a pipeline
#For each file, merge otu column (0) with qiime output ancestral lineage column (-1)
for fileQiime in lQiimeFiles:
  strPathPieces = [filter(None,strPathPiece) for strPathPiece in (fileQiime.get_abspath().split(cExtDelim))]
  strInputBase = cExtDelim.join(strPathPieces[0:-1])
  strOutputBase = sfle.d(fileDirOutput,[filter(None,strOutputPiece) for strOutputPiece in strInputBase.split(cPathDelim)][-1])
  strUpdateNameOutputFile = File(strOutputBase+c_strSufOTU)
  strNormalizeOuputFile = File(strOutputBase+c_strSufPCL)
  strPotentialMetadataFile = strInputBase+c_strSufMetadata

  #Merge the first and last column of Qiime output to have a full name with consensus lineage
  Command( strUpdateNameOutputFile, [progRenameOTUs,fileQiime], funcFormat )

  if(os.path.isfile(strPotentialMetadataFile)):
    #Sum clades, normalize, and add metadata (normalize accounting accounting for heirarchical structure given)
    Default( Command( strNormalizeOuputFile, [progSumAndNormalize,strUpdateNameOutputFile, File(strPotentialMetadataFile)], funcSumNormalizeAndAddMetada ) )
  else:
    #Sum clades and normalize (normalize accounting accounting for heirarchical structure given)
    Default( Command( strNormalizeOuputFile, [progSumAndNormalize,strUpdateNameOutputFile], funcSumNormalize ) )
