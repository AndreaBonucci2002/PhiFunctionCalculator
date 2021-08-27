Number = input('Phi(x) calculator, let x be:')


def factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors


def primefac(lst):
    new_lst = list(set([(i, lst.count(i)) for i in lst]))
    new_lst.sort(key=lambda x: x[1])
    return new_lst


def phi(lst):
    x = []
    for i in range(0, len(lst)):
        h = (lst[i])
        for j in range(0, len(h) - 1):
            if int(h[j + 1]) == 1:
                x.append(int(h[j] - 1))
            else:
                x.append(int(h[j]) ** int(h[j + 1] - 1) * int(h[j] - 1))
    return x


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

print(multiplyList(phi(primefac(factors(int(Number))))))
