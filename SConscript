import os
import sfle
import sys

Import( "*" )
pE = DefaultEnvironment( )

#Extensions
c_strSufPCL		= ".pcl"
c_strSufMetadata	= ".metadata"

# Extensions supported
lsExtensions = [".txt",".qiime",".qiime2"]

#Scripts
#Renames the otus with the ancestry so that clades can be later summed.
progQTM = File(sfle.d( fileDirSrc, "qiimeToMaaslin.py"))

#Read in all input files in the input directory
#Make sure they are qiime files and not temp files
lFileInputFiles = Glob( sfle.d( fileDirInput, "*" ) )
lQiimeFiles = []
for fileName in lFileInputFiles:
  sFilePath, sExtension = os.path.splitext(fileName.get_abspath())
  if sExtension.lower() in lsExtensions:
    if(not sFilePath[0] in ["."]):
      lQiimeFiles.append(fileName)

#Work on each Qiime output file and potentially add to metadata file if it exists
for fileQiime in lQiimeFiles:

  strOutput = sfle.d(fileDirOutput, sfle.rebase(fileQiime, os.path.splitext(fileQiime.get_abspath())[1], c_strSufPCL))
  strMetadata = sfle.d(fileDirInput, sfle.rebase(fileQiime, os.path.splitext(fileQiime.get_abspath())[1], c_strSufMetadata))

  if(os.path.isfile(strMetadata)):
    print "qiimeToMaaslin.py is converting QiimeFile: "+ strOutput +" combined with  Metadata file: "+ strMetadata
    sfle.spipe(pE, fileQiime, progQTM, File(strOutput), [File(strMetadata).get_abspath()])
  else:
    print "qiimeToMaaslin.py is converting QiimeFile: "+ strOutput
    sfle.spipe(pE, fileQiime, progQTM, File(strOutput))