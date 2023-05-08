A = ((1, 2, 3),
     (4, 5, 6))

B = ((-1, 0),
     (0, 1),
     (1,1))

multmatriz = [[0,0],
          [0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            multmatriz[i][j] += A[i][k] * B[k][j]
for i in range(len(multmatriz)):
    multmatriz[i] = tuple(multmatriz[i])
multmatriz = tuple(multmatriz)
for i in range(len(multmatriz)):
    print(multmatriz[i])