from Key_generation import *
from round import *


def take_input(plaint, hex_plaint):
    int_plaint = int(hex_plaint, 16)
    bin_plaint = bin(int_plaint)
    bin_plaint = bin_plaint[2:].zfill(64)
    plaint[:] = bin_plaint
    for i in range(len(plaint)):
        plaint[i] = int(plaint[i])


def init_per(plaint):
    ip = [57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7,
          56, 48, 40, 32, 24, 16, 8, 0,
          58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6
          ]
    temp_plaint = list(map(lambda x: plaint[x], ip))
    plaint[0:] = temp_plaint


def swap_and_inv_per(cipher):
    fp = [
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25,
        32, 0, 40, 8, 48, 16, 56, 24
    ]
    temp_cipher = list(map(lambda x: cipher[x], fp))
    cipher[:] = temp_cipher


arr_of_keys = []
generate_keys(arr_of_keys)
plaint = []
hex_plaint = input()
no_of_it = input()
for k in range(int(no_of_it)):
    take_input(plaint, hex_plaint)
    init_per(plaint)
    left = plaint[:32]
    r = plaint[32:]
    for i in range(16):
        r = des_round(left, r, arr_of_keys[i])

    final_cipher = r + left
    swap_and_inv_per(final_cipher)
    for j in range(len(final_cipher)):
        final_cipher[j] = str(final_cipher[j])
    final_str = ''.join(final_cipher)
    final_dec = int(final_str, 2)
    final_hex = hex(final_dec)
    hex_plaint = final_hex

print(final_hex[2:].upper())
