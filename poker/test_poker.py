import unittest
from poker import *  # noqa


class TestHighestRankHand(unittest.TestCase):
    '''Test poker() returns the highest ranking hand.'''

    def setUp(self):
        self.sf = '6C 7C 8C 9C TC'.split()  # straight flush
        self.fk = '9D 9H 9S 9C 7D'.split()  # four of a kind
        self.fh = 'TD TC TH 7C 7D'.split()  # full house

    def test_for_straight_flush(self):
        '''Test poker() for straight flush'''
        self.assertEqual(poker([self.sf, self.fk, self.fh]), [self.sf])

    def test_for_four_of_kind(self):
        '''Test poker() for four of kind'''
        self.assertEqual(poker([self.fk, self.fh]), [self.fk])

    def test_for_full_house(self):
        '''Test poker() for full house'''
        self.assertEqual(poker([self.fh, self.fh]), [self.fh, self.fh])

    def test_for_a_one_hand_deck(self):
        '''Test poker() with 1 hand'''
        self.assertEqual(poker([self.fh]), [self.fh])

    def test_for_a_deck_with_100_hands(self):
        '''Test poker() with 100 hands'''
        self.assertEqual(poker([self.fk, self.fh] * 50), [self.fk] * 50)

    def test_for_an_empty_deck(self):
        '''Test poker() with 0 hands'''
        self.assertEqual(poker([]), None)


class TestHighestRankInAHand(unittest.TestCase):
    '''Test hand_rank() returns the highest rank in the hand.'''

    def setUp(self):
        self.sf = '6C 7C 8C 9C TC'.split()  # straight flush
        self.fk = '9D 9H 9S 9C 7D'.split()  # four of a kind
        self.fh = 'TD TC TH 7C 7D'.split()  # full house

    def test_hand_rank_with_straight_flush(self):
        '''Test get info for straight flush'''
        self.assertEqual(hand_rank(self.sf), (8, 10))

    def test_hand_rank_with_four_of_a_kind(self):
        '''Test get info for four of a kind'''
        self.assertEqual(hand_rank(self.fk), (7, 9, 7))

    def test_hand_rank_with_full_house(self):
        '''Test get info for full house'''
        self.assertEqual(hand_rank(self.fh), (6, 10, 7))


class TestGetHandRank(unittest.TestCase):
    '''Test card_ranks() returns the highest ranking hand.'''

    def setUp(self):
        self.sf = '6C 7C 8C 9C TC'.split()  # straight flush - 8
        self.fk = '9D 9H 9S 9C 7D'.split()  # four of a kind - 7
        self.fh = 'TD TC TH 7C 7D'.split()  # full house - 6
        self.f = '6C 3C 8C 7C TC'.split()  # flush - 5
        self.s = '9D 8H 7S 6D 5C'.split()  # straight - 4
        self.tk = 'TD TC TH 7C 3D'.split()  # three of a kind - 3
        self.tp = '6C 7D 7C 6D TC'.split()  # two pair - 2
        self.p = '9D 9H TS 7D 4C'.split()  # pair - 1
        self.hc = 'TD 3C 2H 6C 7D'.split()  # high card - 0

    def test_get_rank_of_straight_flush(self):
        '''Test get info for straight flush'''
        self.assertEqual(card_ranks(self.sf), [10, 9, 8, 7, 6])

    def test_get_rank_of_four_of_a_kind(self):
        '''Test get info for full house'''
        self.assertEqual(card_ranks(self.fk), [9, 9, 9, 9, 7])

    def test_get_rank_of_full_house(self):
        '''Test get info for full house'''
        self.assertEqual(card_ranks(self.fh), [10, 10, 10, 7, 7])

    def test_get_rank_of_flush(self):
        '''Test get info for flush'''
        self.assertEqual(card_ranks(self.f), [10, 8, 7, 6, 3])

    def test_get_rank_of_straight(self):
        '''Test get info for straight'''
        self.assertEqual(card_ranks(self.s), [9, 8, 7, 6, 5])

    def test_get_rank_of_three_of_a_kind(self):
        '''Test get info for three of a kind'''
        self.assertEqual(card_ranks(self.tk), [10, 10, 10, 7, 3])

    def test_get_rank_of_two_pair(self):
        '''Test get info for two pair'''
        self.assertEqual(card_ranks(self.tp), [10, 7, 7, 6, 6])

    def test_get_rank_of_pair(self):
        '''Test get info for pair'''
        self.assertEqual(card_ranks(self.p), [10, 9, 9, 7, 4])

    def test_get_rank_of_high_card(self):
        '''Test get info for high card'''
        self.assertEqual(card_ranks(self.hc), [10, 7, 6, 3, 2])


class TestHelperFunctions(unittest.TestCase):
    '''Test helper functions.'''

    def setUp(self):
        self.sf = '6C 7C 8C 9C TC'.split()  # straight flush - 8
        self.fk = '9D 9H 9S 9C 7D'.split()  # four of a kind - 7
        self.fh = 'TD TC TH 7C 7D'.split()  # full house - 6
        self.f = '6C 3C 8C 7C TC'.split()  # flush - 5
        self.s = '9D 8H 7S 6D 5C'.split()  # straight - 4
        self.tk = 'TD TC TH 7C 3D'.split()  # three of a kind - 3
        self.tp = '6C 7D 7C 6D TC'.split()  # two pair - 2
        self.p = '9D 9H TS 7D 4C'.split()  # pair - 1
        self.hc = 'TD 3C 2H 6C 7D'.split()  # high card - 0
        self.fk_ranks = card_ranks(self.fk)
        self.tp_ranks = card_ranks(self.tp)
        self.s_ranks = card_ranks(self.s)

    def test_get_straight_true(self):
        '''Test get straight'''
        self.assertTrue(straight(self.s_ranks))

    def test_get_straight_false(self):
        '''Test fail to get straight'''
        self.assertFalse(straight(self.fk_ranks))

    def test_get_flush_true(self):
        '''Test get flush'''
        self.assertTrue(flush(self.sf))

    def test_get_flush_false(self):
        '''Test fail to get flush'''
        self.assertFalse(flush(self.fk))

    def test_get_four_of_kind(self):
        '''Test get four of a kind'''
        self.assertEqual(kind(4, self.fk_ranks), 9)

    def test_get_three_of_kind(self):
        '''Test get three of a kind'''
        self.assertEqual(kind(3, self.fk_ranks), None)

    def test_get_two_of_kind(self):
        '''Test get two of a kind'''
        self.assertEqual(kind(2, self.fk_ranks), None)

    def test_get_one_of_kind(self):
        '''Test get one of a kind'''
        self.assertEqual(kind(1, self.fk_ranks), 7)

    def test_get_two_pair_with_two(self):
        '''Test get two pair with two pairs.'''
        self.assertEqual(two_pair([5, 5, 10, 2, 10]), (10, 5))

    def test_get_two_pair_with_one(self):
        '''Test get two pair with a pair.'''
        self.assertEqual(two_pair([5, 3, 10, 2, 10]), None)

    def test_get_two_pair_without_a_pair(self):
        '''Test get two pair without a pair.'''
        self.assertEqual(two_pair([5, 3, 4, 2, 10]), None)


if __name__ == '__main__':
    unittest.main()
