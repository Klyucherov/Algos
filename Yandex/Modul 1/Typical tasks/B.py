# Первое решение
def solutionB(num: int) ->str:
    num = str(num)
    new = ''
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '-':
            new = '-' + new
        elif num[i] == '0':
            if new != '':
                new += num[i]
        else:
            new += num[i]
    return new

num = -15005
print(solutionB(num))


# Второе решение
def reverse_num(n: str) -> str:
    """This is optimized for readability.
        If need to optimize for performance, can do in one cycle."""
    if n in {'', '0'}:
        return n
    sign = '-' if n[0] == '-' else ''
    result = n.rstrip('0').lstrip('-')
    return sign + "".join(reversed(result))

def main():
    with open('input.txt') as f:
        num = f.readline().strip()
    print(reverse_num(num))

if __name__ == "__main__":
    main()