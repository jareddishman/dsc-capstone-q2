import argparse

import src.features.build_datasets as build
import src.models.train_model as train_model
import src.models.predict_model as predict

def main():
    model = train_model.load_model()
    prediction = predict.predict_from_file(model, "/projects/greengenes2/gg2_genomes/ncbi/GCA/018/937/935/GCA_018937935.1_PDT001069856.1/GCA_018937935.1_PDT001069856.1_protein.faa.gz")
    print(prediction)


if __name__ == '__main__':
    main()