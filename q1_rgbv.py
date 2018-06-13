from matrix import lmatrix, index_matrix, kcm_check, rgb_view
import random
import numpy as np 
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import adjusted_rand_score

def generate_random_prototypes(i_matrix):
    prototype_set = random.sample(list(i_matrix), 7)
    return prototype_set

def kernel_gh(inv_s, xk, gi, linha, linha_g):
    somatorio = 0
    for i in range(p):
        somatorio += inv_s[i] * (xk[linha, i] - gi[linha_g, i]) ** 2
    k_gh = np.exp(-0.5 * somatorio)
    return k_gh

def prototype_new():
    num = np.zeros((c,)).tolist()
    den = np.zeros((c,)).tolist()
    proto_result = np.zeros((c,)).tolist()
    for i in range(c):
        for k in range(len(clusters)):
            if clusters[k] == 0 and i == 0:
                num[i] += np.dot(kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i), rgb_view[k])
                den[i] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i)
            elif clusters[k] == 1 and i == 1:
                num[i] += np.dot(kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i), rgb_view[k])
                den[i] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i)
            elif clusters[k] == 2 and i == 2:
                num[i] += np.dot(kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i), rgb_view[k])
                den[i] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i)
            elif clusters[k] == 3 and i == 3:
                num[i] += np.dot(kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i), rgb_view[k])
                den[i] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i)
            elif clusters[k] == 4 and i == 4:
                num[i] += np.dot(kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i), rgb_view[k])
                den[i] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i)
            elif clusters[k] == 5 and i == 5:
                num[i] += np.dot(kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i), rgb_view[k])
                den[i] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i)
            elif clusters[k] == 6 and i == 6:
                num[i] += np.dot(kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i), rgb_view[k])
                den[i] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i)
        proto_result[i] = num[i] / den[i]
    return proto_result

def hyperparameter_new(prod, den2):
    for j in range(p):
        for h in range(p):
            for i in range(c): 
                for k in range(len(clusters)):
                    if clusters[k] == 0 and i == 0:
                        if j == 0:
                            prod[h] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, h] - prototypes_matrix[i, h]) ** 2
                        if h == 0:    
                            den2[j] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, j] - prototypes_matrix[i, j]) ** 2
                    elif clusters[k] == 1 and i == 1:
                        if j == 0:
                            prod[h] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, h] - prototypes_matrix[i, h]) ** 2
                        if h == 0:    
                            den2[j] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, j] - prototypes_matrix[i, j]) ** 2
                    elif clusters[k] == 2 and i == 2:
                        if j == 0:
                            prod[h] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, h] - prototypes_matrix[i, h]) ** 2
                        if h == 0:    
                            den2[j] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, j] - prototypes_matrix[i, j]) ** 2
                    elif clusters[k] == 3 and i == 3:
                        if j == 0:
                            prod[h] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, h] - prototypes_matrix[i, h]) ** 2
                        if h == 0:    
                            den2[j] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, j] - prototypes_matrix[i, j]) ** 2
                    elif clusters[k] == 4 and i == 4:
                        if j == 0:
                            prod[h] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, h] - prototypes_matrix[i, h]) ** 2
                        if h == 0:    
                            den2[j] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, j] - prototypes_matrix[i, j]) ** 2
                    elif clusters[k] == 5 and i == 5:
                        if j == 0:
                            prod[h] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, h] - prototypes_matrix[i, h]) ** 2
                        if h == 0:    
                            den2[j] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, j] - prototypes_matrix[i, j]) ** 2
                    elif clusters[k] == 6 and i == 6:
                        if j == 0:
                            prod[h] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, h] - prototypes_matrix[i, h]) ** 2
                        if h == 0:    
                            den2[j] += kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i) * (rgb_view[k, j] - prototypes_matrix[i, j]) ** 2
    return prod, den2

def objective_function():
    dec = 0
    for i in range(c):
        for k in range(len(clusters)):
            if i == 0 and clusters[k] == 0:
                dec += 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i))
            elif i == 1 and clusters[k] == 1:
                dec += 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i))
            elif i == 2 and clusters[k] == 2:
                dec += 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i))
            elif i == 3 and clusters[k] == 3:
                dec += 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i))
            elif i == 4 and clusters[k] == 4:
                dec += 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i))
            elif i == 5 and clusters[k] == 5:
                dec += 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i))
            elif i == 6 and clusters[k] == 6:
                dec += 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, k, i))
    return dec

# INITIALIZATION

