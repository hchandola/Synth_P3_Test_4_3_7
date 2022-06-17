from typing import List

def sat197(z: str, x="-8142432/763083", y="66/-13474", max_len=18):
    [[a, b], [c, d], [u, v]] = [[int(n) for n in s.split("/")] for s in [x, y, z]]
    return a * c * v == b * d * u and len(z) <= max_len
def sol197(x="-8142432/763083", y="66/-13474", max_len=18):
    """Write x * y as the shortest equivalent fraction using at most max_len chars

    x="-2/3", y="-3/8", max_len=3 => "1/4"
    """
    [[a, b], [c, d]] = [[int(n) for n in s.split("/")] for s in [x, y]]
    num, den = a * c, b * d
    if num < 0 and den < 0:
        num, den = -num, -den
    if num == 0:
        return "0/1"

    def gcd(a, b):
        a, b = min(a, b), max(a, b)
        if b % a == 0:
            return a
        return gcd(b % a, a)

    d = gcd(abs(num), abs(den))
    return f'{num // d}/{den // d}'
# assert sat197(sol197())
