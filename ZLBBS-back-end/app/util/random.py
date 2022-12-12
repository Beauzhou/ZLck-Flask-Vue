import string, random


def rand():
    str1 = string.digits + string.ascii_letters
    str2 = ''
    for i in range(6):
        str2 = str2 + random.choice(str1)
    return str2
