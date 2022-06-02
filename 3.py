#Трьохвимірний масив. Для заданого  масиву цілих чисел (довжина > 5*5*5, генеровані випадковим чином) знайти мінімальне значення,
#максимальне значення, впорядкувати масив  за зростанням по осі OX, потім по осі OY, OZ. Вивести результати.

import numpy as np

a = np.random.randint(1, 25, (5, 5, 5))
a

"""
array([[[19,  5, 16, 21, 23],
        [ 6, 17,  7, 22,  4],
        [ 3, 17, 18,  4,  7],
        [ 3, 11, 15, 18, 11],
        [12, 10, 20,  6, 14]],

       [[ 8,  1,  4,  3,  1],
        [13,  5,  5, 18, 24],
        [18, 10, 17, 17,  6],
        [ 3,  2,  5,  5,  7],
        [ 2,  9,  9, 16,  5]],

       [[ 9,  3,  8,  7, 11],
        [17,  3,  6,  8, 12],
        [ 7, 24, 15,  7,  6],
        [ 6, 15, 20,  8, 15],
        [10, 14,  2, 21, 22]],

       [[18,  9,  6, 20,  6],
        [15,  9, 20, 13, 21],
        [24, 14,  1, 16,  4],
        [15, 17, 21, 21, 17],
        [18, 13, 18,  9,  1]],

       [[21, 15,  6,  7, 16],
        [11,  8, 16, 22,  4],
        [17,  6,  9, 14,  5],
        [ 8,  9, 11,  6,  9],
        [20, 17, 23, 11,  2]]])

"""

mn = a[0][0][0]
mx = mn
for x in a:
  for y in x:
    for item in y:
      if mn > item:
        mn = item
      if mx < item:
        mx = item
print(f'Minimun: {mn}\nMaximum: {mx}')

"""
Minimun: 1
Maximum: 24
"""

a1 = np.sort(a, 0)
a2 = np.sort(a, 1)
a3 = np.sort(a, 2)

a1

"""
array([[[ 8,  1,  4,  3,  1],
        [ 6,  3,  5,  8,  4],
        [ 3,  6,  1,  4,  4],
        [ 3,  2,  5,  5,  7],
        [ 2,  9,  2,  6,  1]],

       [[ 9,  3,  6,  7,  6],
        [11,  5,  6, 13,  4],
        [ 7, 10,  9,  7,  5],
        [ 3,  9, 11,  6,  9],
        [10, 10,  9,  9,  2]],

       [[18,  5,  6,  7, 11],
        [13,  8,  7, 18, 12],
        [17, 14, 15, 14,  6],
        [ 6, 11, 15,  8, 11],
        [12, 13, 18, 11,  5]],

       [[19,  9,  8, 20, 16],
        [15,  9, 16, 22, 21],
        [18, 17, 17, 16,  6],
        [ 8, 15, 20, 18, 15],
        [18, 14, 20, 16, 14]],

       [[21, 15, 16, 21, 23],
        [17, 17, 20, 22, 24],
        [24, 24, 18, 17,  7],
        [15, 17, 21, 21, 17],
        [20, 17, 23, 21, 22]]])

"""

a2

"""
array([[[ 3,  5,  7,  4,  4],
        [ 3, 10, 15,  6,  7],
        [ 6, 11, 16, 18, 11],
        [12, 17, 18, 21, 14],
        [19, 17, 20, 22, 23]],

       [[ 2,  1,  4,  3,  1],
        [ 3,  2,  5,  5,  5],
        [ 8,  5,  5, 16,  6],
        [13,  9,  9, 17,  7],
        [18, 10, 17, 18, 24]],

       [[ 6,  3,  2,  7,  6],
        [ 7,  3,  6,  7, 11],
        [ 9, 14,  8,  8, 12],
        [10, 15, 15,  8, 15],
        [17, 24, 20, 21, 22]],

       [[15,  9,  1,  9,  1],
        [15,  9,  6, 13,  4],
        [18, 13, 18, 16,  6],
        [18, 14, 20, 20, 17],
        [24, 17, 21, 21, 21]],

       [[ 8,  6,  6,  6,  2],
        [11,  8,  9,  7,  4],
        [17,  9, 11, 11,  5],
        [20, 15, 16, 14,  9],
        [21, 17, 23, 22, 16]]])
"""

a3

"""
array([[[ 5, 16, 19, 21, 23],
        [ 4,  6,  7, 17, 22],
        [ 3,  4,  7, 17, 18],
        [ 3, 11, 11, 15, 18],
        [ 6, 10, 12, 14, 20]],

       [[ 1,  1,  3,  4,  8],
        [ 5,  5, 13, 18, 24],
        [ 6, 10, 17, 17, 18],
        [ 2,  3,  5,  5,  7],
        [ 2,  5,  9,  9, 16]],

       [[ 3,  7,  8,  9, 11],
        [ 3,  6,  8, 12, 17],
        [ 6,  7,  7, 15, 24],
        [ 6,  8, 15, 15, 20],
        [ 2, 10, 14, 21, 22]],

       [[ 6,  6,  9, 18, 20],
        [ 9, 13, 15, 20, 21],
        [ 1,  4, 14, 16, 24],
        [15, 17, 17, 21, 21],
        [ 1,  9, 13, 18, 18]],

       [[ 6,  7, 15, 16, 21],
        [ 4,  8, 11, 16, 22],
        [ 5,  6,  9, 14, 17],
        [ 6,  8,  9,  9, 11],
        [ 2, 11, 17, 20, 23]]])
"""

