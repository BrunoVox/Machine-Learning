import numpy as np
from sklearn.preprocessing import normalize

def label_matrix(label, matrix):
    label = np.matrix(matrix, dtype = str)[:,0]
    return label

def object_matrix(obj, matrix):
    obj = np.matrix(matrix)[:,1:20]
    return obj

# def gen_matrix(matrixnew):
#     for m in range(0, 2100):
#         for n in range(0, 18):
#             matrixnew[m, n] = float(objmatrix[m, n])
#     return matrixnew

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
# print(type(str(lmatrix[20])))

objmatrix = object_matrix(objmatrix, matrix)
objmatrix = check(objmatrix)
# objmatrix += 1
# objmatrix = np.matrix(objmatrix)


# for i in range(0, 2100):
#     for j in range(0,18):
#         objmatrix[i,j] = float(objmatrix[i,j])

objmatrix = objmatrix.astype(float)

# print(type(objmatrix[0,0]))
# print(objmatrix[0,0])

complete_view = np.matrix((objmatrix))

shape_view = np.matrix(matrix)[:,1:9]

rgb_view = np.matrix(matrix)[:,10:19]

index_matrix = np.ravel(np.zeros((2100, 1)))
for i in range(0, len(complete_view)):
    index_matrix[i] = i
