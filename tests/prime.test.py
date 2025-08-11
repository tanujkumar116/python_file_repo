```python
import pytest
from prime import is_prime, list_primes, count_primes

def test_is_prime_small_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True

def test_is_prime_large_numbers():
    assert is_prime(1009) == True
    assert is_prime(1000000007) == True

def test_is_prime_negative():
    assert is_prime(-1) == False
    assert is_prime(-10) == False

def test_list_primes_various_limits():
    assert list_primes(0) == []
    assert list_primes(10) == [2, 3, 5, 7]
    assert list_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def test_list_primes_negative():
    with pytest.raises(ValueError):
        list_primes(-1)


def test_count_primes_various_limits():
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(10) == 4
    assert count_primes(100) == 25

def test_count_primes_negative():
    with pytest.raises(ValueError):
        count_primes(-5)

```
