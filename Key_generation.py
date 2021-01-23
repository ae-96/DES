def take_input(key):
    hex_key = input()
    int_key = int(hex_key, 16)
    bin_key = bin(int_key)
    bin_key = bin_key[2:].zfill(64)
    key[:] = bin_key
    for i in range(len(key)) :
        key[i]= int(key[i])



def pc1(key):
    pc1 = [56, 48, 40, 32, 24, 16, 8,
           0, 57, 49, 41, 33, 25, 17,
           9, 1, 58, 50, 42, 34, 26,
           18, 10, 2, 59, 51, 43, 35,
           62, 54, 46, 38, 30, 22, 14,
           6, 61, 53, 45, 37, 29, 21,
           13, 5, 60, 52, 44, 36, 28,
           20, 12, 4, 27, 19, 11, 3
           ]
    temp_key = list(map(lambda x: key[x], pc1))
    del key[55:]
    key[0:] = temp_key


def pc2(key):
    pc2 = [
        13, 16, 10, 23, 0, 4,
        2, 27, 14, 5, 20, 9,
        22, 18, 11, 3, 25, 7,
        15, 6, 26, 19, 12, 1,
        40, 51, 30, 36, 46, 54,
        29, 39, 50, 44, 32, 47,
        43, 48, 38, 55, 33, 52,
        45, 41, 49, 35, 28, 31
    ]
    temp_key = list(map(lambda x: key[x], pc2))
    del key[47:]
    key[0:] = temp_key


def pc2_for_all_keys(arr_of_keys):
    for i in arr_of_keys:
        pc2(i)


def left_rotate_for_all_keys(key, arr_of_keys):
    left_rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    i = 0
    L = key[:28]
    R = key[28:]
    while i < 16:
        j = 0
        while j < left_rotations[i]:
            L.append(L[0])
            del L[0]
            R.append(R[0])
            del R[0]
            j += 1

        arr_of_keys.append(L + R)

        i += 1


def generate_keys(arr_of_keys):
    key = []
    take_input(key)
    pc1(key)
    left_rotate_for_all_keys(key, arr_of_keys)
    pc2_for_all_keys(arr_of_keys)


