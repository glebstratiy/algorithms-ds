import numpy as np
length = 120

#Для заданого  масиву цілих чисел (довжина > 100, генеровані випадковим чином) знайти мінімальне значення, 
#максимальне значення, впорядкувати масив ( за спаданням, за зростанням)

arr = np.random.randint(1, length, length)
arr
import numpy as np
LENGTH = 120

arr = np.random.randint(1, LENGTH, LENGTH)
arr
mn = arr[0]
mx = mn
for item in arr:
  mn = np.min([mn, item])
  mx = np.max([mx, item])

print(f'Minimun: {mn}\nMaximum: {mx}')
arr_asc = np.sort(arr)
arr_desc = np.flip(arr_asc)
print(f'Sorted array asc:{arr_asc}\n')
print(f'Sorted array desc:{arr_desc}')

"""
Minimun: 2
Maximum: 119
Sorted array asc:[  2   2   3   4   5   5   5   6   6   7   8   9  10  10  14  14  15  15
  16  18  18  19  20  22  23  24  27  27  28  28  30  30  31  32  33  33
  34  34  35  36  36  40  41  41  42  42  43  45  45  45  45  45  47  47
  47  49  53  55  55  56  57  58  58  60  62  63  64  65  65  68  73  73
  73  76  76  76  77  77  80  81  82  82  83  83  83  83  84  85  85  85
  87  88  88  91  91  91  92  92  93  95  97  97 101 102 102 102 102 103
 104 110 110 111 111 112 112 113 115 116 117 119]
 
 Sorted array desc:[119 117 116 115 113 112 112 111 111 110 110 104 103 102 102 102 102 101
  97  97  95  93  92  92  91  91  91  88  88  87  85  85  85  84  83  83
  83  83  82  82  81  80  77  77  76  76  76  73  73  73  68  65  65  64
  63  62  60  58  58  57  56  55  55  53  49  47  47  47  45  45  45  45
  45  43  42  42  41  41  40  36  36  35  34  34  33  33  32  31  30  30
  28  28  27  27  24  23  22  20  19  18  18  16  15  15  14  14  10  10
   9   8   7   6   6   5   5   5   4   3   2   2]

"""
#А) в центрі -  мінімальне (максимальне) значення, додаємо зліва – справа елементи в порядку зростання (спадання). Вивести масив.

center_arr = np.empty_like(arr)
left_el = (LENGTH - 1)//2
right_el = left_el + 1
# if for odd Length
border = 0
if LENGTH % 2 == 1:
  center_arr[left_el] = arr_asc[-1]
  left_el -= 1
  border = 1

i = LENGTH - 1 - border
while i >= 0:
  center_arr[left_el] = arr_asc[i]
  i -= 1
  left_el -= 1

  center_arr[right_el] = arr_asc[i]
  i -= 1
  right_el += 1

print(center_arr)

"""
[  1   3   4   4   4   5   5   6   8  10  10  14  14  16  19  19  20  21
  21  21  22  23  23  23  24  27  28  28  29  29  31  34  34  35  35  35
  37  38  39  39  42  42  42  44  44  45  46  47  47  48  48  49  49  49
  51  52  54  57  58  58  59  59  60  64  65  65  66  67  68  69  69  70
  70  74  76  77  78  78  79  79  80  80  81  82  82  83  85  85  86  87
  87  87  91  93  93  93  94  95  96  96  97  97  97 101 103 103 104 106
 107 107 109 109 111 112 112 113 114 114 116 117]
"""

#Б) сформувати масив – максимальне, мінімальне, максимальне (з тих, що залишились), мінімальне, … Вивести масив.
updown = np.empty(LENGTH, dtype = type(LENGTH))
left_ind = 0
right_ind = LENGTH - 1
i = 0
while i < LENGTH:
  updown[i] = arr_asc[right_ind]
  i += 1
  right_ind -= 1
  updown[i] = arr_asc[left_ind]
  i += 1
  left_ind += 1

print(updown)

"""
[119   2 117   2 116   3 115   4 113   5 112   5 112   5 111   6 111   6
 110   7 110   8 104   9 103  10 102  10 102  14 102  14 102  15 101  15
  97  16  97  18  95  18  93  19  92  20  92  22  91  23  91  24  91  27
  88  27  88  28  87  28  85  30  85  30  85  31  84  32  83  33  83  33
  83  34  83  34  82  35  82  36  81  36  80  40  77  41  77  41  76  42
  76  42  76  43  73  45  73  45  73  45  68  45  65  45  65  47  64  47
  63  47  62  49  60  53  58  55  58  55  57  56]
"""

#В) сформувати масив – елементи з парними номерами спадають, потів – елементи з непарними номерами зростають. Вивести масив.

arr_odd = np.array([arr[i] for i in range(1, LENGTH, 2)])
arr_odd.sort()
arr_even = np.array([arr[j] for j in range(0, LENGTH, 2)])
arr_even = np.flip(np.sort(arr_even))
res = np.concatenate((arr_even, arr_odd))
res

"""
array([119, 115, 113, 112, 111, 110, 110, 104, 102, 102, 102, 101,  97,
        95,  93,  92,  91,  91,  85,  85,  83,  83,  83,  82,  82,  81,
        80,  77,  77,  73,  73,  60,  58,  58,  57,  56,  55,  55,  49,
        47,  45,  45,  41,  34,  33,  32,  28,  27,  24,  18,  15,  14,
        10,   9,   8,   6,   5,   5,   4,   3,   2,   2,   5,   6,   7,
        10,  14,  15,  16,  18,  19,  20,  22,  23,  27,  28,  30,  30,
        31,  33,  34,  35,  36,  36,  40,  41,  42,  42,  43,  45,  45,
        45,  47,  47,  53,  62,  63,  64,  65,  65,  68,  73,  76,  76,
        76,  83,  84,  85,  87,  88,  88,  91,  92,  97, 102, 103, 111,
       112, 116, 117])
"""
