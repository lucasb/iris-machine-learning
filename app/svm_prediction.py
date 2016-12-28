#!/usr/bin/env python

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import validate_dataset as validate

# Make predictions using Support Vector Machines
svm = SVC()
# load train data from validate
svm.fit(validate.X_train, validate.Y_train)
# get predictions and registers from validation
predictions = svm.predict(validate.X_validation)
registers = validate.Y_validation


if __name__ == '__main__':
    # accuracy score 0.9333 is equal 93,33%
    print(accuracy_score(registers, predictions))
    # matrix with 3 errors made
    print(confusion_matrix(registers, predictions))
    # classification table (precision, recall, f1-score, support)
    print(classification_report(registers, predictions))
