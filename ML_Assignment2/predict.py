"""Small menu program that uses the final model from each assignment notebook.

Run it from a terminal:  python predict.py
Settings match the notebooks: degree 2, K = 7, max depth 3, 25% test set, random_state 42.
"""
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier

DATA = Path(__file__).parent / "data"
WHEAT_FEATURES = ["kernel_length_mm", "groove_length_mm"]
PENGUIN_FEATURES = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]


def build_mpg_model():
    cars = pd.read_csv(DATA / "mpg.csv").dropna(subset=["horsepower"])
    X_train, X_test, y_train, y_test = train_test_split(
        cars[["horsepower"]].values, cars["mpg"].values, test_size=0.25, random_state=42)
    model = make_pipeline(PolynomialFeatures(2), LinearRegression()).fit(X_train, y_train)
    return model, model.score(X_test, y_test)


def build_wheat_model():
    wheat = pd.read_csv(DATA / "seeds.csv")
    X_train, X_test, y_train, y_test = train_test_split(
        wheat[WHEAT_FEATURES], wheat["variety"], test_size=0.25, random_state=42,
        stratify=wheat["variety"])
    model = KNeighborsClassifier(n_neighbors=7).fit(X_train, y_train)
    return model, model.score(X_test, y_test)


def build_penguin_model():
    penguins = pd.read_csv(DATA / "penguins.csv").dropna()
    X_train, X_test, y_train, y_test = train_test_split(
        penguins[PENGUIN_FEATURES], penguins["species"], test_size=0.25, random_state=42,
        stratify=penguins["species"])
    model = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
    return model, model.score(X_test, y_test)


def ask_number(prompt, low, high):
    """Keep asking until the user types a number between low and high."""
    while True:
        try:
            value = float(input(f"{prompt} ({low}-{high}): "))
        except ValueError:
            print("  Please type a number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Please stay between {low} and {high}, the range the model was trained on.")


def predict_mpg():
    model, r2 = build_mpg_model()
    hp = ask_number("Horsepower", 46, 230)
    print(f"\nPredicted fuel economy: {model.predict([[hp]])[0]:.1f} mpg")
    print(f"(Polynomial regression, degree 2, test R² = {r2:.2f})")


def predict_wheat():
    model, accuracy = build_wheat_model()
    kernel = pd.DataFrame([[
        ask_number("Kernel length in mm", 4.9, 6.7),
        ask_number("Groove length in mm", 4.5, 6.6),
    ]], columns=WHEAT_FEATURES)
    votes = [f"{round(share * 7)} {variety}"
             for variety, share in zip(model.classes_, model.predict_proba(kernel)[0]) if share > 0]
    print(f"\nPredicted variety: {model.predict(kernel)[0]}")
    print(f"Neighbour votes: {', '.join(votes)}")
    print(f"(KNN, K = 7, test accuracy = {accuracy:.1%})")


def predict_penguin():
    model, accuracy = build_penguin_model()
    penguin = pd.DataFrame([[
        ask_number("Bill length in mm", 32, 60),
        ask_number("Bill depth in mm", 13, 22),
        ask_number("Flipper length in mm", 172, 231),
        ask_number("Body mass in g", 2700, 6300),
    ]], columns=PENGUIN_FEATURES)
    print(f"\nPredicted species: {model.predict(penguin)[0]}")
    print(f"(Decision tree, max depth 3, test accuracy = {accuracy:.1%})")


def main():
    choices = {"1": predict_mpg, "2": predict_wheat, "3": predict_penguin}
    while True:
        print("\n--- ML Assignment 2 ---")
        print("1. Predict a car's fuel economy")
        print("2. Identify a wheat variety")
        print("3. Identify a penguin")
        print("4. Quit")
        choice = input("Choose 1-4: ").strip()
        if choice == "4":
            break
        if choice in choices:
            choices[choice]()
        else:
            print("Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
