import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold
from matrix import objmatrix, lmatrix, complete_view, rgb_view
from multivar_classifier import multivar_density

rskf = RepeatedStratifiedKFold(10, 30)

# MATRIZES DE RESULTADO DO KFOLD
kfold_result = np.zeros((2100, 300))
kfold_result = kfold_result.astype(str)
for i in range(2100):
    for j in range(300):
        if kfold_result[i,j] == "0.0":
            kfold_result[i,j] = ""

# MULTIVARIATE NORMAL DENSITY

j = -1

for train_index, test_index in rskf.split(rgb_view, lmatrix):
    
    j += 1
    
    mean_vector_grass = np.zeros((1, 10))
    mean_vector_window = np.zeros((1, 10))
    mean_vector_cement = np.zeros((1, 10))
    mean_vector_brickface = np.zeros((1, 10))
    mean_vector_sky = np.zeros((1, 10))
    mean_vector_foliage = np.zeros((1, 10))
    mean_vector_path = np.zeros((1, 10))
    covar_grass = np.identity((10))
    covar_window = np.identity((10))
    covar_cement = np.identity((10))
    covar_brickface = np.identity((10))
    covar_sky = np.identity((10))
    covar_foliage = np.identity((10))
    covar_path = np.identity((10))

    print("ANDAMENTO:", (j * 100) / 300, "%")

    for i in range(1890):
        if lmatrix[train_index[i]] == "GRASS":
            mean_vector_grass += rgb_view[train_index[i]]
        elif lmatrix[train_index[i]] == "WINDOW":
            mean_vector_window += rgb_view[train_index[i]]
        elif lmatrix[train_index[i]] == "CEMENT":
            mean_vector_cement += rgb_view[train_index[i]]
        elif lmatrix[train_index[i]] == "BRICKFACE":
            mean_vector_brickface += rgb_view[train_index[i]]
        elif lmatrix[train_index[i]] == "SKY":
            mean_vector_sky += rgb_view[train_index[i]]
        elif lmatrix[train_index[i]] == "FOLIAGE":
            mean_vector_foliage += rgb_view[train_index[i]]
        elif lmatrix[train_index[i]] == "PATH":
            mean_vector_path += rgb_view[train_index[i]]    
    mean_vector_grass = mean_vector_grass / 270
    mean_vector_window = mean_vector_window / 270
    mean_vector_cement = mean_vector_cement / 270
    mean_vector_brickface = mean_vector_brickface / 270
    mean_vector_sky = mean_vector_sky / 270
    mean_vector_foliage = mean_vector_foliage / 270
    mean_vector_path = mean_vector_path / 270

    for i in range(1890):
        if lmatrix[train_index[i]] == "GRASS":
            covar_grass += np.dot(np.transpose(rgb_view[train_index[i]] - mean_vector_grass), rgb_view[train_index[i]] - mean_vector_grass)
        elif lmatrix[train_index[i]] == "WINDOW":
            covar_window += np.dot(np.transpose(rgb_view[train_index[i]] - mean_vector_window), rgb_view[train_index[i]] - mean_vector_window)
        elif lmatrix[train_index[i]] == "CEMENT":
            covar_cement += np.dot(np.transpose(rgb_view[train_index[i]] - mean_vector_cement), rgb_view[train_index[i]] - mean_vector_cement)
        elif lmatrix[train_index[i]] == "BRICKFACE":
            covar_brickface += np.dot(np.transpose(rgb_view[train_index[i]] - mean_vector_brickface), rgb_view[train_index[i]] - mean_vector_brickface)
        elif lmatrix[train_index[i]] == "SKY":
            covar_sky += np.dot(np.transpose(rgb_view[train_index[i]] - mean_vector_sky), rgb_view[train_index[i]] - mean_vector_sky)
        elif lmatrix[train_index[i]] == "FOLIAGE":
            covar_foliage += np.dot(np.transpose(rgb_view[train_index[i]] - mean_vector_foliage), rgb_view[train_index[i]] - mean_vector_foliage)
        elif lmatrix[train_index[i]] == "PATH":
            covar_path += np.dot(np.transpose(rgb_view[train_index[i]] - mean_vector_path), rgb_view[train_index[i]] - mean_vector_path)
    covar_grass = np.dot(1 / 270, covar_grass)
    covar_window = np.dot(1 / 270, covar_window)
    covar_cement = np.dot(1 / 270, covar_cement)
    covar_brickface = np.dot(1 / 270, covar_brickface)
    covar_sky = np.dot(1 / 270, covar_sky)
    covar_foliage = np.dot(1 / 270, covar_foliage)
    covar_path = np.dot(1 / 270, covar_path)

    

    for i in range(210):
        px_grass = multivar_density(rgb_view[test_index[i]], np.ravel(mean_vector_grass), covar_grass)
        px_window = multivar_density(rgb_view[test_index[i]], np.ravel(mean_vector_window), covar_window)
        px_cement = multivar_density(rgb_view[test_index[i]], np.ravel(mean_vector_cement), covar_cement)
        px_brickface = multivar_density(rgb_view[test_index[i]], np.ravel(mean_vector_brickface), covar_brickface)
        px_sky = multivar_density(rgb_view[test_index[i]], np.ravel(mean_vector_sky), covar_sky)
        px_foliage = multivar_density(rgb_view[test_index[i]], np.ravel(mean_vector_foliage), covar_foliage)
        px_path = multivar_density(rgb_view[test_index[i]], np.ravel(mean_vector_path), covar_path)
        storage = [px_grass, px_window, px_cement, px_brickface, px_sky, px_foliage, px_path]
        if max(storage) == px_grass:
            kfold_result[test_index[i],j] = "GRASS"
        elif max(storage) == px_window:
            kfold_result[test_index[i],j] = "WINDOW"
        elif max(storage) == px_cement:
            kfold_result[test_index[i],j] = "CEMENT"
        elif max(storage) == px_brickface:
            kfold_result[test_index[i],j] = "BRICKFACE"
        elif max(storage) == px_sky:
            kfold_result[test_index[i],j] = "SKY"
        elif max(storage) == px_foliage:
            kfold_result[test_index[i],j] = "FOLIAGE"
        elif max(storage) == px_path:
            kfold_result[test_index[i],j] = "PATH"

# K FOLD METRICS

print("FINALIZANDO...")

correct = 0
wrong = 0

for j in range(300):
    for i in range(2100):
        if kfold_result[i,j] == "":
            continue
        if lmatrix[i] == kfold_result[i,j]:
            correct += 1
        else:
            wrong += 1

total = correct + wrong

print("A PORCENTAGEM DE ACERTO TOTAL FOI:", float((correct * 100)/(total)), "%")

result_bay_rgbv = correct / total