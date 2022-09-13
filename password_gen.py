import random
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_case = '0123456789'
symbols = '!@#$%^&*'

use_all = lower_case + upper_case + num_case + symbols
length_password = 8

password = ''.join(random.sample(use_all, length_password))
print(password)
