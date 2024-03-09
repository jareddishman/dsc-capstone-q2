import csv
import os

def dict_to_csv(filename, subfolder_path, dictionary, filtered_keys=None):
    if filtered_keys is not None:
        keys = list(dictionary.keys())
        if type(filtered_keys) == list:
            for filt in list(filtered_keys):
                keys.remove(filt)
        else:
            keys.remove(filtered_keys)

        output_dict = {k:dictionary[k] for k in keys}
    else:
        output_dict = dictionary

    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    path = subfolder_path + '/' + filename
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(output_dict.keys())
        writer.writerows(zip(*output_dict.values()))