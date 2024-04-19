a = [[1, 2, 11, 4],
     [4, 15, 2, 1],
     [5, 6, 7, 8],
     [12, 13, 14, 15]]

count = 0  

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] > 10:
            count += 1

print(f"A matriz 'a' contém {count} valores maiores que 10.")
