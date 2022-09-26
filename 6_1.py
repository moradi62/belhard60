#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int

def dec_to_bin(i: int):
    bit_res = 0
    ste = 1
    while i > 0:
        temp = i % 2
        bit_res = bit_res + (temp * ste)
        ste = ste * 10
        i = int(i / 2)
    return bit_res


def bin_to_dec(b: int):
    dis_res = 0
    ste = 0
    temp = 0
    while b != 0:
        temp = b % 10
        if temp > 0:
            dis_res += (2**ste)
        ste += 1
        b = b//10
    return dis_res

num = int(input('Напишите цифру: '))

print(f'Двоичное число {num} равно {dec_to_bin(num)}')
print(f'Десятичное число {dec_to_bin(num)} равно {bin_to_dec(dec_to_bin(num))}')
