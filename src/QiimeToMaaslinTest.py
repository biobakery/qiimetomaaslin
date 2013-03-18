"""
Author: Timothy Tickle
Description: Class to test the RunMicroPITA class
"""

__author__ = "Timothy Tickle"
__copyright__ = "Copyright 2011"
__credits__ = ["Timothy Tickle"]
__license__ = ""
__version__ = ""
__maintainer__ = "Timothy Tickle"
__email__ = "ttickle@sph.harvard.edu"
__status__ = "Development"

#Import libraries
from qiimeToMaaslin import *
from subprocess import call
import csv
import unittest

class QiimeToMaaslinTest(unittest.TestCase):

    strTestDir = "test"
    strTempDir = os.path.join(strTestDir,"temp")
    strInputDir = os.path.join(strTestDir,"input")
    strAnswerDir = os.path.join(strTestDir,"answer")
    strMetadataFile = os.path.join(strInputDir,"test1.metadata")

#####Test qiimeFormat1
    def testqiimeFormat1ForGoodCase(self):
        
        #Inputs
        strInput = "k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae"

        #Correct Answer
        strAnswer = "k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae"

        #Call method
        strResult = qiimeFormat1(strInput)

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

#####Test qiimeFormat2
    def testqiimeFormat2ForGoodCase(self):
        
        #Inputs
        strInput = "Root;k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae"

        #Correct Answer
        strAnswer = "k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae"

        #Call method
        strResult = qiimeFormat2(strInput)

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

#####Test qiimeFormat3
    def testqiimeFormat3ForGoodCase(self):
        
        #Inputs
        strInput = "k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__; g__Aquabacterium"

        #Correct Answer
        strAnswer = "k__Bacteria|p__Proteobacteria|c__Betaproteobacteria|o__Burkholderiales|f__unclassified|g__Aquabacterium"

        #Call method
        strResult = qiimeFormat3(strInput)

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testqiimeFormat3ForGoodCase2(self):
        
        #Inputs
        strInput = "k__Bacteria; p__Tenericutes; c__Mollicutes; o__RF39"

        #Correct Answer
        strAnswer = "k__Bacteria|p__Tenericutes|c__Mollicutes|o__RF39"

        #Call method
        strResult = qiimeFormat3(strInput)

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

#####Test funcDetectFormat
    def testFuncDetectFormatFormat1(self):

        #Inputs
        strInput = "k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae"

        #Correct Answer
        strAnswer = "qiimeFormat1"

        #Call method
        strResult = funcDetectFormat(strInput).__name__

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testFuncDetectFormatFormat2(self):

        #Inputs
        strInput = "Root;k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae"

        #Correct Answer
        strAnswer = "qiimeFormat2"

        #Call method
        strResult = funcDetectFormat(strInput).__name__

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testFuncDetectFormatFormat3(self):

        #Inputs
        strInput = "k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__; g__Aquabacterium"

        #Correct Answer
        strAnswer = "qiimeFormat3"

        #Call method
        strResult = funcDetectFormat(strInput).__name__

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testFuncDetectFormatFormat3b(self):

        #Inputs
        strInput = "k__Bacteria; p__Tenericutes; c__Mollicutes; o__RF39"

        #Correct Answer
        strAnswer = "qiimeFormat3"

        #Call method
        strResult = funcDetectFormat(strInput).__name__

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testFuncDetectFormatFormatGeneric(self):

        #Inputs
        strInput = "k__Bacteria"

        #Correct Answer
        strAnswer = "funcPass"

        #Call method
        strResult = funcDetectFormat(strInput).__name__

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testFuncDetectFormatFormatError(self):

        #Inputs
        strInput = "ERROR"

        #Correct Answer
        strAnswer = "funcPass"

        #Call method
        strResult = funcDetectFormat(strInput).__name__

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

