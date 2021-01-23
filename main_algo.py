from Key_generation import *
from round import *


def take_input(plaint):
    hex_plaint = input()
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


arr_of_keys = []
generate_keys(arr_of_keys)
plaint = []
take_input(plaint)
init_per(plaint)
l = plaint[:32]
r = plaint[32:]
for i in range(16):
    des_round(l, r, arr_of_keys[i])
# swap
# inverse_per
# convert to hexa