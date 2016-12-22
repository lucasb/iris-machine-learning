#!/usr/bin/env python

from sklearn import model_selection
import load_dataset as load

# split-out validation dataset
array = load.dataset().values

seed = 7
# 80% to train and 20% to validate
validation_size = 0.20
# values
X = array[:, 0: 4]
# names
Y = array[:, 4]

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
                                                X, Y, test_size=validation_size, random_state=seed)

# constant to validate
SEED = seed
NUM_FOLDS = 10
NUM_INSTANCES = len(X_train)
SCORING = 'accuracy'


if __name__ == '__main__':
    # lines extracted
    print(X_validation)
    # names extracted
    print(Y_validation)
