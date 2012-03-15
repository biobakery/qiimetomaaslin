QiimeToMaAsLin supports transforming a Qiime OTU table into the abundance section of a MaAsLin .pcl file.
To use MaAsLin one would still need to add metadata to the .pcl file.
The bitbucket project sfle needs to be installed to run QiimeToMaaslin as a automated project.
QiimeToMaaslin should be placed in .../sfle/input

QiimeToMaAsLin is intended to perform the following operations:
1. Combine the OTU name with the consensus lineage
2. Add all clade levels and sum each clade level
3. Normalize the sample by dividing each clade/OTU by the total sum of the sample abundances.

Several formats of Qiime Consensus lineages are supported with QiimeToMaAsLin.
Different formats are indicated by extension numbering.
Below is a key to the extensions needed for formating:
Extension	Format Example
.qiime		k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae
.qiime2		Root;k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae

To Run:
Place your input file with a valid extension (see above) into the input folder of qiimetomaasline.
Move up two directory level to what should be a sfle folder.
Type scons output/qiimetomaasline
The output should be in ...sfle/output/qiimetomaaslin
