import argparse
import sys

import src.features.build_datasets as build
import src.models.train_model as train_model
import src.models.predict_model as predict

import time
import numpy as np

test_path = "/projects/greengenes2/gg2_genomes/ncbi/GCA/018/937/935/GCA_018937935.1_PDT001069856.1/GCA_018937935.1_PDT001069856.1_protein.faa.gz"
# test_path = "/projects/greengenes2/gg2_genomes/ncbi/GCF/002/967/575/GCF_002967575.1_BS951/GCF_002967575.1_BS951_protein.faa.gz"

def main():
    # parser = argparse.ArgumentParser(description='Predict whether a peptide has antimicrobial properties using a Deep Neural Network')
    # args = parse_arguments(parser)

    model = train_model.load_model()

    # files = sys.stdin
    # if len(files) == 0: files = test_path # temporary to just allow running the damn thing
    files = test_path


    decision_threshold=0.99
    prediction = predict.predict_from_file(model, files, decision_threshold=decision_threshold)
    # headers = prediction['headers']

    show_metrics(prediction, decision_threshold=decision_threshold)

def show_metrics(prediction, **kwargs):
    headers = prediction['headers']

    # metrics
    num_positive = sum(prediction["labels"])

    # displaying metrics
    # print(f'headers =', headers)
    print(f'num positive for AMP = {num_positive}. Total sequences processed = {len(prediction["labels"])}')
    print(f'AMP detection rate with threshold of {kwargs["decision_threshold"]} = {num_positive/len(prediction["labels"])}')
    # print({k:v for k,v in zip(prediction['headers'], prediction['raw'])})
    print({k:v for k,v in zip(prediction['headers'], prediction['confidence'])})
    

def write_output(prediction):
    ...


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('time to completion:', end-start)