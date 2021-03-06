"""
if it is not python, i will get mad to understand hash
"""
import hashlib

secret = 'reyedfim'

def parse_letter(letters):
    password = ''
    for i in range(10 ** 99):
        mix = hashlib.md5((letters + str(i)).encode('utf-8')).hexdigest()
        if mix.startswith('00000'):
            password += mix[5]
        if len(password) == 8:
            return password

# assert parse_letter('abc') == '18f47a30'

# print(parse_letter(secret))

def get_password(letters):
    password = ['-'] * 8
    for i in range(10 ** 99):
        mix = hashlib.md5((letters + str(i)).encode('utf-8')).hexdigest()
        if mix.startswith('00000'):
            index = int(mix[5], 16)
            if index < 8 and password[index] is '-':
                password[index] = mix[6]
                print(password)
            if '-' not in password:
                return password

print('password is ', ''.join(get_password(secret)))
