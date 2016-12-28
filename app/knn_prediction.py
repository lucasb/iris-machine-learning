#!/usr/bin/env python

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import validate_dataset as validate

# Make predictions using K-Nearest Neighbors
knn = KNeighborsClassifier()
# load train data from validate
knn.fit(validate.X_train, validate.Y_train)
# get predictions and registers from validation
predictions = knn.predict(validate.X_validation)
registers = validate.Y_validation


if __name__ == '__main__':
    # accuracy score 0.9 is equal 90%
    print(accuracy_score(registers, predictions))
    # matrix with 3 errors made
    print(confusion_matrix(registers, predictions))
    # classification table (precision, recall, f1-score, support)
    print(classification_report(registers, predictions))
