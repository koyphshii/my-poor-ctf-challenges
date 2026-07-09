from sage.all import *
from Crypto.Util.number import *
from FLAG import flag
import os
import hashlib


def generate_custom_prime():
    while True:
        low_bits        = str(getRandomNBitInteger(140)).encode().hex()[2:]
        high_bits       = hex(getRandomNBitInteger(100))[2:]
        prime_candidate = int(high_bits + low_bits, 16)
        if isPrime(prime_candidate):
            return prime_candidate


moduli = []
for _ in range(10_000):
    pp = generate_custom_prime()
    qq = generate_custom_prime()
    moduli.append(pp * qq)


curve_prime = 2**255 - 19
curve_a = 19298681539552699237261830834781317975544997444273427339909597334573241639236
curve_b = 55751746669818908907645289078257140818241103727901012315294400837956729358436

field = GF(curve_prime)
curve = EllipticCurve([field(curve_a), field(curve_b)])

while True:
    seed = os.urandom(64)
    x1   = field(bytes_to_long(seed[:32]))
    x2   = field(bytes_to_long(seed[32:]))
    try:
        point_A = curve.lift_x(x1)
        point_B = curve.lift_x(x2)
        break
    except ValueError:
        continue


def derive_modulus_index(key_bytes: bytes) -> int:
    digest = hashlib.sha256(key_bytes).digest()
    return (int.from_bytes(digest, 'big') * 10_000) >> 256


modulus    = moduli[derive_modulus_index(seed)]
public_exp = 0x10001
ciphertext = pow(bytes_to_long(flag), public_exp, modulus)

with open("out.txt", "w") as f:
    f.write(f"moduli = {moduli}\n")
    f.write(f"ciphertext = {ciphertext}\n")
    f.write(f"A + B = {point_A + point_B}\n")
    f.write(f"A - B = {point_A - point_B}\n")
