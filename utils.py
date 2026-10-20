import random
import hashlib
import string
from functools import reduce


ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase  # 0-9A-Za-z

def encode(num: int) -> str:
    if num < 0:
        raise ValueError("Base62 encodes non-negative integers")
    if num == 0:
        return ALPHABET[0]
    out = []
    while num:
        num, rem = divmod(num, 62)
        out.append(ALPHABET[rem])
    return "".join(reversed(out))


def generate_short_id(long_url):
    encoded = hashlib.sha256(long_url.encode())
    hex_digits = reduce(lambda x, y: str(x)+str(y), map(ord, encoded.hexdigest()[:8]))
    short_id = encode(int(hex_digits))
    return short_id



