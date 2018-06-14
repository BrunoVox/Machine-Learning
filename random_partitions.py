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


    test_part = np.zeros((10, 210))
    valid_part = np.zeros((10, 420))
    train_part = np.zeros((10, 1470))
    for i in range(10):
        for j in range(210):
            if i == 0:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]
                
                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]

            elif i == 1:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]

            if i == 2:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]

            if i == 3:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]

            if i == 4:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]

            if i == 5:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]

            if i == 6:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]

            if i == 7:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]

            if i == 8:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,9], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]

            if i == 9:
                test_part[i,j] = np.ravel(np.reshape(part_matrix[:,i], (1, 210)))[j]

                valid_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,0], (1, 210)))[j]
                valid_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]

                train_part[i,j+0*210] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]
                train_part[i,j+1*210] = np.ravel(np.reshape(part_matrix[:,3], (1, 210)))[j]
                train_part[i,j+2*210] = np.ravel(np.reshape(part_matrix[:,4], (1, 210)))[j]
                train_part[i,j+3*210] = np.ravel(np.reshape(part_matrix[:,5], (1, 210)))[j]
                train_part[i,j+4*210] = np.ravel(np.reshape(part_matrix[:,6], (1, 210)))[j]
                train_part[i,j+5*210] = np.ravel(np.reshape(part_matrix[:,7], (1, 210)))[j]
                train_part[i,j+6*210] = np.ravel(np.reshape(part_matrix[:,8], (1, 210)))[j]
            
            


    # valid_part = np.matrix((10, 420))
    # for i in range(10):
    #     if i == 0:
    #         for j in range(210):
    #             valid_part[1,j] = np.ravel(np.reshape(part_matrix[:,1], (1, 210)))[j]
    #             valid_part[2,j] = np.ravel(np.reshape(part_matrix[:,2], (1, 210)))[j]

#     valid_part = np.ravel(valid_part)

#     for j in range(3,10):
#         for i in range(0, len(part_matrix)):
#             train_part[i + (j - 3) * len(part_matrix)] = part_matrix[i, j]

#     train_part = np.ravel(train_part)

    return test_part, valid_part, train_part

# # train_parts_bay = []
# # train_parts = []
# # valid_parts = []
# # test_parts = []

# # for i in range(0, 30):
# #     train_parts_bay = np.hstack()
# #     train_parts.append(random_parts()[2])
# #     valid_parts.append(random_parts()[1])
# #     test_parts.append(random_parts()[0])

# # print(train_parts_bay)

# a = random_parts()

# print(a[0])
# print(np.shape(a[0]))