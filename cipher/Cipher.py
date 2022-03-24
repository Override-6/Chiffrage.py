import random


def key_random(key):
    seed = 0
    for c in key:
        if isinstance(c, type('')):
            c = ord(c)
        seed += c
    return random.Random(seed)


def encrypt(value, key, key_idx=0):
    buff = [0] * len(value)
    r = key_random(key)
    idx = 0
    for i in value:
        buff[idx] = (i ^ r.randint(0, 255)) % 2
        idx += 1
        key_idx += 1
    return buff
