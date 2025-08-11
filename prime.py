def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(limit):
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes

def count_primes(limit):
    return len(list_primes(limit))

if __name__ == "__main__":
    limit = 50
    print(f"Prime numbers up to {limit}: {list_primes(limit)}")
    print(f"Total primes up to {limit}: {count_primes(limit)}")