#####Test funcFormatInput
    def testFuncFormatInputFormat1(self):

        #Input file
        strInputFile = os.path.join(self.strInputDir,"test1.txt")

        #Answer
        llsAnswer = [["#OTU ID","E2005150","E2005180.1","E2005180.2","E2005250.1","E2005250.2","E2005260.1","E2005260.2","E2005450","E2005460","E2006140.1"],
                ["k__Bacteria|p__Tenericutes|c__Mollicutes|o__RF39|f__unclassified|g__unclassified|1","0","0","0","0","0","0","0","0","1","0"],
                ["k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae|1000","5","0","0","0","0","0","0","0","0","0"],
                ["k__Bacteria|p__Bacteroidetes|c__Bacteroidia|o__Bacteroidales|f__Bacteroidaceae|g__Bacteroides|1008","86","132","15","0","0","0","0","70","6","0"],
                ["k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae|g__unclassified|101","0","0","0","0","0","4","0","0","0","0"],
                ["k__Bacteria|p__Bacteroidetes|c__Bacteroidia|o__Bacteroidales|f__Prevotellaceae|g__Prevotella|1010","0","2","0","0","1","0","0","0","0","0"],
                ["k__Bacteria|p__Bacteroidetes|c__Bacteroidia|o__Bacteroidales|f__Prevotellaceae|g__Prevotella|1013","0","0","1","0","0","2","0","0","0","0"],
                ["k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae|g__Ruminococcus|1023","4","0","0","0","0","0","1","1","0","0"],
                ["k__Bacteria|p__Tenericutes|c__Erysipelotrichi|o__Erysipelotrichales|f__Erysipelotrichaceae|g__Clostridium|1026","0","0","0","0","0","0","2","5","0","6"],
                ["k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae|1029","0","0","0","0","0","0","0","0","2","0"],
                ["k__Bacteria|p__Firmicutes|c__Clostridia|o__unclassified|f__Lachnospiraceae|1034","1","0","0","0","0","0","0","0","1","0"],
                ["k__unclassified|1035","0","5","0","5","5","0","5","0","0","0"]]
        strAnswer = ",".join([",".join(lsData) for lsData in llsAnswer])

        #Result
        llsLines = funcFormatInput(csv.reader(open(strInputFile, 'rU'), csv.excel_tab))
        strResult = ",".join([",".join(lsData) for lsData in llsLines])

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

#####Test qiimetomaaslin
    def testQiimeToMaaslinForFormat1(self):

        #Inputs
        strInputFile = os.path.join(self.strInputDir,"test1.txt")

        #Result file
        strResultFile = os.path.join(self.strTempDir,"test1-test.txt")

        #AnswerFile
        strAnswerFile = os.path.join(self.strAnswerDir,"test1-test.txt")

        #Call qiimeToMaaslin
        call(["python","qiimeToMaaslin.py",self.strMetadataFile],stdin=open(strInputFile, 'rU'),stdout=open(strResultFile, 'w'))

        #Read both answer and generated file
        strAnswer = ",".join([",".join(lsLine) for lsLine in csv.reader(open(strResultFile, 'rU'))])
        strResult = ",".join([",".join(lsLine) for lsLine in csv.reader(open(strAnswerFile, 'rU'))])

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testQiimeToMaaslinForFormat2(self):

        #Inputs
        strInputFile = os.path.join(self.strInputDir,"test2.txt")

        #Result file
        strResultFile = os.path.join(self.strTempDir,"test2-test.txt")

        #AnswerFile
        strAnswerFile = os.path.join(self.strAnswerDir,"test2-test.txt")

        #Call qiimeToMaaslin
        call(["python","qiimeToMaaslin.py",self.strMetadataFile],stdin=open(strInputFile, 'rU'),stdout=open(strResultFile, 'w'))

        #Read both answer and generated file
        strAnswer = ",".join([",".join(lsLine) for lsLine in csv.reader(open(strResultFile, 'rU'))])
        strResult = ",".join([",".join(lsLine) for lsLine in csv.reader(open(strAnswerFile, 'rU'))])

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

    def testQiimeToMaaslinForFormat3(self):

        #Inputs
        strInputFile = os.path.join(self.strInputDir,"test3.txt")

        #Result file
        strResultFile = os.path.join(self.strTempDir,"test3-test.txt")

        #AnswerFile
        strAnswerFile = os.path.join(self.strAnswerDir,"test3-test.txt")

        #Call qiimeToMaaslin
        call(["python","qiimeToMaaslin.py",self.strMetadataFile],stdin=open(strInputFile, 'rU'),stdout=open(strResultFile, 'w'))

        #Read both answer and generated file
        strAnswer = ",".join([",".join(lsLine) for lsLine in csv.reader(open(strResultFile, 'rU'))])
        strResult = ",".join([",".join(lsLine) for lsLine in csv.reader(open(strAnswerFile, 'rU'))])

        #Check result against answer
        self.assertEqual(strResult,strAnswer,"".join([str(self),"::Expected=",strAnswer,". Received=",strResult,"."]))

##
#Creates a suite of tests
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(QiimeToMaaslinTest)
    return suite
