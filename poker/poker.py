import random


def shuffle(deck):
    '''Knuth's Algorithum P.'''
    n = len(deck)
    for i in range(n - 1):  # not to swap last item with itself
        swap(deck, i, random.randrange(i, n))


def swap(deck, i, j):
    '''Swap elements i and j of a collection.'''
    deck[i], deck[j] = deck[j], deck[i]


def poker(hands):
    '''Return a list of winning hands: poker([hand,...]) => [hand,...]'''
    if hands:
        return allmax(hands, key=hand_rank)
    return None


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    maximum = max(iterable, key=key)
    return list(filter(
        lambda hand: hand_rank(hand) == hand_rank(maximum),
        iterable))


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    # ranks_to_nums = {
    #     'T': 10,
    #     'J': 11,
    #     'Q': 12,
    #     'K': 13,
    #     'A': 14
    # }
    # ranks = [r for r, s in hand]
    # ranks = list(map(
    #     lambda x: ranks_to_nums[x] if x in ranks_to_nums.keys() else int(x),
    #     ranks)
    # )

    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks


def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return ranks == list(range(ranks[0], ranks[4] - 1, -1))


def flush(hand):
    "Return True if all the cards have the same suit."
    return len({suit for rank, suit in hand}) == 1


def kind(number, ranks):
    for num in ranks:
        if ranks.count(num) == number:
            return num
    return None


# def group_by(ranks):
#     result = {}
#     for item in ranks:
#         if item in result:
#             result[item] += 1
#         else:
#             result[item] = 1
#     return result


# def two_pair(ranks):
#     """If there are two pair, return the two ranks as a
#     tuple: (highest, lowest); otherwise return None."""
#     grouped = group_by(ranks)
#     result = [key for key, value in grouped.items() if value == 2]
#     if len(result) < 2:
#         return None
#     else:
#         return tuple(sorted(result, reverse=True))


def two_pair(ranks):
    ranks = sorted(ranks, reverse=True)
    higher_pair = kind(2, ranks)
    lower_pair = kind(2, sorted(ranks))
    if higher_pair and higher_pair != lower_pair:
        return (higher_pair, lower_pair)
    return None


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, max(ranks), ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def deal(numhands, n=5, deck=[r + s for r in '23456789TJQKA' for s in 'SHDC']):
    # random.shuffle(deck)
    shuffle(deck)
    return [
        deck[n * index: n * index + 5]
        for index in range(numhands)]


def main():
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]
    sf1 = "6C 7C 8C 9C TC".split()  # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    print(poker([sf1, sf2, fk, fh]) == [sf1, sf2])
    print(deal(1))
    print(deal(2))
    print(deal(5))


if __name__ == '__main__':
    main()
