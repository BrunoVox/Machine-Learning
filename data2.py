import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold
from matrix import objmatrix, lmatrix, complete_view
from multivar_classifier import multivar_density
from parzen_classifier import parzen_window, parzen_density

rskf = RepeatedStratifiedKFold(10, 30)

# MATRIZES DE RESULTADO DO KFOLD
kfold_result1 = np.zeros((2100,300))
kfold_result1 = kfold_result1.astype(str)
for i in range(0, 2100):
    for j in range(0, 300):
        if kfold_result1[i,j] == "0.0":
            kfold_result1[i,j] = ""

kfold_result2 = np.zeros((2100,300))
kfold_result2 = kfold_result2.astype(str)
for i in range(0, 2100):
    for j in range(0, 300):
        if kfold_result2[i,j] == "0.0":
            kfold_result2[i,j] = ""

kfold_result3 = np.zeros((2100,300))
kfold_result3 = kfold_result3.astype(str)
for i in range(0, 2100):
    for j in range(0, 300):
        if kfold_result3[i,j] == "0.0":
            kfold_result3[i,j] = ""

kfold_result4 = np.zeros((2100,300))
kfold_result4 = kfold_result4.astype(str)
for i in range(0, 2100):
    for j in range(0, 300):
        if kfold_result4[i,j] == "0.0":
            kfold_result4[i,j] = ""

kfold_result5 = np.zeros((2100,300))
kfold_result5 = kfold_result5.astype(str)
for i in range(0, 2100):
    for j in range(0, 300):
        if kfold_result5[i,j] == "0.0":
            kfold_result5[i,j] = ""

# MULTIVARIATE NORMAL DENSITY BASED ON PARZEN WINDOW



