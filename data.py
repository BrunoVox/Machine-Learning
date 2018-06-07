import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold
from matrix import objmatrix, lmatrix
from multivar_classifier import multivar_density

rskf = RepeatedStratifiedKFold(10, 30)

# MATRIZES DE RESULTADO DO KFOLD
kfold_result = np.zeros((2100,300))
kfold_result = kfold_result.astype(str)
for i in range(0, 2100):
    for j in range(0, 300):
        if kfold_result[i,j] == "0.0":
            kfold_result[i,j] = ""

# MULTIVARIATE NORMAL DENSITY

j = -1

for train_index, test_index in rskf.split(objmatrix, lmatrix):
    # print("TRAIN:", train_index, "TEST:", test_index)
    # objmatrix_train, objmatrix_test = objmatrix[train_index], objmatrix[test_index]
    # lmatrix_train, lmatrix_test = lmatrix[train_index], lmatrix[test_index]

    j += 1

    mean_vector_grass = np.zeros((1, 18))
    mean_vector_window = np.zeros((1, 18))
    mean_vector_cement = np.zeros((1, 18))
    mean_vector_brickface = np.zeros((1, 18))
    mean_vector_sky = np.zeros((1, 18))
    mean_vector_foliage = np.zeros((1, 18))
    mean_vector_path = np.zeros((1, 18))
    covar_grass = np.identity((18))
    covar_window = np.identity((18))
    covar_cement = np.identity((18))
    covar_brickface = np.identity((18))
    covar_sky = np.identity((18))
    covar_foliage = np.identity((18))
    covar_path = np.identity((18))

    print("ANDAMENTO:", (j * 100) / 300, "%")

    for i in range(0, 1890):
        if lmatrix[train_index[i]] == "GRASS":
            # print(np.matrix(objmatrix[train_index[i],:]))
            mean_vector_grass += objmatrix[train_index[i]]
        if lmatrix[train_index[i]] == "WINDOW":
            mean_vector_window += np.matrix(objmatrix[train_index[i]])
        if lmatrix[train_index[i]] == "CEMENT":
            mean_vector_cement += np.matrix(objmatrix[train_index[i]])
        if lmatrix[train_index[i]] == "BRICKFACE":
            mean_vector_brickface += np.matrix(objmatrix[train_index[i]])
        if lmatrix[train_index[i]] == "SKY":
            mean_vector_sky += np.matrix(objmatrix[train_index[i]])
        if lmatrix[train_index[i]] == "FOLIAGE":
            mean_vector_foliage += np.matrix(objmatrix[train_index[i]])
        if lmatrix[train_index[i]] == "PATH":
            mean_vector_path += np.matrix(objmatrix[train_index[i]])    
    mean_vector_grass = mean_vector_grass / 270
    mean_vector_window = mean_vector_window / 270
    mean_vector_cement = mean_vector_cement / 270
    mean_vector_brickface = mean_vector_brickface / 270
    mean_vector_sky = mean_vector_sky / 270
    mean_vector_foliage = mean_vector_foliage / 270
    mean_vector_path = mean_vector_path / 270

    for i in range(0, 1890):
        if lmatrix[train_index[i]] == "GRASS":
            covar_grass += np.dot(np.transpose(objmatrix[train_index[i]] - mean_vector_grass), objmatrix[train_index[i]] - mean_vector_grass)
        if lmatrix[train_index[i]] == "WINDOW":
            covar_window += np.dot(np.transpose(objmatrix[train_index[i]] - mean_vector_window), objmatrix[train_index[i]] - mean_vector_window)
        if lmatrix[train_index[i]] == "CEMENT":
            covar_cement += np.dot(np.transpose(objmatrix[train_index[i]] - mean_vector_cement), objmatrix[train_index[i]] - mean_vector_cement)
        if lmatrix[train_index[i]] == "BRICKFACE":
            covar_brickface += np.dot(np.transpose(objmatrix[train_index[i]] - mean_vector_brickface), objmatrix[train_index[i]] - mean_vector_brickface)
        if lmatrix[train_index[i]] == "SKY":
            covar_sky += np.dot(np.transpose(objmatrix[train_index[i]] - mean_vector_sky), objmatrix[train_index[i]] - mean_vector_sky)
        if lmatrix[train_index[i]] == "FOLIAGE":
            covar_foliage += np.dot(np.transpose(objmatrix[train_index[i]] - mean_vector_foliage), objmatrix[train_index[i]] - mean_vector_foliage)
        if lmatrix[train_index[i]] == "PATH":
            covar_path += np.dot(np.transpose(objmatrix[train_index[i]] - mean_vector_path), objmatrix[train_index[i]] - mean_vector_path)
    covar_grass = np.dot(1 / 270, covar_grass)
    covar_window = np.dot(1 / 270, covar_window)
    covar_cement = np.dot(1 / 270, covar_cement)
    covar_brickface = np.dot(1 / 270, covar_brickface)
    covar_sky = np.dot(1 / 270, covar_sky)
    covar_foliage = np.dot(1 / 270, covar_foliage)
    covar_path = np.dot(1 / 270, covar_path)

    

    for i in range(0, 210):
        px_grass = multivar_density(objmatrix[test_index[i]], np.ravel(mean_vector_grass), covar_grass)
        px_window = multivar_density(objmatrix[test_index[i]], np.ravel(mean_vector_window), covar_window)
        px_cement = multivar_density(objmatrix[test_index[i]], np.ravel(mean_vector_cement), covar_cement)
        px_brickface = multivar_density(objmatrix[test_index[i]], np.ravel(mean_vector_brickface), covar_brickface)
        px_sky = multivar_density(objmatrix[test_index[i]], np.ravel(mean_vector_sky), covar_sky)
        px_foliage = multivar_density(objmatrix[test_index[i]], np.ravel(mean_vector_foliage), covar_foliage)
        px_path = multivar_density(objmatrix[test_index[i]], np.ravel(mean_vector_path), covar_path)
        storage = {px_grass, px_window, px_cement, px_brickface, px_sky, px_foliage, px_path}
        if max(storage) == px_grass:
            kfold_result[test_index[i],j] = "GRASS"
        if max(storage) == px_window:
            kfold_result[test_index[i],j] = "WINDOW"
        if max(storage) == px_cement:
            kfold_result[test_index[i],j] = "CEMENT"
        if max(storage) == px_brickface:
            kfold_result[test_index[i],j] = "BRICKFACE"
        if max(storage) == px_sky:
            kfold_result[test_index[i],j] = "SKY"
        if max(storage) == px_foliage:
            kfold_result[test_index[i],j] = "FOLIAGE"
        if max(storage) == px_path:
            kfold_result[test_index[i],j] = "PATH"



# K FOLD METRICS

print("FINALIZANDO...")

correct = 0
wrong = 0

for j in range(0, 300):
    for i in range(0, 2100):
        if kfold_result[i,j] == "":
            continue
        if lmatrix[i] == kfold_result[i,j]:
            correct += 1
        else:
            wrong += 1

total = correct + wrong

print("A PORCENTAGEM DE ACERTO TOTAL FOI:", float((correct * 100)/(total)), "%")



# with open("out.txt", "w") as output:
#     output.write(kfold_result)