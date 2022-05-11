def determinant(matrix, size):
  value = 0

  if size > 2:
    for i in range(size):
      matrix2 = []
      sign = (-1)**(i)

      for j in range(1, size):
        row = []
        for k in range(size):
          if k == i:
            continue
          row.append(matrix[j][k])
        matrix2.append(row)
      value += sign*matrix[0][i]*determinant(matrix2, size-1)

    return value

  elif size == 2:
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
  elif size == 1:
    return matrix[0][0]
  
  return 0

def det(matrix):
  rowLen = len(matrix[0])
  columnLen = len(matrix)

  if rowLen != columnLen:
    return 0

  return determinant(matrix, rowLen)
  

tab = [[1,3,0,-1],[0,2,1,3],[3,1,2,1],[-1,2,0,3]]
print(det(tab))