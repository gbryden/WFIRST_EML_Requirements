#!/bin/bash

#run in a python 3 environment where doorstop has been installed
doorstop import inputs/EML_L1_reqs.csv L1
doorstop import inputs/EML_L2_reqs.csv L2
doorstop import inputs/EML_L3_reqs.csv L3

doorstop

# optionally make some Excel format spreadsheets:
#doorstop export L1 outputs/EML_L1_reqs.xlsx
#doorstop export L2 outputs/EML_L2_reqs.xlsx
#doorstop export L3 outputs/EML_L3_reqs.xlsx

doorstop publish all ./outputs

# use pandoc to create markdown-format files (in /outputs)
make -f MakefileMarkdown
# use pandoc to create microsoft docs (in /outputs)
make -f MakefileDoc

# make a graphic showing the requirements flow
python RunGraphviz.py
rm Digraph.gv
mv Digraph.gv.png WFIRST_EML_Requirements.png

#python MakeLinksGitHubFriendly.py
