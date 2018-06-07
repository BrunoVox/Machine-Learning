#f = open("C:/Users/bruno/OneDrive/Documents/ProjetosCC/Projeto AM/dados.txt",'r')
#print(f.readlines()[5])

w, h = 20, 2100
matrix = [[0 for x in range(w)] for y in range(h)]


with open("C:/Users/bruno/OneDrive/Documents/ProjetosCC/Projeto AM/dados.txt", 'r') as f:
    for i in range(0, len(f.readlines())):

        f = open("C:/Users/bruno/OneDrive/Documents/ProjetosCC/Projeto AM/dados.txt",'r')
        matrix[i] = f.readlines()[i].split(",")
        # for k in range(0, len(f.readlines()[k].split(","))):
        #     matrix[i][k] = f.readlines()[k].split
            
print(matrix)

a = 0
for i in range(1, 19):
    a += float(matrix[5][i])

a = a/19
print(a)





#print(len(f.readlines()))

#file = open("C:/Users/bruno/OneDrive/Documents/ProjetosCC/Projeto AM/dados.txt", "r")
#for line in file:
#    print(line),