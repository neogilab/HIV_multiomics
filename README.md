# Network-based multi-omics integration reveals metabolic risk profile within treated HIV-infection 

## Description
Multi-omics characterization of 97 people living with HIV under antiretroviral therapy (lipidomcis, metabolomics, microbiome)

## Installation

### Clone the repository
```
git clone https://github.com/neogilab/HIV_multiomics.git
cd HIV_multiomics
```
### Download data from [https://figshare.com/]
[https://doi.org/10.6084/m9.figshare.21120268.v1]
[https://doi.org/10.6084/m9.figshare.21120271.v1]
[https://doi.org/10.6084/m9.figshare.21088066.v1]

### Requirements

1. A linux distribution

2. The following python modules
```
pip3 install leidenalg
pip3 install igraph
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

2) Move data files to folder data (additional clinical parameters are in the data folder)
3) Change path to your own computer for each notebook
4) Execute R notebooks for producing tables and figures

### Author

Flora Mikaeloff
