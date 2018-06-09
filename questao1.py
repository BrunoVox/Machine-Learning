from matrix import complete_view, lmatrix, index_matrix
import random
import numpy as np 
from sklearn.metrics.pairwise import euclidean_distances

def generate_random_prototypes(i_matrix):
    prototype_set = random.sample(list(i_matrix), 7)
    return prototype_set

def kernel_gh(inv_s, xk, gi, linha, linha_g):
    somatorio = 0
    for i in range(0, p):
        somatorio += inv_s[i] * (xk[linha, i] - gi[linha_g, i]) ** 2
    k_gh = np.exp(-0.5 * somatorio)
    return k_gh

def prototype_new():
    num = np.zeros((c,))
    den = np.zeros((c,))
    proto_result = np.zeros((c,))
    for j in range(c):
        for i in range(len(clusters)):
            if j == clusters[i]:
                num[j] += kernel_gh(hyperparameter_vector, complete_view, prototypes_matrix, i, clusters[i]) * complete_view[i, :]
                den[j] += kernel_gh(hyperparameter_vector, complete_view, prototypes_matrix, i, clusters[i])
        proto_result[j] = num[j] / den[j]
    return proto_result

def hyperparameter_new(prod, den2, i, h, s):
    temp_part = clusters[:, i]
    for part in range(0, len(temp_part)):
        if temp_part[part] == -1:
            break
        else:
            if s == 0:
                prod[h] += kernel_gh(hyperparameter_vector, complete_view, prototypes_matrix, int(temp_part[part]), i) * (complete_view[int(temp_part[part]), h] - prototypes_matrix[i, h]) ** 2
            den2[h] += kernel_gh(hyperparameter_vector, complete_view, prototypes_matrix, int(temp_part[part]), i) * (complete_view[int(temp_part[part]), s] - prototypes_matrix[i, s]) ** 2
    return prod[h], den2[s]

# INITIALIZATION

c = 7
p = 18

euc_distance = euclidean_distances(complete_view) ** 2

percentile_10 = np.percentile(euc_distance, 10)
percentile_90 = np.percentile(euc_distance, 90)
sigma_2 = (percentile_10 + percentile_90) / 2 # tril_indices numpy
gama = (1 / sigma_2) ** p
hyperparameter_vector = np.ones((p,)) * (gama ** (1 / p))

prototypes_vector = generate_random_prototypes(index_matrix)
prototypes_matrix = np.zeros((c, p))

for i in range(len(prototypes_vector)):
    for j in range(p):
        prototypes_matrix[i, j] = complete_view[int(prototypes_vector[i]), j]
# print(prototypes_matrix)
clusters = np.zeros((2100,))

factor_list = np.ravel(np.zeros((7,1)))

for i in range(len(complete_view)):
    for j in range(len(prototypes_matrix)):
        factor_list[j] = 2 * (1 - kernel_gh(hyperparameter_vector, complete_view, prototypes_matrix, i, j))
    factor_min = np.argmin(factor_list)
    clusters[i] = factor_min
print(clusters)
# PARTE FINAL DO ALGORITMO

test_sum = 1
old_hyperparameter_vector = 0
# print(hyperparameter_vector)
while test_sum != 0:
    result_prototype_new = prototype_new()
    
    for i in range(c):
        prototypes_matrix[i] = result_prototype_new[i]
    # print(prototypes_matrix)
    # CÁLCULO DO HIPERPARÂMETRO
    produtorio = np.ravel(np.zeros((18, 1)))
    denominator2 = np.ravel(np.zeros((18, 1)))

    for s in range(0, len(hyperparameter_vector)):
        print(s, "/ 18")
        for h in range(0, p):
            for i in range(0, c):
                hp_temp = hyperparameter_new(produtorio, denominator2, i, h, s)
                produtorio[h] += hp_temp[0]
                denominator2[s] += hp_temp[1]
                
        if s == 0:
            result_prod = 1
            for h in range(0, p):
                result_prod *= produtorio[h]
            # print(result_prod)
        
        hyperparameter_vector[s] = ((gama ** (1 / p)) * (result_prod ** (1 / p))) / denominator2[s]

    # test = hyperparameter_vector - old_hyperparameter_vector
    # test_sum = np.sum(test)
    # print(hyperparameter_vector)
    # old_hyperparameter_vector = hyperparameter_vector
    # if test_sum == 0:
    # print(hyperparameter_vector)

    

    # for i in range(0, len(complete_view)):
    #     for j in range(0, len(prototypes_matrix)):
    #         # print(kernel_gh(hyperparameter_vector, complete_view, prototypes_matrix, i, j))
    #         factor_list[j] = 2 * (1 - kernel_gh(hyperparameter_vector, complete_view, prototypes_matrix, i, j))
    #     factor_min = np.argmin(factor_list)
    #     for m in range(0, len(clusters)):
    #         if clusters[m, factor_min] == -1:
    #             clusters[m, factor_min] = i
    #             break
    # count = 0
    # for j in range(0, c):
    #     for i in range(0, len(clusters)):
    #         for k in range(0, len(clusters_old)):
    #             if clusters[i, j] == clusters_old[k, j]:
    #                 count += 1
    #                 break
    #             if clusters[i, j] == -1 or clusters_old[i, j] == -1:
    #                 break
    print(clusters)
