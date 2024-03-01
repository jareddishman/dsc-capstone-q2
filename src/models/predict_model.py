from src.features.build_datasets import vectorize

def evaluate_model(model, dataset):
    # Evaluate model on provided dataset and get test accuracy
    test_accuracy = model.evaluate(dataset, batch_size=8)
    return test_accuracy

def predict_from_file(model, filepath, decision_threshold = 0.5):
    if decision_threshold > 1 or decision_threshold < 0:
        raise ValueError("threshold must be between 0 and 1")

    # vectorize sequence data from the dataset file
    vectors = vectorize(filepath)

    # Make predictions from model
    predictions = model.predict(vectors)

    # Convert probability predictions to binary labels (0 or 1) based on a threshold of 0.5
    return [1 if p > decision_threshold else 0 for p in predictions]
