from src.features.build_datasets import vectorize
import numpy as np

def evaluate_model(model, dataset):
    # Evaluate model on provided dataset and get test accuracy
    test_accuracy = model.evaluate(dataset, batch_size=8)
    return test_accuracy

def predict_from_file(model, filepath, decision_threshold = 0.5):
    if decision_threshold > 1 or decision_threshold < 0:
        raise ValueError("threshold must be between 0 and 1")

    # vectorize sequence data from the dataset file
    vectors, headers, raw_sequences = vectorize(filepath)

    # Make predictions from model
    predictions = model.predict(vectors)

    # Convert probability predictions to binary labels (0 or 1) based given decision threshold
    labels = [True if p > decision_threshold else False for p in predictions]
    
    numpy_labels = np.array(labels)
    headers = np.array(headers)[numpy_labels]
    AMP_vectors = np.array(raw_sequences)[numpy_labels]
    confidence = np.array(predictions)[numpy_labels]

    return {'labels': labels, 'headers': headers, 'raw': AMP_vectors, 'confidence': confidence}