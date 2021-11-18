def tup_examples():
    x, y = 2, 3

    y, x = x, y

    a = b = c = 0  # all are ref to 0

    T = 1, 2, 3, 4, 5  # tuple

    q, w, e, r, i = T

    o, p, *rest = T  # *rest, o, p = T

    print(T)  # (1, 2, 3, 4, 5)

    print(*T)  # 1, 2, 3, 4, 5

    print(*T, sep=":", end="!\n")  # 1: 2: 3: 4: 5!


def for_examples(a: int, b: str,
                 ):
    # range function returns iterable objects (арифм. прогрессии)
    A = range(3)  # генератор арифметических прогрессий
    # range(start,stop, step), step = int
    # print(A) 0, 1, 2, 3
    print(*A)  # 0 1 2

    # for loop works with any iterable objects
    for i in range(a):
        print()

    B = 2, 3, 4, 5

    for j in range(len(B)):
        print(B[j])

    C = [(1, 2), (3, 4), (5, 6)]
    for k in range(len(C)):
        T = C[k]
        width, height = T  # govnocod

    for elem in C:
        width, height = elem

    for width, height in C:
        print(width, height)

    # for iter objects with 1 argument
    objects = [a, b]
    # how to give an index in for
    for i, elems in enumerate(objects):
        print(i)


def func_with_long_argument_list(a, b, c, d, rest):
    # see call method
    print()


def sets_dicts_examples():
    A_set = {'moskva',
             'amsterdam',
             'novosibirsk'}
    A_set.add('NewCity')
    if 'moskva' in A_set:
        print('moskva')

    for el in A_set:
        print(el)

    B_dict = {'moskva': 100,
              'novosibirsk': 200,
              'riga': 1000}
    B_dict['newcity'] = 100000
    for name, val in B_dict:
        print(name, '----', val)
    for key in B_dict:
        print(key, '----', B_dict[key])


def test_func() -> None: # returned type function annotation
    pass

def main_local():
    variables = 2, 3, 4, 5
    rest = 10
    func_with_long_argument_list(*variables, rest)
