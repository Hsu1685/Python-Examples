def getCombination(n, max, current, result):
    # Base case
    if n == 0:
        print(result)
    # Recursive case
    else:
        for iter1 in current[-1*n]:
            if len(result) < max:
                result.append(iter1)
            else:
                result = result[:-1*n]
                result.append(iter1)
            getCombination(n-1, max, current, result)
            if n == max:
                result = []

if __name__ == '__main__':
    start = [range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2)]
    start2 = [range(0, 2), range(0, 2), range(0, 2), range(0, 2), range(0, 2)]
    getCombination(len(start2), len(start2), start2, [])