1 Description:

QiimeToMaAsLin supports transforming a Qiime OTU table into the abundance section of a MaAsLin .pcl file.
The bitbucket project sfle needs to be installed to run QiimeToMaaslin as an automated project.
QiimeToMaaslin should be placed in .../sfle/input

QiimeToMaAsLin is intended to perform the following operations:
1. Combine the OTU name with the consensus lineage
2. Add all clade levels (which do not have identical abundance thier children node) and sum each clade level
3. Normalize the sample by dividing each clade/OTU by the total sum of the sample abundances at that given clade level.
4. Optionally a metadata matrix can be added to the abudnance file.


2 Supported formats from Qiime:

Several formats of Qiime Consensus lineages are supported with QiimeToMaAsLin.
Different formats are indicated by extension numbering.
Examples of test files should be provided in the downloading of QiimeToMaAsLin
Below is a key to the extensions needed for formating:
Extension	Format Example
.qiime		k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae
.qiime2		Root;k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae


3 To Run:

Place your input qiime file with a valid extension (see above) into the input folder of qiimetomaasline.
If you want to append a metadata matrix to the header of the abundance table place a file in the input directory with the same file name
as the input qiime file but with the extension ".metadata". See test1.qiime and test1.metadata in the qiimetomaaslin input directory for examples.
Move up two directory level to what should be a sfle folder.
Type scons output/qiimetomaaslin
The output should be in ...sfle/output/qiimetomaaslin


4. File formatting:

1. Please use tab delimited files.
2. qiime files should be as output from Qiime.
3. Metadata files should have samples as rows and metadata as columns.


5 Troubleshooting:

A. The following error is due to none visible foramatting in the file (in this case a txt file from Excel in the Mac Office suite).
Traceback (most recent call last):
  File "/home/ttickle/Desktop/ttickle/sfle/input/qiimetomaaslin/src/qiime2otus.py", line 86, in <module>
    for astrLine in csv.reader( open(strInputQiime), csv.excel_tab ):
_csv.Error: new-line character seen in unquoted field - do you need to open the file in universal-newline mode?

To correct:
Run the following command in a terminal to remove the nonvisible characters and use the new generated file.
strings inputfile.qiime > outputfile.qiime


B. When using the command "scons output/qiimetomaaslin/" I get the message:

ImportError: No module named sfle:
  File "/home/user/sfle/SConstruct", line 2:
    import sfle

Solution: You need to update your path. On a linux terminal in the sfle directory type the following.

export PATH=/usr/local/bin:`pwd`/src:$PATH
export PYTHONPATH=$PATH



