"""
setup to get taxonomic classification for each species
requires generated lineages file
"""

import pandas as pd

dataset_filepath = '/home/jdishman/dsc-capstone-q2/paths/refseq_paths.csv'
lineages_filepath = '/home/jdishman/dsc-capstone-q2/src/lineage_processing/ncbi_lineages_2024-03-11.csv.gz'

data_df = pd.read_csv(dataset_filepath)
lineages_df = pd.read_csv(lineages_filepath, compression='gzip')

data_df = data_df[['organism_name', 'taxid', 'species_taxid']]
lineages_df = lineages_df[['tax_id', 'superkingdom', 'phylum', 'class', 'order', 'family', 'genus',
       'species', 'biotype']]

output_df = data_df.merge(lineages_df, how='inner', left_on='taxid', right_on='tax_id')
output_df.drop('tax_id', axis=1).to_csv('relevant_lineages.csv')