c = 7
p = 10

results_prototypes = np.zeros((700, 10))
results_objects = np.zeros((100, 2100))
results_hyperparameter = np.zeros((100, 10))
results_ari = np.zeros((100, 1))

euc_distance = euclidean_distances(rgb_view) ** 2
euc_distance_adjusted = np.tril(euc_distance)
euc_distance_adjusted = (euc_distance_adjusted).flatten()
to_delete = []
for i in range(len(euc_distance_adjusted)):
    if euc_distance_adjusted[i] == 0:
        to_delete.append(i)
euc_distance_adjusted = np.delete(euc_distance_adjusted, to_delete)

percentile_10 = np.percentile(euc_distance_adjusted, 10)
percentile_90 = np.percentile(euc_distance_adjusted, 90)
sigma_2 = (percentile_10 + percentile_90) / 2
gama = (1 / sigma_2) ** p

# PARTE FINAL DO ALGORITMO

for n in range(100):
    test = 1

    hyperparameter_vector = np.ones((p,)) * (gama ** (1 / p))
    prototypes_vector = generate_random_prototypes(index_matrix)
    prototypes_matrix = np.zeros((c, p))

    for i in range(len(prototypes_vector)):
        for j in range(p):
            prototypes_matrix[i, j] = rgb_view[int(prototypes_vector[i]), j]

    factor_list = np.ravel(np.zeros((7,1)))
    clusters = np.zeros((2100,))
    for i in range(len(rgb_view)):
        for j in range(c):
            factor_list[j] = 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, i, j))
        factor_min = np.argmin(factor_list)
        clusters[i] = factor_min

    count = 0
    while test == 1:
        count += 1
        print("Iteration", count)
        of_old = objective_function()
        print("J:", of_old)

        result_prototype_new = prototype_new()

        for i in range(c):
            for j in range(p):
                prototypes_matrix[i, j] = (np.array(result_prototype_new))[i, 0, j]

        produtorio = np.zeros((p,))
        denominator2 = np.zeros((p,))

        hp_temp = hyperparameter_new(produtorio, denominator2)
        produtorio = hp_temp[0]
        denominator2 = hp_temp[1]

        result_prod = 1
        for i in range(p):
            result_prod *= produtorio[i]

        for j in range(p):
            hyperparameter_vector[j] = ((gama ** (1 / p)) * (result_prod ** (1 / p))) / denominator2[j]

        for i in range(len(rgb_view)):
            for j in range(len(prototypes_matrix)):
                factor_list[j] = 2 * (1 - kernel_gh(hyperparameter_vector, rgb_view, prototypes_matrix, i, j))
            factor_min = np.argmin(factor_list)
            clusters[i] = factor_min
        
        of = objective_function()
        print("J:", of)

        test = 0

        if of != of_old:
            test = 1

        if of == of_old:
            score = adjusted_rand_score(kcm_check, clusters)
            print("ARI:", score)

    for i in range(n, n + 1):
        for j in range(2100):
            results_objects[i, j] = clusters[j]

    for i in range((n * 7), ((n * 7) + 7)):
        for j in range(p):
            if i == (n * 7):
                results_prototypes[i, j] = prototypes_matrix[0, j]
            elif i == ((n * 7) + 1):
                results_prototypes[i, j] = prototypes_matrix[1, j]
            elif i == ((n * 7) + 2):
                results_prototypes[i, j] = prototypes_matrix[2, j]
            elif i == ((n * 7) + 3):
                results_prototypes[i, j] = prototypes_matrix[3, j]
            elif i == ((n * 7) + 4):
                results_prototypes[i, j] = prototypes_matrix[4, j]
            elif i == ((n * 7) + 5):
                results_prototypes[i, j] = prototypes_matrix[5, j]
            elif i == ((n * 7) + 6):
                results_prototypes[i, j] = prototypes_matrix[6, j]

    for i in range(n, n + 1):
        for j in range(p):
            results_hyperparameter[i, j] = hyperparameter_vector[j]

    for i in range(n, n + 1):
        for j in range(1):
            results_ari[i, j] = score

    np.savetxt("clusters_q1_rgbv.txt", results_objects, fmt="%.0f", delimiter=",")
    np.savetxt("prototypes_q1_rgbv.txt", results_prototypes, delimiter=",")
    np.savetxt("hyperparameter_q1_rgbv.txt", results_hyperparameter, delimiter=",")
    np.savetxt("ari_q1_rgbv.txt", results_ari)
    