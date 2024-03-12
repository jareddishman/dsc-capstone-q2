import pandas as pd
from os.path import exists

paths_df = pd.read_csv('/home/jdishman/dsc-capstone-q2/paths/output_paths.csv')
lineages_df = pd.read_csv('/home/jdishman/dsc-capstone-q2/src/lineage_processing/relevant_lineages.csv')

# drop the entries that didn't have taxonomic data
paths = paths_df.drop([17052, 23651, 44690])['path'].to_numpy()

num_AMP = []
for path in paths:
    # TODO: change this to use open() instead of pandas. Should drastically improve runtime by not loading everything
    try:
        # df = pd.read_csv('/home/jdishman/dsc-capstone-q2/' + path)
        f = open('/home/jdishman/dsc-capstone-q2/' + path)
        count = -1 # controlling for csv header
        for line in f:
            count += 1
        f.close()
    except Exception as e:
        # raise e
        # haven't processed this file yet OR something went terribly wrong
        print(f'{path} raised error')
        num_AMP.append(None)
        continue

    num_AMP.append(count)

lineages_df['num_AMP'] = num_AMP
print(lineages_df.head(), lineages_df['num_AMP'].sum())
lineages_df.to_csv('/home/jdishman/dsc-capstone-q2/results/lineages_with_amp.csv')
