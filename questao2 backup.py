import numpy as np

def gen_classmatrix(classmatrix, classname):
    classmatrix = np.zeros(shape=(300,19))
    m = -1
    for i in range(0, 2100):
        if matrix[i][0] == classname:
            n = 0
            m += 1
            for n in range(0, 19):
                classmatrix[m][n] = matrix[i][n+1]
    return classmatrix

def gen_meanclassmatrix(classmatrix):
    return np.mean(classmatrix, axis=0)

w, h = 20, 2100
matrix = [[0 for x in range(w)] for y in range(h)]

lines = None

with open("dados.txt", 'r') as f:
    lines = f.readlines()
   
for i, line in enumerate(lines):
    matrix[i] = line.split(",")

# print(np.matrix(matrix))

# MATRIZ DE DADOS GRASS

grassmatrix = np.zeros(shape=(300, 19))
# m = -1
# for i in range(0, 2100):
#     if matrix[i][0] == "GRASS":
#         n = 0
#         m += 1
#         for n in range(0, 19):
#             grassmatrix[m][n] = matrix[i][n+1]

copia_grassm = gen_classmatrix(grassmatrix, "GRASS")
        
print(np.matrix(copia_grassm))

# MATRIZ DE DADOS PATH

pathmatrix = np.zeros(shape=(300, 19))
# m = -1
# for i in range(0, 2100):
#     if matrix[i][0] == "PATH":
#         n = 0
#         m += 1
#         for n in range(0, 19):
#             pathmatrix[m][n] = matrix[i][n+1]

copia_pathm = gen_classmatrix(pathmatrix, "PATH")
        
print(np.matrix(copia_pathm))

# MATRIZ DE DADOS WINDOW

windowmatrix = np.zeros(shape=(300, 19))
# m = -1
# for i in range(0, 2100):
#     if matrix[i][0] == "WINDOW":
#         n = 0
#         m += 1
#         for n in range(0, 19):
#             windowmatrix[m][n] = matrix[i][n+1]

copia_windowm = gen_classmatrix(windowmatrix, "WINDOW")
        
print(np.matrix(copia_windowm))

# MATRIZ DE DADOS CEMENT

cementmatrix = np.zeros(shape=(300, 19))
# m = -1
# for i in range(0, 2100):
#     if matrix[i][0] == "CEMENT":
#         n = 0
#         m += 1
#         for n in range(0, 19):
#             cementmatrix[m][n] = matrix[i][n+1]

copia_cementm = gen_classmatrix(cementmatrix, "CEMENT")
        
print(np.matrix(copia_cementm))

# MATRIZ DE DADOS SKY

skymatrix = np.zeros(shape=(300, 19))
# m = -1
# for i in range(0, 2100):
#     if matrix[i][0] == "SKY":
#         n = 0
#         m += 1
#         for n in range(0, 19):
#             skymatrix[m][n] = matrix[i][n+1]

copia_skym = gen_classmatrix(skymatrix, "SKY")
        
print(np.matrix(copia_skym))

# MATRIZ DE DADOS BRICKFACE

brickfacematrix = np.zeros(shape=(300, 19))
# m = -1
# for i in range(0, 2100):
#     if matrix[i][0] == "BRICKFACE":
#         n = 0
#         m += 1
#         for n in range(0, 19):
#             brickfacematrix[m][n] = matrix[i][n+1]

copia_brickfacem = gen_classmatrix(brickfacematrix, "BRICKFACE")
        
print(np.matrix(copia_brickfacem))

# MATRIZ DE DADOS FOLIAGE

foliagematrix = np.zeros(shape=(300, 19))
# m = -1
# for i in range(0, 2100):
#     if matrix[i][0] == "FOLIAGE":
#         n = 0
#         m += 1
#         for n in range(0, 19):
#             foliagematrix[m][n] = matrix[i][n+1]

# print(np.mean(foliagematrix, axis=0))

copia_foliagem = gen_classmatrix(foliagematrix, "FOLIAGE")
        
print(np.matrix(copia_foliagem))

# a = np.mean(foliagematrix, axis=0)
# print(a)

copia_foliagemean = gen_meanclassmatrix(copia_foliagem)

print(copia_foliagemean)

# print(np.matrix(copia_foliagemean))

# teste = [[1,2],[3,4]]
# print(teste[0][1]) #PRIMEIRO É A LINHA, SEGUNDO É A COLUNA