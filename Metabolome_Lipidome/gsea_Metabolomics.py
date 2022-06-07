


import gseapy

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/3_layers_integration/results/MSEA_Metabolon/first_neibourgs_metabolites.txt",description='first_neibourgs_MDM',gene_sets="/home/flomik/Desktop/Code-PHD/3_layers_integration/processing/Metabolon_met (copy).gmt",outdir='/home/flomik/Desktop/Code-PHD/3_layers_integration/results/MSEA_Metabolon',cutoff=0.5, verbose=True, background = 879)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/3_layers_integration/results/MSEA_Metabolon/Community_4_metabolites.txt",description='Com_4_MDM',gene_sets="/home/flomik/Desktop/Code-PHD/3_layers_integration/processing/Metabolon_met (copy).gmt",outdir='/home/flomik/Desktop/Code-PHD/3_layers_integration/results/MSEA_Metabolon',cutoff=0.5, verbose=True, background = 879)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/3_layers_integration/results/MSEA_Metabolon/Community_3_metabolites.txt",description='Com_3_MDM',gene_sets="/home/flomik/Desktop/Code-PHD/3_layers_integration/processing/Metabolon_met (copy).gmt",outdir='/home/flomik/Desktop/Code-PHD/3_layers_integration/results/MSEA_Metabolon',cutoff=0.5, verbose=True, background = 879)

