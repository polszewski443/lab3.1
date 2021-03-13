def ntywyrazgeom(a1, n, q):
    return a1 * q ** (n - 1)


def sumanpgeom(a1, n, q):
    if q != 1:
        return a1 * ((1 - q ** n) / (1 - q))
    return a1 * n
