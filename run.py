import sys
import os
import warnings

import src.models.train_model as train_model
import src.models.predict_model as predict
import src.output.output as output

import time

def main():
    model = train_model.load_model()

    decision_threshold=0.99
    for path in sys.argv[1:]:
        start = time.time()
        print(f'processing file at {path}')
        
        # create output csv filepath
        base_path = 'outputs/'
        path_components  = path.split('/')[6:10]
        subfolder_path = base_path + '/'.join(path_components[:-1])
        filename = path_components[-1] + '.csv'

        if os.path.exists(subfolder_path + '/' + filename):
            print('processing for file already completed, skipping....')
            continue

        try:
            prediction = predict.predict_from_file(model, path, decision_threshold=decision_threshold)
        except FileNotFoundError as e:
            warnings.warn('file not found. Skipping')
            continue
        except Exception as e:
            warnings.warn('Unexpected exception encountered, logging to scripts/errors and skipping file')
            logf = open(f"scripts/errors/{path_components[-1]}.log", "w")
            logf.write(str(e))
            logf.close()
            continue
        
        # some files have no sequences matching size restrictions. Skip them
        if prediction == None:
            warnings.warn('File has no valid sequences, skipping...')
            continue

        show_job_metrics(prediction, decision_threshold=decision_threshold)

        # save header, raw sequence, and prediction confidence to csv
        output.dict_to_csv(filename, subfolder_path, prediction, filtered_keys='labels')

        # show time elapsed
        end = time.time()
        print('time to process file:', end-start)

def show_job_metrics(prediction, **kwargs):
    headers = prediction['headers']

    # metrics
    num_positive = sum(prediction["labels"])

    # displaying metrics
    # print(f'headers =', headers)
    print(f'num positive for AMP = {num_positive}. Total sequences processed = {len(prediction["labels"])}')
    print(f'AMP detection rate with threshold of {kwargs["decision_threshold"]} = {num_positive/len(prediction["labels"])}')
    # print({k:v for k,v in zip(prediction['headers'], prediction['raw'])})
    # print({k:v for k,v in zip(prediction['headers'], prediction['confidence'])})


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('time to complete full batch:', end-start)