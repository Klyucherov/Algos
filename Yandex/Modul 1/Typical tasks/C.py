def find_two_missing_numbers(n: int, nums):
    """Этот метод оптимизирован для удобочитаемости.
    Если необходимо оптимизировать по памяти, можно использовать XOR и O(1) память."""
    all_nums = set(range(1, n + 1))
    for x in nums:
        all_nums.remove(x)
    return all_nums

def main():
    with open('input.txt') as f:
        n = int(f.readline().strip())
        nums = map(int, f.readline().split())
        a, b = find_two_missing_numbers(n, nums)
        print("%i %i" % (a, b))
