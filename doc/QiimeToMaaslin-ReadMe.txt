I. Description:

QiimeToMaAsLin supports transforming a Qiime OTU table into a MaAsLin .pcl file. This script can be ran as a seperate script or as a sfle project.

If running as a sfle project, the bitbucket project sfle needs to be installed to run QiimeToMaaslin as an automated project. As well, in this case, QiimeToMaaslin should be placed in .../sfle/input. When ran as a script, the script can be placed anywhere; placing the script in your path may be optimal.

QiimeToMaAsLin is intended to perform the following operations:
1. Combine the OTU name with the consensus lineage and standardize the name.
2. Add all clade levels (which do not have identical abundance thier children node) and sum each clade level
3. Normalize the sample by dividing each clade/OTU by the total sum of the sample abundances at that given clade level.
4. Optionally a metadata matrix can be added to the abundance file.

##### Please note QiimeToMaAsLin has a dependency that will need to be installed, blist (a python library). Please visit https://pypi.python.org/pypi/blist/ for details.

II. Supported formats from Qiime:

Several formats of Qiime Consensus lineages are supported with QiimeToMaAsLin. More may be added as new standards evolve.

1. k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae
2. Root;k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae
3. k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae


III. To Run:

1. As a script
On a terminal in the directory you have the qiimeToMaaslin.py script (or anywhere if you have the script in your path) type the following
python qiimeToMaaslin.py metadatafile.metadata < inputfile.txt > outputfile.pcl

python qiimeToMaaslin.py: Calls the script
metadatafile.metadata: metadata file to combine with the Qiime file; optional and does not need to be written if not requesting this option
inputfile.txt: path location to your input file
outputfile.pcl: path location to where your output file should go


2. As a sfle project

Place your input qiime file with a valid extension (.txt or .qiime) into the input folder of qiimetomaaslin.
If you want to append a metadata matrix, place a file in the input directory with the same file name
as the input qiime file but with the extension ".metadata". See test1.qiime and test1.metadata in the qiimetomaaslin input directory for examples.
Move up two directory level to what should be a sfle folder.
Type scons output/qiimetomaaslin
The output should be in ...sfle/output/qiimetomaaslin


IV. File formatting:

1. Please use tab delimited files.
2. qiime files should be as output from Qiime.
3. Metadata files should have samples as rows and metadata as columns (see example in input file).


V. Troubleshooting:

1. When using the command "scons output/qiimetomaaslin/" I get the message:

ImportError: No module named sfle:
  File "/home/user/sfle/SConstruct", line 2:
    import sfle

Temporary Solution: You need to update your path. On a linux terminal in the sfle directory type the following.

export PATH=/usr/local/bin:`pwd`/src:$PATH
export PYTHONPATH=$PATH

Permanent Solution: In both Mac and Linux operating systems, the path can be placed in the .bash_profile or .bashrc file respectively. When doing this note that `pwd` is a command that should not be included in a permanent path definition. Instead substitute `pwd`/src with the absolute path to the sfle/src folder (can get this in the terminal by typing pwd in the sfle/src directory).
