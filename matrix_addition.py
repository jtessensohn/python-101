matrix1 = [ [1, 3],
[2, 4] ]
matrix2 = [ [5, 2],
[1, 0] ]
matrixEnd = [ [0, 0],
[0, 0] ]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrixEnd[i][j] = matrix1[i][j] + matrix2[i][j]
for r in matrixEnd:
    print(r)