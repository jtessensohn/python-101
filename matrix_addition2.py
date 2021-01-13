matrix1 = [ [2, 4, 6],
[3, 5, 7] ]
matrix2 = [ [3, 5, 7],
[2, 4, 6] ]
matrixEnd = [ [0, 0, 0], 
[0, 0, 0] ]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrixEnd[i][j] = matrix1[i][j] + matrix2[i][j]
for r in matrixEnd:
    print(r)