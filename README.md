# Network-based multi-omics integration reveals metabolic risk profile within treated HIV-infection 

## Abstract

Applying omics technologies has improved our biological understanding of pathology and systemic health status in people living with HIV on antiretroviral therapy (PLWHART). Still, a systematic and in-depth characterization metabolic risk profile during long-term successful treatment is lacking. In this study, we used multi-omics (plasma lipidomic and metabolomic, and fecal 16s microbiome) data-driven stratification and characterization to identify the metabolic risk profile within PLWHART. Through network analysis and similarity network fusion (SNF), we identified three groups of PLWHART (SNF-1 to 3). The SNF-2 (n=44; 45%) had obesity-related clinical features (increased visceral adipose tissue, BMI), higher incidence of metabolic syndrome (MetS), and increased di- and triglycerides despite having higher CD4+ T-cell counts than the other two clusters. The influence of sexual orientation in the microbiome was observed in the SNF-2 and SNF-3, with increased α-diversity compared to SNF-1. Our multi-omics integrative analysis reveals a complex microbial interplay in PLWHART. It identifies a risk cluster of PLWH who may benefit from personalized medicine and lifestyle intervention to improve their metabolic profile and enhance healthy aging. 

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
```
2) Move data files to folder data
3) Execute R notebooks for producing tables and figures
