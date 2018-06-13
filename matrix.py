import numpy as np
from sklearn.preprocessing import scale

def label_matrix(label, matrix):
    label = np.matrix(matrix, dtype = str)[:,0]
    return label

def object_matrix(obj, matrix):
    obj = np.matrix(matrix)[:,1:20]
    return obj

def check(matrix):
    count = 0
    for j in range(0, 18):
        for i in range(1,2100):
            if matrix[i,j] == matrix[i-1,j]:
                count += 1
            if count == 2099:
                matrix = np.delete(matrix, j, axis=1)
                # count = 0
                return matrix

w, h = 20, 2100
matrix = [[0 for x in range(w)] for y in range(h)]

lines = None

with open("dados.txt", 'r') as f:
    lines = f.readlines()
   
for i, line in enumerate(lines):
    matrix[i] = line.split(",")

lmatrix = np.zeros((2100, 1))
objmatrix = np.zeros((2100, 19))

lmatrix = label_matrix(lmatrix, matrix)
objmatrix = object_matrix(objmatrix, matrix)
objmatrix = check(objmatrix)
objmatrix = objmatrix.astype(float)
complete_view = np.matrix(objmatrix)
shape_view = complete_view[:,0:8]
rgb_view = complete_view[:,8:18]
index_matrix = np.zeros((2100,))
for i in range(0, len(complete_view)):
    index_matrix[i] = i

kcm_check = np.zeros((2100,))

for i in range(2100):
    for j in range(1):
        if matrix[i][j] == "GRASS":
            kcm_check[i] = 0
        if matrix[i][j] == "WINDOW":
            kcm_check[i] = 1
        if matrix[i][j] == "CEMENT":
            kcm_check[i] = 2
        if matrix[i][j] == "BRICKFACE":
            kcm_check[i] = 3
        if matrix[i][j] == "SKY":
            kcm_check[i] = 4
        if matrix[i][j] == "FOLIAGE":
            kcm_check[i] = 5
        if matrix[i][j] == "PATH":
            kcm_check[i] = 6 