for train_index, test_index in rskf.split(objmatrix, lmatrix):
    # print("TRAIN:", train_index, "TEST:", test_index)
    # objmatrix_train, objmatrix_test = objmatrix[train_index], objmatrix[test_index]
    # lmatrix_train, lmatrix_test = lmatrix[train_index], lmatrix[test_index]

    for h in range(np.array([0.2, 0.6, 1, 1.4, 1.8])):
        Kernel_grass = 0
        Kernel_window = 0
        Kernel_cement = 0
        Kernel_brickface = 0
        Kernel_sky = 0
        Kernel_foliage = 0
        Kernel_path = 0
        for i in range(0, 1470):
            for j in range(0, 1470):
                # CÁLCULO DO PRODUTÓRIO DOS KERNELS PARA CADA CLASSE
                if lmatrix[train_index[j]] == "GRASS":
                    for k in range(0, 19):
                        Kernel_grass_temp *= parzen_window(complete_view[train_index[i], k], complete_view[train_index[j], k], h)
                    Kernel_grass += Kernel_grass_temp
                if lmatrix[train_index[j]] == "WINDOW":
                    Kernel_window = parzen_window(complete_view[train_index[i]], complete_view[train_index[j]], h) * Kernel_window
                if lmatrix[train_index[j]] == "CEMENT":
                    Kernel_cement = parzen_window(complete_view[train_index[i]], complete_view[train_index[j]], h) * Kernel_cement
                if lmatrix[train_index[j]] == "BRICKFACE":
                    Kernel_brickface = parzen_window(complete_view[train_index[i]], complete_view[train_index[j]], h) * Kernel_brickface
                if lmatrix[train_index[j]] == "SKY":
                    Kernel_sky = parzen_window(complete_view[train_index[i]], complete_view[train_index[j]], h) * Kernel_sky
                if lmatrix[train_index[j]] == "FOLIAGE":
                    Kernel_foliage = parzen_window(complete_view[train_index[i]], complete_view[train_index[j]], h) * Kernel_foliage
                if lmatrix[train_index[j]] == "PATH":
                    Kernel_path = parzen_window(complete_view[train_index[i]], complete_view[train_index[j]], h) * Kernel_path

            # for j in range(0, 1470):
            #     # CÁLCULO DA PROBABILIDADE DE UM DETERMINADO PONTO SER DE UMA CLASSE
            #     px_grass = parzen_density(Kernel_grass, h)
            #     px_window = parzen_density(Kernel_window, h)
            #     px_cement = parzen_density(Kernel_cement, h)
            #     px_brickface = parzen_density(Kernel_brickface, h)
            #     px_sky = parzen_density(Kernel_sky, h)
            #     px_foliage = parzen_density(Kernel_foliage, h)
            #     px_path = parzen_density(Kernel_path, h)
            #     storage = [px_grass, px_window, px_cement, px_brickface, px_sky, px_foliage, px_path]
            #     if max(storage) == px_grass:
            #         if h == 0.2:
            #             kfold_result1[train_index[i],j] = "GRASS"
            #         if h == 0.6:
            #             kfold_result2[train_index[i],j] = "GRASS"
            #         if h == 1:
            #             kfold_result3[train_index[i],j] = "GRASS"
            #         if h == 1.4:
            #             kfold_result4[train_index[i],j] = "GRASS"
            #         if h == 1.8:
            #             kfold_result5[train_index[i],j] = "GRASS"
            #     if max(storage) == px_window:
            #         if h == 0.2:
            #             kfold_result1[train_index[i],j] = "WINDOW"
            #         if h == 0.6:
            #             kfold_result2[train_index[i],j] = "WINDOW"
            #         if h == 1:
            #             kfold_result3[train_index[i],j] = "WINDOW"
            #         if h == 1.4:
            #             kfold_result4[train_index[i],j] = "WINDOW"
            #         if h == 1.8:
            #             kfold_result5[train_index[i],j] = "WINDOW"
            #     if max(storage) == px_cement:
            #         if h == 0.2:
            #             kfold_result1[train_index[i],j] = "CEMENT"
            #         if h == 0.6:
            #             kfold_result2[train_index[i],j] = "CEMENT"
            #         if h == 1:
            #             kfold_result3[train_index[i],j] = "CEMENT"
            #         if h == 1.4:
            #             kfold_result4[train_index[i],j] = "CEMENT"
            #         if h == 1.8:
            #             kfold_result5[train_index[i],j] = "CEMENT"
            #     if max(storage) == px_brickface:
            #         if h == 0.2:
            #             kfold_result1[train_index[i],j] = "BRICKFACE"
            #         if h == 0.6:
            #             kfold_result2[train_index[i],j] = "BRICKFACE"
            #         if h == 1:
            #             kfold_result3[train_index[i],j] = "BRICKFACE"
            #         if h == 1.4:
            #             kfold_result4[train_index[i],j] = "BRICKFACE"
            #         if h == 1.8:
            #             kfold_result5[train_index[i],j] = "BRICKFACE"
            #     if max(storage) == px_sky:
            #         if h == 0.2:
            #             kfold_result1[train_index[i],j] = "SKY"
            #         if h == 0.6:
            #             kfold_result2[train_index[i],j] = "SKY"
            #         if h == 1:
            #             kfold_result3[train_index[i],j] = "SKY"
            #         if h == 1.4:
            #             kfold_result4[train_index[i],j] = "SKY"
            #         if h == 1.8:
            #             kfold_result5[train_index[i],j] = "SKY"
            #     if max(storage) == px_foliage:
            #         if h == 0.2:
            #             kfold_result1[train_index[i],j] = "FOLIAGE"
            #         if h == 0.6:
            #             kfold_result2[train_index[i],j] = "FOLIAGE"
            #         if h == 1:
            #             kfold_result3[train_index[i],j] = "FOLIAGE"
            #         if h == 1.4:
            #             kfold_result4[train_index[i],j] = "FOLIAGE"
            #         if h == 1.8:
            #             kfold_result5[train_index[i],j] = "FOLIAGE"
            #     if max(storage) == px_path:
            #         if h == 0.2:
            #             kfold_result1[train_index[i],j] = "PATH"
            #         if h == 0.6:
            #             kfold_result2[train_index[i],j] = "PATH"
            #         if h == 1:
            #             kfold_result3[train_index[i],j] = "PATH"
            #         if h == 1.4:
            #             kfold_result4[train_index[i],j] = "PATH"
            #         if h == 1.8:
            #             kfold_result5[train_index[i],j] = "PATH"

    # VALIDAÇÃO
    # for i in range(0, 420):
    #     for h in range([0.2, 0.6, 1, 1.4, 1.8]):


    

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