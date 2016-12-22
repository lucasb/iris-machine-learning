#!/usr/bin/env python

from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
import validate_dataset as validate

# models structure
models = [
    ('LR',   'Logistic Regression',                 LogisticRegression()),
    ('LDA',  'Linear Discriminant Analysis',        LinearDiscriminantAnalysis()),
    ('KNN',  'K-Nearest Neighbors',                 KNeighborsClassifier()),
    ('CART', 'Classification and Regression Tree',  DecisionTreeClassifier()),
    ('NB',   'Gaussian Naive Bayes',                GaussianNB()),
    ('SVM',  'Support Vector Machines',             SVC()),
]

# number of splits dataset and times to evaluated
NUM_FOLDS = 10
# strategy to scoring
SCORING = 'accuracy'


def ranking():
    """
    Rank better methods based on validation dataset.
    """
    def score(model):
        """
        Get score for a model.
        """
        short, name, model_class = model
        # build cross validation
        kf = model_selection.KFold(n_splits=NUM_FOLDS, random_state=validate.SEED)
        # score between 0-1 for model
        model_results = model_selection.cross_val_score(model_class, validate.X_train,
                                                        validate.Y_train, cv=kf, scoring=SCORING)
        # short, rank percent and standard value
        return short, model_results.mean(), model_results.std()
    # call score for each model and sort by highest rank percent value
    return sorted(map(score, models), key=lambda i: i[1], reverse=True)

if __name__ == '__main__':
    # ranked best models
    [print("%s\t%f\t%f" % item) for item in ranking()]
