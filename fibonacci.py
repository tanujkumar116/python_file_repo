def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def find_in_fibonacci(num):
    seq = fibonacci(20)
    return num in seq, seq

if __name__ == "__main__":
    n = 15
    print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
    search_num = 21
    found, seq = find_in_fibonacci(search_num)
    print(f"Is {search_num} in Fibonacci sequence? {found}")
