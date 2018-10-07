def get_primes(n):
    primes = [x for x in range(2, n + 1)
              if x not in [
                  i for sub in [list(range(2 * j, n + 1, j)) for j in range(2, int(n**0.5) + 1)] for i in sub]
              ]
    return primes



