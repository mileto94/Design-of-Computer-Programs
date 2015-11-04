from poker import *  # noqa
from collections import defaultdict


def shuffle2(deck):  # O(n^2) OK
    n = len(deck)
    swapped = [False] * n
    while not all(swapped):
        i, j = random.randrange(n), random.randrange(n)
        swapped[i] = True
        swap(deck, i, j)


def shuffle3(deck):  # O(n) BAD
    n = len(deck)
    for i in range(n):
        swap(deck, i, random.randrange(n))


def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    expected = n * 1. / factorial(len(deck))  # expected count
    ok = all(
        (0.9 <= counts[item] / expected <= 1.1)
        for item in counts)
    name = shuffler.__name__
    print('%s(%s) %s' % (name, deck, ('ok' if ok else '*** BAD ***')))
    print('    ')
    for item, count in sorted(counts.items()):
        print('%s:%4.1f' % (item, count * 100.0 / n))
    print()


def test_shufflers(
        shufflers=[shuffle, shuffle2, shuffle3], decks=['abc', 'ab']):
    for deck in decks:
        print()
        for func in shufflers:
            test_shuffler(func, deck)


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    test_shufflers()
