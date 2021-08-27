Number = input('Phi(x) calculator, let x be:')


def factors(num):
    i = 2
    factors = []
    while i <= num:
        if (num % i) == 0:
            factors.append(i)
            num = num / i
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


def multiplyList(lst):
    res = 1
    for x in lst:
        res = res * x
    return res

print(multiplyList(phi(primefac(factors(int(Number))))))
