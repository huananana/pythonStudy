"""__author__=蒋志颖"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

# 从一叠牌中抽取特定的一张纸牌
    def __getitem__(self, position):
        return self._cards[position]


print("========1=========")
# 纸牌对象
beer_card = Card('7', 'diamonds')
print(beer_card)

print("========2=========")
# 运行类，产生52张牌
deck = FrenchDeck()
print(len(deck))

print("========3=========")
# 从一叠牌中抽取特定的一张纸牌，deck[0],deck[-1]。都是由__getitem__方法提供的
print(deck[0], deck[-1])

print("========4=========")
# 随机抽取一张牌
for _ in range(6):
    print(choice(deck))

# 抽取所有K牌
print("========5=========")
print(deck[11::13])

# 可迭代
for card in deck:   # doctest: +ELLIPSIS # : 过长的内容可能被省略，使用这代码可以保证全部输出
    print(card)

# 反向迭代
for card in reversed(deck):   # doctest: +ELLIPSIS
    print(card)


print(Card("Q", "hearts") in deck)
print(Card("7", "beasts") in deck)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high): # doctest: + ELLIPSIS
    print(card)
