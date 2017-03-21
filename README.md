# WFIRST Microlensing Requirements

### Inputs:

- L1 requirements
- L2 requirements and links to L1
- L3 requirements and links to L2

### Outputs:

-  [flowchart](WFIRST_EML_Requirements.png)
-  documents: L1, L2, L3 in html, markdown, docx, and xlsx format (in outputs/)

### To Update Results:

- Edit the input files (inputs/EML_L1_reqs.csv)
- Remove old/create new yml files from input csv
- Run doorstop/pandoc/graphviz

### Software Requirements

* python 3
* doorstop (Browning & Adams 2014)
  * http://dx.doi.org/10.4236/jsea.2014.73020):
  * https://doorstop.readthedocs.io/en/latest/#setup
* pandoc: http://pandoc.org/installing.html
* graphviz: https://pypi.python.org/pypi/graphviz

brew install pandoc
brew install graphviz
pip install doorstop
pip install graphviz
