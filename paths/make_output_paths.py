import pandas as pd

paths = pd.read_csv('/home/jdishman/dsc-capstone-q2/paths/refseq_paths.csv')

def transform_path(dataset_path):
    base_path = 'outputs/'
    output_path  = dataset_path.split('/')[6:10]
    output_path = base_path + '/'.join(output_path) + '.csv'
    return output_path

out_df = paths[['organism_name','taxid','species_taxid']]
out_df['path'] = paths['ftp_path'].apply(transform_path)
out_df.to_csv('/home/jdishman/dsc-capstone-q2/paths/output_paths.csv')
    