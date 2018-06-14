import random
from matrix import lmatrix
import numpy as np

def random_parts():

    part_matrix = np.zeros((210, 10))
    valid_part = np.zeros((420, 1))
    train_part = np.zeros((7 * 210, 1))
    grass_vector, grass_index = np.zeros((int(len(lmatrix)/7),1)), 0
    window_vector, window_index = np.zeros((int(len(lmatrix)/7),1)), 0
    cement_vector, cement_index = np.zeros((int(len(lmatrix)/7),1)), 0
    brickface_vector, brickface_index = np.zeros((int(len(lmatrix)/7),1)), 0
    sky_vector, sky_index = np.zeros((int(len(lmatrix)/7),1)), 0
    foliage_vector, foliage_index = np.zeros((int(len(lmatrix)/7),1)), 0
    path_vector, path_index = np.zeros((int(len(lmatrix)/7),1)), 0

    for i in range(0, len(lmatrix)):
        if lmatrix[i] == "GRASS":
            grass_vector[grass_index] = i
            grass_index += 1
        if lmatrix[i] == "WINDOW":
            window_vector[window_index] = i
            window_index += 1
        if lmatrix[i] == "CEMENT":
            cement_vector[cement_index] = i
            cement_index += 1
        if lmatrix[i] == "BRICKFACE":
            brickface_vector[brickface_index] = i
            brickface_index += 1
        if lmatrix[i] == "SKY":
            sky_vector[sky_index] = i
            sky_index += 1
        if lmatrix[i] == "FOLIAGE":
            foliage_vector[foliage_index] = i
            foliage_index += 1
        if lmatrix[i] == "PATH":
            path_vector[path_index] = i
            path_index += 1

    # SORTEIO DAS PARTIÇÕES

    for j in range(0, 10):
        random_grass = random.sample(list(np.ravel(grass_vector)), 30)
        for i in range(0, len(random_grass)):
            part_matrix[i, j] = random_grass[i]
        grass_vector = np.setdiff1d(grass_vector, random_grass)

        random_window = random.sample(list(np.ravel(window_vector)), 30)
        for i in range(30, len(random_window) + 30):
            part_matrix[i, j] = random_window[i - 30]
        window_vector = np.setdiff1d(window_vector, random_window)

        random_cement = random.sample(list(np.ravel(cement_vector)), 30)
        for i in range(60, len(random_cement) + 60):
            part_matrix[i, j] = random_cement[i - 60]
        cement_vector = np.setdiff1d(cement_vector, random_cement)

        random_brickface = random.sample(list(np.ravel(brickface_vector)), 30)
        for i in range(90, len(random_brickface) + 90):
            part_matrix[i, j] = random_brickface[i - 90]
        brickface_vector = np.setdiff1d(brickface_vector, random_brickface)

        random_sky = random.sample(list(np.ravel(sky_vector)), 30)
        for i in range(120, len(random_sky) + 120):
            part_matrix[i, j] = random_sky[i - 120]
        sky_vector = np.setdiff1d(sky_vector, random_sky)

        random_foliage = random.sample(list(np.ravel(foliage_vector)), 30)
        for i in range(150, len(random_foliage) + 150):
            part_matrix[i, j] = random_foliage[i - 150]
        foliage_vector = np.setdiff1d(foliage_vector, random_foliage)

        random_path = random.sample(list(np.ravel(path_vector)), 30)
        for i in range(180, len(random_path) + 180):
            part_matrix[i, j] = random_path[i - 180]
        path_vector = np.setdiff1d(path_vector, random_path)

    # A COLUNA 0 CORRESPONDE À PARTIÇÃO DE TESTE
    # AS COLUNAS 1 E 2 CORRESPONDEM À PARTIÇÃO DE VALIDAÇÃO
    # AS COLUNAS DE 3 A 9 CORRESPONDEM À PARTIÇÃO DE TREINAMENTO

    test_part_1 = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))
    test_part_2 = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))
    test_part_3 = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))
    test_part_4 = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))
    test_part_5 = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))
    test_part_6 = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))
    test_part_7 = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))
    test_part_8 = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))
    test_part_9 = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))
    test_part_10 = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))

    # valid_part_1 = np.ravel(np.reshape(part_matrix[:,1:3], (1, 420)))
    # valid_part_2 = np.ravel(np.reshape(part_matrix[:,2:4], (1, 420)))
    # valid_part_3 = np.ravel(np.reshape(part_matrix[:,3:5], (1, 420)))
    # valid_part_4 = np.ravel(np.reshape(part_matrix[:,4:6], (1, 420)))
    # valid_part_5 = np.ravel(np.reshape(part_matrix[:,5:7], (1, 420)))
    # valid_part_6 = np.ravel(np.reshape(part_matrix[:,6:8], (1, 420)))
    # valid_part_7 = np.ravel(np.reshape(part_matrix[:,7:9], (1, 420)))
    # valid_part_8 = np.ravel(np.reshape(part_matrix[:,8:0], (1, 420)))
    # valid_part_9 = np.ravel(np.reshape(part_matrix[:,9:1], (1, 420)))
    # valid_part_10 = np.ravel(np.reshape(part_matrix[:,0:2], (1, 420)))

    # test_part = []

    # test_part.append(test_part_1)
    # test_part.append(test_part_2)
    # test_part.append(test_part_3)
    # test_part.append(test_part_4)
    # test_part.append(test_part_5)
    # test_part.append(test_part_6)
    # test_part.append(test_part_7)
    # test_part.append(test_part_8)
    # test_part.append(test_part_9)
    # test_part.append(test_part_10)

    # total_part = []

    # for i in range(2100):
    #     total_part.append(i)
    
    # for i in range(len(test_part_1)):
    #     aux = total_part
    #     aux.remove(test_part_1[i])

    # valid_part_1 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_1.append(aux[i])

    # train_part_1 = aux

    # for i in range(len(test_part_2)):
    #     aux = total_part
    #     aux.remove(test_part_2[i])

    # valid_part_2 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_2.append(aux[i])

    # train_part_2 = aux

    # for i in range(len(test_part_3)):
    #     aux = total_part
    #     aux.remove(test_part_3[i])

    # valid_part_3 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_3.append(aux[i])

    # train_part_3 = aux

    # for i in range(len(test_part_4)):
    #     aux = total_part
    #     aux.remove(test_part_4[i])

    # valid_part_4 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_4.append(aux[i])

    # train_part_4 = aux

    # for i in range(len(test_part_5)):
    #     aux = total_part
    #     aux.remove(test_part_5[i])

    # valid_part_5 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_5.append(aux[i])

    # train_part_5 = aux

    # for i in range(len(test_part_6)):
    #     aux = total_part
    #     aux.remove(test_part_6[i])

    # valid_part_6 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_6.append(aux[i])

    # train_part_6 = aux

    # for i in range(len(test_part_7)):
    #     aux = total_part
    #     aux.remove(test_part_7[i])

    # valid_part_7 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_7.append(aux[i])

    # train_part_7 = aux

    # for i in range(len(test_part_8)):
    #     aux = total_part
    #     aux.remove(test_part_8[i])

    # valid_part_8 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_8.append(aux[i])

    # train_part_8 = aux

    # for i in range(len(test_part_9)):
    #     aux = total_part
    #     aux.remove(test_part_9[i])

    # valid_part_9 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_9.append(aux[i])

    # train_part_9 = aux

    # for i in range(len(test_part_10)):
    #     aux = total_part
    #     aux.remove(test_part_10[i])

    # valid_part_10 = []
    # random.shuffle(aux)
    # for i in range(420):
    #     valid_part_10.append(aux[i])

    # train_part_10 = aux

    # train_part = np.zeros((10,))

    # for i in range(10):
    #     train_part[i] = train_part_1

       


    for j in range(1,3):
        for i in range(0, len(part_matrix)):
            valid_part[i + (j - 1) * len(part_matrix)] = part_matrix[i, j]

    valid_part_1 = np.ravel(valid_part)

    for j in range(3,10):
        for i in range(0, len(part_matrix)):
            train_part[i + (j - 3) * len(part_matrix)] = part_matrix[i, j]

    train_part = np.ravel(train_part)

    return test_part, valid_part, train_part

# train_parts_bay = []
# train_parts = []
# valid_parts = []
# test_parts = []

# for i in range(0, 30):
#     train_parts_bay = np.hstack()
#     train_parts.append(random_parts()[2])
#     valid_parts.append(random_parts()[1])
#     test_parts.append(random_parts()[0])

# print(train_parts_bay)