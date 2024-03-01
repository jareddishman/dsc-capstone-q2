import argparse
import sys

import src.features.build_datasets as build
import src.models.train_model as train_model
import src.models.predict_model as predict

test_path = "/projects/greengenes2/gg2_genomes/ncbi/GCA/018/937/935/GCA_018937935.1_PDT001069856.1/GCA_018937935.1_PDT001069856.1_protein.faa.gz"

def main():
    # parser = argparse.ArgumentParser(description='Predict whether a peptide has antimicrobial properties using a Deep Neural Network')
    # args = parse_arguments(parser)

    model = train_model.load_model()
    
    # files = sys.stdin
    # if len(files) == 0: files = test_path # temporary to just allow running the damn thing
    files = test_path

    prediction = predict.predict_from_file(model, files, decision_threshold=0.9)
    print(prediction)

# def parse_arguments(parser):
#     parser.add_argument('-f', help='Specify the file path for .faa file', nargs='+')

if __name__ == '__main__':
    main()