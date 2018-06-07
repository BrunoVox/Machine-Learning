import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold
from matrix import objmatrix, lmatrix
from multivar_classifier import multivar_density
from random import randint

rskf = RepeatedStratifiedKFold(10, 30)

for train_index, validation_index, test_index in rskf.split(objmatrix, lmatrix):
    # print("TRAIN:", train_index, "TEST:", test_index)
    # objmatrix_train, objmatrix_test = objmatrix[train_index], objmatrix[test_index]
    # lmatrix_train, lmatrix_test = lmatrix[train_index], lmatrix[test_index]

    print("TRAIN:", train_index, "VALID:", validation_index, "TEST:", test_index)
    # X_train, X_test = X[train_index], X[test_index]
    # y_train, y_test = y[train_index], y[test_index]