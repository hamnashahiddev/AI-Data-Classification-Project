"""
DecodeLabs - Project 2: Data Classification Using AI
------------------------------------------------------
Goal: Build a basic classification model using a small dataset (the Iris
benchmark), following the IPO (Input -> Process -> Output) framework
taught in the deck.

Key Requirements met:
  1. Load and understand a dataset        -> load_iris() + a quick summary
  2. Split data into training/testing     -> train_test_split (80/20, shuffled)
  3. Apply a simple classification algo   -> K-Nearest Neighbors (KNN)

Key Skills demonstrated:
  Data handling, supervised learning basics, model training,
  feature scaling, and output validation (confusion matrix + F1 score
  instead of relying on the "accuracy mirage").
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score,
)


# ------------------------------------------------------------------
# PHASE 1 (INPUT): Load and understand the dataset
# ------------------------------------------------------------------
def load_and_inspect_data():
    """Load the Iris benchmark and print a quick summary (samples, classes)."""
    iris = load_iris()
    X, y = iris.data, iris.target

    print("=" * 55)
    print(" RAW MATERIAL: The Iris Benchmark")
    print("=" * 55)
    print(f"Samples:    {X.shape[0]} (balanced)")
    print(f"Features:   {X.shape[1]} -> {iris.feature_names}")
    print(f"Classes:    {len(iris.target_names)} -> {list(iris.target_names)}")
    print()

    return X, y, iris.target_names


# ------------------------------------------------------------------
# PHASE 2 (PROCESS): Split, scale, and train
# ------------------------------------------------------------------
def build_pipeline(X, y, k=5, test_size=0.2, random_state=42):
    """Split into train/test, scale features, and fit a KNN classifier."""

    # STRUCTURAL INTEGRITY: shuffle + split (80% train / 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=True, stratify=y
    )

    # THE GATEKEEPER RULE: scale features so no single dimension dominates
    # distance calculations (mean = 0, variance = 1)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)  # transform only, never re-fit on test data

    # THE ALGORITHM: K-Nearest Neighbors (the "proximity principle")
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    return model, X_test_scaled, y_test


# ------------------------------------------------------------------
# PHASE 3 (OUTPUT): Predict and validate — beyond just "accuracy"
# ------------------------------------------------------------------
def evaluate_model(model, X_test, y_test, target_names):
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="macro")
    cm = confusion_matrix(y_test, predictions)

    print("=" * 55)
    print(" OUTPUT VALIDATION")
    print("=" * 55)
    print(f"Accuracy: {accuracy:.2%}")
    print(f"F1 Score (macro): {f1:.3f}   <- the trustworthy metric")
    print()
    print("Confusion Matrix (rows = actual, cols = predicted):")
    print(cm)
    print()
    print("Full classification report:")
    print(classification_report(y_test, predictions, target_names=target_names))

    return accuracy, f1, cm


# ------------------------------------------------------------------
# BONUS: try a small range of K values to find the "elbow"
# ------------------------------------------------------------------
def find_best_k(X, y, k_range=range(1, 16)):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True, stratify=y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("=" * 55)
    print(" TUNING THE ENGINE: Choosing K")
    print("=" * 55)
    best_k, best_acc = None, 0.0
    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, y_train)
        acc = accuracy_score(y_test, model.predict(X_test_scaled))
        print(f"  k={k:>2}  ->  accuracy={acc:.2%}")
        if acc > best_acc:
            best_k, best_acc = k, acc

    print(f"\nBest K found: {best_k} (accuracy={best_acc:.2%})\n")
    return best_k


# ------------------------------------------------------------------
# MAIN: run the full pipeline
# ------------------------------------------------------------------
if __name__ == "__main__":
    X, y, target_names = load_and_inspect_data()

    best_k = find_best_k(X, y)

    model, X_test, y_test = build_pipeline(X, y, k=best_k)
    evaluate_model(model, X_test, y_test, target_names)

    # Predict a brand-new, unseen flower measurement
    print("=" * 55)
    print(" LIVE PREDICTION: A new, unseen sample")
    print("=" * 55)
    new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])  # sepal_len, sepal_wid, petal_len, petal_wid
    scaler = StandardScaler().fit(X)  # simple demo scaler on full data
    prediction = model.predict(scaler.transform(new_flower))
    print(f"Input measurements: {new_flower.tolist()[0]}")
    print(f"Predicted species: {target_names[prediction[0]]}")