# ML Assignment 2: Polynomial Regression, KNN and Decision Trees

This assignment applies three machine learning algorithms to real datasets. Each algorithm has a notebook and a short explanation video.

| Group | Algorithm | Dataset | Question | Final model | Test result |
|---|---|---|---|---|---|
| A | Polynomial regression | Auto MPG (cars from 1970–1982) | Predict fuel economy (mpg) from horsepower | Degree 2 | R² ≈ 0.66 |
| B | K-Nearest Neighbours | Seeds (210 wheat kernels, 3 varieties) | Identify the variety from kernel length and groove length | K = 7 | 94.3% (50/53) |
| C | Decision tree | Palmer Penguins (333 penguins, 3 species) | Identify the species from bill length, bill depth, flipper length and body mass | Max depth 3 | 95% (80/84) |

## Project structure

```
Assignmeng2-MachineLearning/
├── ML_Assignment2/                              # Assignment work
│   ├── A_PolynomialRegression_CarMPG_Simple.ipynb   # Group A notebook (used in the video)
│   ├── A_PolynomialRegression_CarMPG.ipynb          # Group A, longer version
│   ├── B_KNN_WheatSeeds_Simple.ipynb                # Group B notebook (used in the video)
│   ├── B_KNN_Iris_Simple.ipynb                      # Group B, alternative dataset
│   ├── B_KNN_BreastCancer.ipynb                     # Group B, alternative dataset
│   ├── C_DecisionTree_Penguins_Simple.ipynb         # Group C notebook (used in the video)
│   ├── C_DecisionTree_Penguins.ipynb                # Group C, longer version
│   ├── predict.py                                   # Menu program that uses all three final models
│   └── data/                                        # mpg.csv, seeds.csv, penguins.csv
├── LAB/                                         # Course lab notebooks (see "Labs" below)
└── VIDEO_SCRIPTS.md                             # Video scripts and cue cards
```

The three `_Simple` notebooks are the main submission. The video scripts are based on them.

## Labs

The [LAB/](LAB/) folder holds the course lab notebooks. They cover the techniques the assignment builds on.

**Python and statistics basics**

| Notebook | Topic |
|---|---|
| `1_Python101.ipynb` | Python basics |
| `1a_PandasTutorial.ipynb` | Introduction to pandas (uses `PastHires.csv`) |
| `2_MeanMedianMode (1).ipynb` | Mean, median, mode and NumPy |
| `2_PolynomialRegression (2).ipynb` | Polynomial regression |
| `3_MeanMedianExercise (1).ipynb` | Exercise: mean and median customer spend |
| `4_StdDevVariance (1).ipynb` | Standard deviation and variance |
| `5_Percentiles.ipynb` | Percentiles |
| `6_ConditionalProbabilityExercise.ipynb` | Conditional probability |

**A. Regression and supervised learning**

| Notebook | Topic |
|---|---|
| `A.1_LinearRegression (1).ipynb` | Linear regression |
| `A.2_PolynomialRegression (2) (1).ipynb` | Polynomial regression (related to assignment Group A) |
| `A.3_MultipleRegression.ipynb` | Multiple regression (uses `cars.xls`) |
| `A.3_MultivariateRegression.ipynb` | Multivariate regression (uses `cars.xls`) |
| `A.4_TrainTest Supervised Unsupervised.ipynb` | Train/test split, supervised and unsupervised learning |
| `A.5_NaiveBayes.ipynb` | Naive Bayes |

**B. Classification, clustering and model evaluation**

| Notebook | Topic |
|---|---|
| `B.1_KMeans (4).ipynb` | K-Means clustering |
| `B.2_DecisionTree.ipynb` | Decision trees (uses `PastHires.csv`; related to assignment Group C) |
| `B.2_Support Vectors.ipynb` | Support vector machines |
| `B.3_KNN (2).ipynb` | K-Nearest Neighbours (related to assignment Group B) |
| `B.4_PCA (4).ipynb` | Principal component analysis (Iris) |
| `B.5_KFoldCrossValidation.ipynb` | K-fold cross-validation (Iris) |

**Data files:** `PastHires.csv`, `cars.xls`, `access_log.txt` and `emails.zip`. The last two are large, and `.gitignore` leaves them out of the repository.

**Running the labs:** the labs were written for Google Colab. Some upload their data with `files.upload()`, and `B.3_KNN` reads the MovieLens `u.data` file from Google Drive. To run them locally, change those cells to read the files directly, for example `pd.read_csv("PastHires.csv")`.

## Setup

You need Python 3.10 or later.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## Running

**Notebooks:** open a notebook in VS Code or Jupyter and choose **Run All**. The data is read from `ML_Assignment2/data/`.

**Prediction program:**

```bash
cd ML_Assignment2
python predict.py
```

The program shows a menu with these options:

1. Predict a car's fuel economy from its horsepower.
2. Identify a wheat variety from two kernel measurements. It also shows the neighbours' votes.
3. Identify a penguin species from four measurements.

The models use the same settings as the notebooks: a 25% test set, `random_state=42`, degree 2, K = 7 and max depth 3. The program only accepts values inside the range of the training data.

## Videos

Each video is under 2 minutes and explains one algorithm using its notebook. [VIDEO_SCRIPTS.md](VIDEO_SCRIPTS.md) has the full script and a cue card for each video.

## Datasets

- **Auto MPG:** UCI Machine Learning Repository.
- **Seeds:** UCI Machine Learning Repository.
- **Palmer Penguins:** Gorman, Williams and Fraser (2014), Palmer Station LTER, Antarctica.
