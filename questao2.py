import numpy as np

def gen_classmatrix(classmatrix, classname):
    m = -1
    for i in range(0, 2100):
        if matrix[i][0] == classname:
            m += 1
            for n in range(0, 19):
                classmatrix[m][n] = matrix[i][n+1]
    return classmatrix

def gen_meanclassmatrix(classmatrix):
    return np.mean(classmatrix, axis=0)

def gen_meanclassfull(meanclassfull, classmean):
    for i in range(0, 300):
        for j in range(0, 18):
            meanclassfull[i][j] = classmean[j]
    return meanclassfull

def mvg(covar, classmatrixm, classmeanfull):
    det = np.linalg.det(covar)
    print(det)
    a = np.sqrt((2*np.pi**18)*det)
    print(a)
    b = classmatrixm - classmeanfull
    print(b)
    c = np.linalg.inv(covar)
    print(c)
    return (1/a)*(np.exp(-0.5*np.dot(np.dot(b, c), np.transpose(b))))

def check(matrix):
    count = 0
    for j in range(0, 300):
        for i in range(0,300):
            if i > 0 and matrix[i][j] == matrix[i-1][j]:
                count += 1
            if count == 299:
                matrix = np.delete(matrix, j, axis=1)
                return matrix

w, h = 20, 2100
matrix = [[0 for x in range(w)] for y in range(h)]

lines = None

with open("dados.txt", 'r') as f:
    lines = f.readlines()
   
for i, line in enumerate(lines):
    matrix[i] = line.split(",")

# # # MATRIZ DE DADOS GRASS

# # grassmatrix = np.zeros(shape=(300, 19))
# # copia_grassm = gen_classmatrix(grassmatrix, "GRASS")
# # copia_grassm_checked = check(copia_grassm)
# # copia_grassmean = gen_meanclassmatrix(copia_grassm_checked)
# # meangrassfull = np.zeros(shape=(300,18))
# # copia_meangrassfull = gen_meanclassfull(meangrassfull, copia_grassmean)
# # grasscovar = (1/18)*np.dot(np.transpose(copia_grassm_checked - copia_meangrassfull), (copia_grassm_checked - copia_meangrassfull))
# # # if grasscovar[0][1] != grasscovar[1][0]:
# # #     print("ALGO ESTA ERRADO")
# # # print(np.shape(grasscovar))
# # # print(np.all((np.linalg.eigvals(grasscovar)) >= 0))
# # mvg_grass = mvg(grasscovar, copia_grassm_checked, copia_meangrassfull)

# # # MATRIZ DE DADOS PATH

# # pathmatrix = np.zeros(shape=(300, 19))
# # copia_pathm = gen_classmatrix(pathmatrix, "PATH")
# # copia_pathm_checked = check(copia_pathm)
# # copia_pathmean = gen_meanclassmatrix(copia_pathm_checked)
# # meanpathfull = np.zeros(shape=(300,18))
# # copia_meanpathfull = gen_meanclassfull(meanpathfull, copia_pathmean)
# # pathcovar = (1/18)*np.dot(np.transpose(copia_pathm_checked - copia_meanpathfull), (copia_pathm_checked - copia_meanpathfull))
# # mvg_path = mvg(pathcovar, copia_pathm_checked, copia_meanpathfull)

# # # MATRIZ DE DADOS WINDOW

# # windowmatrix = np.zeros(shape=(300, 19))
# # copia_windowm = gen_classmatrix(windowmatrix, "WINDOW")
# # copia_windowm_checked = check(copia_windowm)
# # copia_windowmean = gen_meanclassmatrix(copia_windowm_checked)
# # meanwindowfull = np.zeros(shape=(300,18))
# # copia_meanwindowfull = gen_meanclassfull(meanwindowfull, copia_windowmean)
# # windowcovar = (1/18)*np.dot(np.transpose(copia_windowm_checked - copia_meanwindowfull), (copia_windowm_checked - copia_meanwindowfull))
# # mvg_window = mvg(windowcovar, copia_windowm_checked, copia_meanwindowfull)

# # # MATRIZ DE DADOS CEMENT

# # cementmatrix = np.zeros(shape=(300, 19))
# # copia_cementm = gen_classmatrix(cementmatrix, "CEMENT")
# # copia_cementm_checked = check(copia_cementm)
# # copia_cementmean = gen_meanclassmatrix(copia_cementm_checked)
# # meancementfull = np.zeros(shape=(300,18))
# # copia_meancementfull = gen_meanclassfull(meancementfull, copia_cementmean)
# # cementcovar = (1/18)*np.dot(np.transpose(copia_cementm_checked - copia_meancementfull), (copia_cementm_checked - copia_meancementfull))
# # mvg_cement = mvg(cementcovar, copia_cementm_checked, copia_meancementfull)

# # MATRIZ DE DADOS SKY

# skymatrix = np.zeros(shape=(300, 19))
# copia_skym = gen_classmatrix(skymatrix, "SKY")
# copia_skym_checked = check(copia_skym)
# copia_skymean = gen_meanclassmatrix(copia_skym_checked)
# meanskyfull = np.zeros(shape=(300,18))
# copia_meanskyfull = gen_meanclassfull(meanskyfull, copia_skymean)
# skycovar = (1/18)*np.dot(np.transpose(copia_skym_checked - copia_meanskyfull), (copia_skym_checked - copia_meanskyfull))
# # if skycovar[0][1] != skycovar[1][0]:
# #     print("ALGO ESTA ERRADO")
# # print(np.shape(skycovar))
# # print(np.all((np.linalg.eigvals(skycovar)) >= 0))
# mvg_sky = mvg(skycovar, copia_skym_checked, copia_meanskyfull)

# # # MATRIZ DE DADOS BRICKFACE

# # brickfacematrix = np.zeros(shape=(300, 19))
# # copia_brickfacem = gen_classmatrix(brickfacematrix, "BRICKFACE")
# # copia_brickfacem_checked = check(copia_brickfacem)
# # copia_brickfacemean = gen_meanclassmatrix(copia_brickfacem_checked)
# # meanbrickfacefull = np.zeros(shape=(300,18))
# # copia_meanbrickfacefull = gen_meanclassfull(meanbrickfacefull, copia_brickfacemean)
# # brickfacecovar = (1/18)*np.dot(np.transpose(copia_brickfacem_checked - copia_meanbrickfacefull), (copia_brickfacem_checked - copia_meanbrickfacefull))
# # mvg_brickface = mvg(brickfacecovar, copia_brickfacem_checked, copia_meanbrickfacefull)

# # # MATRIZ DE DADOS FOLIAGE

# # foliagematrix = np.zeros(shape=(300, 19))
# # copia_foliagem = gen_classmatrix(foliagematrix, "FOLIAGE")
# # copia_foliagem_checked = check(copia_foliagem)
# # copia_foliagemean = gen_meanclassmatrix(copia_foliagem_checked)
# # meanfoliagefull = np.zeros(shape=(300,18))
# # copia_meanfoliagefull = gen_meanclassfull(meanfoliagefull, copia_foliagemean)
# # foliagecovar = (1/18)*np.dot(np.transpose(copia_foliagem_checked - copia_meanfoliagefull), (copia_foliagem_checked - copia_meanfoliagefull))
# # mvg_foliage = mvg(foliagecovar, copia_foliagem_checked, copia_meanfoliagefull)