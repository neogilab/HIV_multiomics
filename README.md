# Network-based multi-omics integration reveals metabolic risk profile within treated HIV-infection 

## Description
Multi-omics characterization of 97 people living with HIV under antiretroviral therapy (lipidomcis, metabolomics, microbiome)

## Installation

### Clone the repository
```
git clone https://github.com/neogilab/HIV_multiomics.git
cd HIV_multiomics
```

### Requirements

1. A linux distribution

2. The following python packages

```
pip3 install -r requirements.txt
# This command will install the following modules:
# igraph==0.8.2
# leidendag==0.8.0
```
3. R and R studio environment and following packages
Open R and run
```
# install and load  the package  manager
 if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
    
 bio_pkgs <- c("ComplexHeatmap", "ggalluvial", "ggplot2", "MOFA2", 
          "phyloseq", "vegan", "limma", "SNFtool")

# install:
BiocManager::install(bio_pkgs)
```

4. Cytoscape software version 3.6.1
[https://github.com/cytoscape/cytoscape/releases/3.6.1/]

### Run code

1) Create folders
```
Rscript create_folders.R
```

2) Move data files to folder data
3) Change path to your own computer
4) Execute R notebooks for producing tables and figures
```
Rscript -e src/1_SNF/SNF_cross_validation.Rmd
```
### Author

Flora Mikaeloff
