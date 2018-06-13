import numpy as np
from sklearn.preprocessing import scale

def label_matrix(label, matrix):
    label = np.matrix(matrix, dtype = str)[:,0]
    return label

def object_matrix(obj, matrix):
    obj = np.matrix(matrix)[:,1:20]
    return obj

def check(matrix):
    # count = 0
    # for j in range(0, 18):
    #     for i in range(1,2100):
    #         if matrix[i,j] == matrix[i-1,j]:
    #             count += 1
    #         if count == 2099:
    #             matrix = np.delete(matrix, j, axis=1)
    #             return matrix

    matrix = np.delete(matrix, 2, axis=1)
    matrix = np.delete(matrix, 2, axis=1)
    matrix = np.delete(matrix, 2, axis=1)
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
shape_view = complete_view[:,0:6]
rgb_view = complete_view[:,6:16]
index_matrix = np.zeros((2100,))
for i in range(0, len(complete_view)):
    index_matrix[i] = i

kcm_check = np.zeros((2100,))
grass_matrix = np.zeros((300, 19))
window_matrix = np.zeros((300, 19))
cement_matrix = np.zeros((300, 19))
brickface_matrix = np.zeros((300, 19))
sky_matrix = np.zeros((300, 19))
foliage_matrix = np.zeros((300, 19))
path_matrix = np.zeros((300, 19))

grass_matrix_mean = np.zeros((1, 19))
window_matrix_mean = np.zeros((1, 19))
cement_matrix_mean = np.zeros((1, 19))
brickface_matrix_mean = np.zeros((1, 19))
sky_matrix_mean = np.zeros((1, 19))
foliage_matrix_mean = np.zeros((1, 19))
path_matrix_mean = np.zeros((1, 19))

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

# GRASS MATRIX
# countgrass = 0
# countwindow = 0
# countcement = 0
# countbrickface = 0
# countsky = 0
# countfoliage = 0
# countpath = 0
# for i in range(2100):
#     if lmatrix[i] == "GRASS":
#         for j in range(19):
#             grass_matrix[countgrass,j] = complete_view[i,j]
#         countgrass += 1
#     if lmatrix[i] == "WINDOW":
#         for j in range(19):
#             window_matrix[countwindow,j] = complete_view[i,j]
#         countwindow += 1
#     if lmatrix[i] == "CEMENT":
#         for j in range(19):
#             cement_matrix[countcement,j] = complete_view[i,j]
#         countcement += 1    
#     if lmatrix[i] == "BRICKFACE":
#         for j in range(19):
#             brickface_matrix[countbrickface,j] = complete_view[i,j]
#         countbrickface += 1
#     if lmatrix[i] == "SKY":
#         for j in range(19):
#             sky_matrix[countsky,j] = complete_view[i,j]
#         countsky += 1
#     if lmatrix[i] == "FOLIAGE":
#         for j in range(19):
#             foliage_matrix[countfoliage,j] = complete_view[i,j]
#         countfoliage += 1
#     if lmatrix[i] == "PATH":
#         for j in range(19):
#             path_matrix[countpath,j] = complete_view[i,j]
#         countpath += 1

# for j in range(19):
#     temp = 0
#     for i in range(300):
#         temp += grass_matrix[i,j]
#     grass_matrix_mean[0,j] = temp/300
# print(grass_matrix_mean[0,10])

# for j in range(19):
#     temp = 0
#     for i in range(300):
#         temp += window_matrix[i,j]
#     window_matrix_mean[0,j] = temp/300
# print(window_matrix_mean[0,10])

# for j in range(19):
#     temp = 0
#     for i in range(300):
#         temp += cement_matrix[i,j]
#     cement_matrix_mean[0,j] = temp/300
# print(cement_matrix_mean[0,10])

# for j in range(19):
#     temp = 0
#     for i in range(300):
#         temp += brickface_matrix[i,j]
#     brickface_matrix_mean[0,j] = temp/300
# print(brickface_matrix_mean[0,10])

# for j in range(19):
#     temp = 0
#     for i in range(300):
#         temp += sky_matrix[i,j]
#     sky_matrix_mean[0,j] = temp/300
# print(sky_matrix_mean[0,10])

# for j in range(19):
#     temp = 0
#     for i in range(300):
#         temp += foliage_matrix[i,j]
#     foliage_matrix_mean[0,j] = temp/300
# print(foliage_matrix_mean[0,10])

# for j in range(19):
#     temp = 0
#     for i in range(300):
#         temp += path_matrix[i,j]
#     path_matrix_mean[0,j] = temp/300
# print(path_matrix_mean[0,10])

# total = (grass_matrix_mean[0,10] + window_matrix_mean[0,10] + cement_matrix_mean[0,10] + brickface_matrix_mean[0,10] + foliage_matrix_mean[0,10] + path_matrix_mean[0,10] + sky_matrix_mean[0,10]) / 7

# print('DECISÃO:', total)