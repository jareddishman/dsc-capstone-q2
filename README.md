dsc180a-quarter1 Group A06 Antimicrobial Peptide Project 
==============================

Quarter 1 research duplication for DSC 180A at UCSD


**INSTRUCTIONS:**

To run the model, run the run.py file.
    run.py accepts two arguments "train" and "predict"
    argument "train" will train the model
    argument "predict" will test the model, printing the accuracy and loss


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Paper that our project is replicating
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── run.py             <- Runs the project code
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── features       <- Scripts to preprocess raw data and turn them into features for modeling
        │   └── build_datasets.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py


--------

Link to dataset: https://www.dveltri.com/ascan/v2/data/AMP_Scan2_OrigPaper_Dataset.zip
Data is pre-separated in to train/validate/test splits
AMP files are positively labeled, DUMMY files are negatively labeled
