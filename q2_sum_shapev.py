import numpy as np
from matrix import lmatrix, complete_view, rgb_view, shape_view
from parzen_classifier import parzen_window, parzen_density
from sklearn.metrics import accuracy_score
# from q2_bay_comv import px_grass, px_brickface, px_cement, px_foliage, px_path, px_sky, px_window
# from q2_parzen_comv import p_grass, p_brickface, p_cement, p_foliage, p_path, p_sky, p_window
from random_partitions import random_parts
from multivar_classifier import multivar_density

label_parzen = np.ravel(np.zeros((2100, 1)))
valid_result = np.zeros((420, 6))
test_result = np.zeros((210, 2))
h_result = np.ravel(np.zeros((5, 1)))
valid_result_count = np.ravel(np.zeros((5, 1)))

# MATRIZES DE RESULTADO DO KFOLD
kfold_result = np.zeros((2100, 300))
kfold_result = kfold_result.astype(str)
for i in range(2100):
    for j in range(300):
        if kfold_result[i,j] == "0.0":
            kfold_result[i,j] = ""

# MULTIVARIATE NORMAL DENSITY BASED ON PARZEN WINDOW

for n in range(30):
    
    train_part = random_parts()[2]
    valid_part = random_parts()[1]
    test_part = random_parts()[0]

    for i in range(0, len(train_part)):
        if lmatrix[int(train_part[i])] == "GRASS":
            label_parzen[int(train_part[i])] = 1
        elif lmatrix[int(train_part[i])] == "WINDOW":
            label_parzen[int(train_part[i])] = 2
        elif lmatrix[int(train_part[i])] == "CEMENT":
            label_parzen[int(train_part[i])] = 3
        elif lmatrix[int(train_part[i])] == "BRICKFACE":
            label_parzen[int(train_part[i])] = 4
        elif lmatrix[int(train_part[i])] == "SKY":
            label_parzen[int(train_part[i])] = 5
        elif lmatrix[int(train_part[i])] == "FOLIAGE":
            label_parzen[int(train_part[i])] = 6
        elif lmatrix[int(train_part[i])] == "PATH":
            label_parzen[int(train_part[i])] = 7

    for i in range(0, len(valid_part)):
        if lmatrix[int(valid_part[i])] == "GRASS":
            label_parzen[int(valid_part[i])] = 1
        elif lmatrix[int(valid_part[i])] == "WINDOW":
            label_parzen[int(valid_part[i])] = 2
        elif lmatrix[int(valid_part[i])] == "CEMENT":
            label_parzen[int(valid_part[i])] = 3
        elif lmatrix[int(valid_part[i])] == "BRICKFACE":
            label_parzen[int(valid_part[i])] = 4
        elif lmatrix[int(valid_part[i])] == "SKY":
            label_parzen[int(valid_part[i])] = 5
        elif lmatrix[int(valid_part[i])] == "FOLIAGE":
            label_parzen[int(valid_part[i])] = 6
        elif lmatrix[int(valid_part[i])] == "PATH":
            label_parzen[int(valid_part[i])] = 7

    for i in range(0, len(test_part)):
        if lmatrix[int(test_part[i])] == "GRASS":
            label_parzen[int(test_part[i])] = 1
        elif lmatrix[int(test_part[i])] == "WINDOW":
            label_parzen[int(test_part[i])] = 2
        elif lmatrix[int(test_part[i])] == "CEMENT":
            label_parzen[int(test_part[i])] = 3
        elif lmatrix[int(test_part[i])] == "BRICKFACE":
            label_parzen[int(test_part[i])] = 4
        elif lmatrix[int(test_part[i])] == "SKY":
            label_parzen[int(test_part[i])] = 5
        elif lmatrix[int(test_part[i])] == "FOLIAGE":
            label_parzen[int(test_part[i])] = 6
        elif lmatrix[int(test_part[i])] == "PATH":
            label_parzen[int(test_part[i])] = 7
    
    mean_vector_grass = np.zeros((1, 8))
    mean_vector_window = np.zeros((1, 8))
    mean_vector_cement = np.zeros((1, 8))
    mean_vector_brickface = np.zeros((1, 8))
    mean_vector_sky = np.zeros((1, 8))
    mean_vector_foliage = np.zeros((1, 8))
    mean_vector_path = np.zeros((1, 8))
    covar_grass = np.identity((8))
    covar_window = np.identity((8))
    covar_cement = np.identity((8))
    covar_brickface = np.identity((8))
    covar_sky = np.identity((8))
    covar_foliage = np.identity((8))
    covar_path = np.identity((8))

    for i in range(len(train_part)):
        if lmatrix[int(train_part[i])] == "GRASS":
            mean_vector_grass += shape_view[int(train_part[i])]
        elif lmatrix[int(train_part[i])] == "WINDOW":
            mean_vector_window += shape_view[int(train_part[i])]
        elif lmatrix[int(train_part[i])] == "CEMENT":
            mean_vector_cement += shape_view[int(train_part[i])]
        elif lmatrix[int(train_part[i])] == "BRICKFACE":
            mean_vector_brickface += shape_view[int(train_part[i])]
        elif lmatrix[int(train_part[i])] == "SKY":
            mean_vector_sky += shape_view[int(train_part[i])]
        elif lmatrix[int(train_part[i])] == "FOLIAGE":
            mean_vector_foliage += shape_view[int(train_part[i])]
        elif lmatrix[int(train_part[i])] == "PATH":
            mean_vector_path += shape_view[int(train_part[i])]    
    mean_vector_grass = mean_vector_grass / 240
    mean_vector_window = mean_vector_window / 240
    mean_vector_cement = mean_vector_cement / 240
    mean_vector_brickface = mean_vector_brickface / 240
    mean_vector_sky = mean_vector_sky / 240
    mean_vector_foliage = mean_vector_foliage / 240
    mean_vector_path = mean_vector_path / 240

    for i in range(len(train_part)):
        if lmatrix[int(train_part[i])] == "GRASS":
            covar_grass += np.dot(np.transpose(shape_view[int(train_part[i])] - mean_vector_grass), shape_view[int(train_part[i])] - mean_vector_grass)
        elif lmatrix[int(train_part[i])] == "WINDOW":
            covar_window += np.dot(np.transpose(shape_view[int(train_part[i])] - mean_vector_window), shape_view[int(train_part[i])] - mean_vector_window)
        elif lmatrix[int(train_part[i])] == "CEMENT":
            covar_cement += np.dot(np.transpose(shape_view[int(train_part[i])] - mean_vector_cement), shape_view[int(train_part[i])] - mean_vector_cement)
        elif lmatrix[int(train_part[i])] == "BRICKFACE":
            covar_brickface += np.dot(np.transpose(shape_view[int(train_part[i])] - mean_vector_brickface), shape_view[int(train_part[i])] - mean_vector_brickface)
        elif lmatrix[int(train_part[i])] == "SKY":
            covar_sky += np.dot(np.transpose(shape_view[int(train_part[i])] - mean_vector_sky), shape_view[int(train_part[i])] - mean_vector_sky)
        elif lmatrix[int(train_part[i])] == "FOLIAGE":
            covar_foliage += np.dot(np.transpose(shape_view[int(train_part[i])] - mean_vector_foliage), shape_view[int(train_part[i])] - mean_vector_foliage)
        elif lmatrix[int(train_part[i])] == "PATH":
            covar_path += np.dot(np.transpose(shape_view[int(train_part[i])] - mean_vector_path), shape_view[int(train_part[i])] - mean_vector_path)
    covar_grass = np.dot(1 / 240, covar_grass)
    covar_window = np.dot(1 / 240, covar_window)
    covar_cement = np.dot(1 / 240, covar_cement)
    covar_brickface = np.dot(1 / 240, covar_brickface)
    covar_sky = np.dot(1 / 240, covar_sky)
    covar_foliage = np.dot(1 / 240, covar_foliage)
    covar_path = np.dot(1 / 240, covar_path)

    hx = 0.002
    for i in range(0, len(test_part)):
        p_grass = 0
        p_window = 0
        p_cement = 0
        p_brickface = 0
        p_sky = 0
        p_foliage = 0
        p_path = 0
        somatorio_grass = 0
        somatorio_window = 0
        somatorio_cement = 0
        somatorio_brickface = 0
        somatorio_sky = 0
        somatorio_foliage = 0
        somatorio_path = 0
        for j in range(0, len(train_part)):
            if label_parzen[int(train_part[j])] == 1:
                prod_grass = 0
                for c in range(0, 8):                            
                    if prod_grass == 0:
                        prod_grass = parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                    else:
                        prod_grass *= parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                somatorio_grass += prod_grass
            elif label_parzen[int(train_part[j])] == 2:
                prod_window = 0
                for c in range(0, 8):                            
                    if prod_window == 0:
                        prod_window = parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                    else:
                        prod_window *= parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                somatorio_window += prod_window
            elif label_parzen[int(train_part[j])] == 3:
                prod_cement = 0
                for c in range(0, 8):                            
                    if prod_cement == 0:
                        prod_cement = parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                    else:
                        prod_cement *= parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                somatorio_cement += prod_cement
            elif label_parzen[int(train_part[j])] == 4:
                prod_brickface = 0
                for c in range(0, 8):                            
                    if prod_brickface == 0:
                        prod_brickface = parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                    else:
                        prod_brickface *= parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                somatorio_brickface += prod_brickface
            elif label_parzen[int(train_part[j])] == 5:
                prod_sky = 0
                for c in range(0, 8):                            
                    if prod_sky == 0:
                        prod_sky = parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                    else:
                        prod_sky *= parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                somatorio_sky += prod_sky
            elif label_parzen[int(train_part[j])] == 6:
                prod_foliage = 0
                for c in range(0, 8):                            
                    if prod_foliage == 0:
                        prod_foliage = parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                    else:
                        prod_foliage *= parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                somatorio_foliage += prod_foliage
            elif label_parzen[int(train_part[j])] == 7:
                prod_path = 0
                for c in range(0, 8):                            
                    if prod_path == 0:
                        prod_path = parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                    else:
                        prod_path *= parzen_window(shape_view[int(test_part[i]), c], shape_view[int(train_part[j]), c], hx)
                somatorio_path += prod_path


        px_grass = multivar_density(shape_view[int(test_part[i])], np.ravel(mean_vector_grass), covar_grass)
        px_window = multivar_density(shape_view[int(test_part[i])], np.ravel(mean_vector_window), covar_window)
        px_cement = multivar_density(shape_view[int(test_part[i])], np.ravel(mean_vector_cement), covar_cement)
        px_brickface = multivar_density(shape_view[int(test_part[i])], np.ravel(mean_vector_brickface), covar_brickface)
        px_sky = multivar_density(shape_view[int(test_part[i])], np.ravel(mean_vector_sky), covar_sky)
        px_foliage = multivar_density(shape_view[int(test_part[i])], np.ravel(mean_vector_foliage), covar_foliage)
        px_path = multivar_density(shape_view[int(test_part[i])], np.ravel(mean_vector_path), covar_path)
        
        p_grass = parzen_density(somatorio_grass, hx)
        p_window = parzen_density(somatorio_window, hx)
        p_cement = parzen_density(somatorio_cement, hx)
        p_brickface = parzen_density(somatorio_brickface, hx)
        p_sky = parzen_density(somatorio_sky, hx)
        p_foliage = parzen_density(somatorio_foliage, hx)
        p_path = parzen_density(somatorio_path, hx)

        storage = [px_grass + p_grass, px_window + p_window, px_cement + p_cement, px_brickface + p_brickface, px_sky + p_sky, px_foliage + p_foliage, px_path + p_path]

        px = np.argmax(storage) + 1
    
        test_result[i, 0] = label_parzen[int(test_part[i])]
        test_result[i, 1] = px

    result_ensemble_comv = accuracy_score(test_result[:,0], test_result[:,1])
    print(r"A % de acerto do teste foi:", result_ensemble_comv)