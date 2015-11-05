import itertools


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    maximum = max(iterable, key=key)
    return list(filter(
        lambda hand: hand_rank(hand) == hand_rank(maximum),
        iterable))


# def group_by(hands):
#     result = {}
#     for hand in hands:
#         rank = hand_rank(hand)[0]
#         if rank in result:
#             result[rank].append(hand)
#         else:
#             result[rank] = [hand]
#     return result


# def get_best(sorted_cards):
#     for key, value in sorted_cards.items():
#         if key == max(sorted_cards.keys()):
#             return allmax(value, key=hand_rank)[0]


# def best_hand(hand):
#     "From a 7-card hand, return the best 5 card hand."
#     # items = ''.join(map(str, range(len(hand))))
#     items = '0123456'
#     all_hands = list(itertools.combinations(items, 5))
#     all_hands = [[hand[index] for index in map(int, h)] for h in all_hands]
#     sorted_cards = group_by(all_hands)  # sorted items
#     return get_best(sorted_cards)


# Simpler than using the above three functions to do the same
def best_hand(hand):
    return max(itertools.combinations(hand, 5), key=hand_rank)


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def straight(ranks):
    """Return True if the ordered
    ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def kind(n, ranks):
    """Return the first rank that this hand has
    exactly n-of-a-kind of. Return None if there
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """If there are two pair here, return the two
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    return 'test_best_hand passes'

print test_best_hand()
