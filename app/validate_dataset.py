#!/usr/bin/env python
from sklearn import model_selection
import load_dataset as load

# Split-out validation dataset
array = load.dataset().values

# 80% to train and 20% to validate
validation_size = 0.20
# values
X = array[:, 0: 4]
# names
Y = array[:, 4]

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
                                                X, Y, test_size=validation_size, random_state=7)

if __name__ == '__main__':
    print(X_validation)
    print(Y_validation)
