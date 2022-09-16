# Network-based multi-omics integration reveals metabolic risk profile within treated HIV-infection 

## Description
Multi-omics characterization of 97 people living with HIV under antiretroviral therapy (lipidomcis, metabolomics, microbiome)

## Installation

### Clone the repository
```
git clone https://github.com/neogilab/HIV_multiomics.git
cd HIV_multiomics
```
### Download data from fishare (https://figshare.com/)
1. Lipidome : [https://doi.org/10.6084/m9.figshare.21120268.v1]
2. Metabolome : [https://doi.org/10.6084/m9.figshare.21120271.v1]
3. Microbiome : [https://doi.org/10.6084/m9.figshare.21088066.v1]

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

a) Files processing
preprocessing_input_files.Rmd
microbiome_processing.Rmd


b) SNF

SNF_cross_validation.Rmd
Identify_HC_clusters_in_data.Rmd


c) Metabolome / lipidome analysis

Merge_data_cluster.Rmd
Boxplot_lipid_classes.Rmd
LIMMA_microbiome_cocomo_2_HC_HIV.Rmd
LIMMA_microbiome_cocomo_2_HC.Rmd


d) Microbiome analysis

Make_table_clinical_with_microbiome.Rmd
COCOMO_microbiome_preprocessing.Rmd
figures_microbiome_extra.Rmd
preparing_lEfSe_input.Rmd
Microbiome_DGE_family.Rmd
Boxplots_top_microbes.Rmd
Statistic_tests_microbiome.Rmd


e) Clinical

Statistics_COCOMO-microbiome_3.Rmd

f) MDM

Microbiome_derived_metabolites.Rmd
association_clinical_items_MDM.Rmd


g) MOFA
mofa_3_layers_4.Rmd
mofa_3_layers_downstream_analysis_4.Rmd
mofa_3_layers_MSEA.Rmd

h) Figures
PCA_cocomo_3_layers_2.Rmd

### Author

Flora Mikaeloff
