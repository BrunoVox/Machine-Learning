import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RepeatedStratifiedKFold
from matrix import objmatrix, lmatrix, complete_view, rgb_view, shape_view
from multivar_classifier import multivar_density
from parzen_classifier import parzen_window, parzen_density
from random_partitions import random_parts

label_parzen = np.ravel(np.zeros((2100, 1)))
valid_result = np.zeros((420, 6))
test_result = np.zeros((210, 2))
h_result = np.ravel(np.zeros((5, 1)))
valid_result_count = np.ravel(np.zeros((5, 1)))

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

    # VALIDAÇÃO

    h = [0.001, 0.0012, 0.0014, 0.0017, 0.002]


    for hi in range(0, 5):    
        hx = h[hi]
        for i in range(0, len(valid_part)):
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
                            prod_grass = parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                        else:
                            prod_grass *= parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    somatorio_grass += prod_grass
                elif label_parzen[int(train_part[j])] == 2:
                    prod_window = 0
                    for c in range(0, 8):                            
                        if prod_window == 0:
                            prod_window = parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                        else:
                            prod_window *= parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    somatorio_window += prod_window
                elif label_parzen[int(train_part[j])] == 3:
                    prod_cement = 0
                    for c in range(0, 8):                            
                        if prod_cement == 0:
                            prod_cement = parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                        else:
                            prod_cement *= parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    somatorio_cement += prod_cement
                elif label_parzen[int(train_part[j])] == 4:
                    prod_brickface = 0
                    for c in range(0, 8):                            
                        if prod_brickface == 0:
                            prod_brickface = parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                        else:
                            prod_brickface *= parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    somatorio_brickface += prod_brickface
                elif label_parzen[int(train_part[j])] == 5:
                    prod_sky = 0
                    for c in range(0, 8):                            
                        if prod_sky == 0:
                            prod_sky = parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                        else:
                            prod_sky *= parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    somatorio_sky += prod_sky
                elif label_parzen[int(train_part[j])] == 6:
                    prod_foliage = 0
                    for c in range(0, 8):                            
                        if prod_foliage == 0:
                            prod_foliage = parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                        else:
                            prod_foliage *= parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    somatorio_foliage += prod_foliage
                elif label_parzen[int(train_part[j])] == 7:
                    prod_path = 0
                    for c in range(0, 8):                            
                        if prod_path == 0:
                            prod_path = parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                        else:
                            prod_path *= parzen_window(rgb_view[int(valid_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    somatorio_path += prod_path

            p_grass = parzen_density(somatorio_grass, hx)
            p_window = parzen_density(somatorio_window, hx)
            p_cement = parzen_density(somatorio_cement, hx)
            p_brickface = parzen_density(somatorio_brickface, hx)
            p_sky = parzen_density(somatorio_sky, hx)
            p_foliage = parzen_density(somatorio_foliage, hx)
            p_path = parzen_density(somatorio_path, hx)

            lista = [p_grass, p_window, p_cement, p_brickface, p_sky, p_foliage, p_path]

            px = np.argmax(lista) + 1

            if hi == 0:
                valid_result[i, 0] = label_parzen[int(valid_part[i])]
                valid_result[i, 1] = px
            else:
                valid_result[i, hi + 1] = px

        print("PROGRESSO:", (hi + 1) * 100 / 5, "%")

    # COMPARAR OS H

    result1 = accuracy_score(valid_result[:,0], valid_result[:,1])
    result2 = accuracy_score(valid_result[:,0], valid_result[:,2])
    result3 = accuracy_score(valid_result[:,0], valid_result[:,3])
    result4 = accuracy_score(valid_result[:,0], valid_result[:,4])
    result5 = accuracy_score(valid_result[:,0], valid_result[:,5])

    lista = [result1, result2, result3, result4, result5]

    print(result1, result2,result3, result4, result5)

    best_h = np.argmax(lista)
    h_test = h[best_h]

    # TEST

    hx = h_test
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
                        prod_grass = parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    else:
                        prod_grass *= parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                somatorio_grass += prod_grass
            elif label_parzen[int(train_part[j])] == 2:
                prod_window = 0
                for c in range(0, 8):                            
                    if prod_window == 0:
                        prod_window = parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    else:
                        prod_window *= parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                somatorio_window += prod_window
            elif label_parzen[int(train_part[j])] == 3:
                prod_cement = 0
                for c in range(0, 8):                            
                    if prod_cement == 0:
                        prod_cement = parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    else:
                        prod_cement *= parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                somatorio_cement += prod_cement
            elif label_parzen[int(train_part[j])] == 4:
                prod_brickface = 0
                for c in range(0, 8):                            
                    if prod_brickface == 0:
                        prod_brickface = parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    else:
                        prod_brickface *= parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                somatorio_brickface += prod_brickface
            elif label_parzen[int(train_part[j])] == 5:
                prod_sky = 0
                for c in range(0, 8):                            
                    if prod_sky == 0:
                        prod_sky = parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    else:
                        prod_sky *= parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                somatorio_sky += prod_sky
            elif label_parzen[int(train_part[j])] == 6:
                prod_foliage = 0
                for c in range(0, 8):                            
                    if prod_foliage == 0:
                        prod_foliage = parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    else:
                        prod_foliage *= parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                somatorio_foliage += prod_foliage
            elif label_parzen[int(train_part[j])] == 7:
                prod_path = 0
                for c in range(0, 8):                            
                    if prod_path == 0:
                        prod_path = parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                    else:
                        prod_path *= parzen_window(rgb_view[int(test_part[i]), c], rgb_view[int(train_part[j]), c], hx)
                somatorio_path += prod_path

        p_grass = parzen_density(somatorio_grass, hx)
        p_window = parzen_density(somatorio_window, hx)
        p_cement = parzen_density(somatorio_cement, hx)
        p_brickface = parzen_density(somatorio_brickface, hx)
        p_sky = parzen_density(somatorio_sky, hx)
        p_foliage = parzen_density(somatorio_foliage, hx)
        p_path = parzen_density(somatorio_path, hx)

        lista = [p_grass, p_window, p_cement, p_brickface, p_sky, p_foliage, p_path]

        px = np.argmax(lista) + 1
    
        test_result[i, 0] = label_parzen[int(test_part[i])]
        test_result[i, 1] = px

    result_parzen_shapev = accuracy_score(test_result[:,0], test_result[:,1])
    print(r"A % de acerto do teste foi:", result_parzen_shapev)