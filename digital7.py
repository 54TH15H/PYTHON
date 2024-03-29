# You have 100 cards, numbered 1 to 100. You distribute them into k piles and collect back the
# piles in order. For example, if you distribute them into 4 piles, then the first pile will contain the
# cards numbered 1, 5, 9, … and the 4 th pile will contain the cards numbered 4, 8, 12, …. While
# collecting back the cards you collect first the last pile, flip it bottom to top, then take the third
# pile, flip it bottom to top and put the cards on top of the 4th pile and so on. Next round, you
# distribute the cards into another set of piles and collect in the same manner (last pile first and
# first pile last).
#  If we have 10 cards, and put them into 2 piles, the order of the cards in the piles (top to
# bottom) would be 9, 7, 5, 3, 1 and 10, 8, 6, 4, 2
#  We flip the piles to get the order 1, 3, 5, 7, 9 and 2, 4, 6, 8, 10
#  We put the second pile at the bottom and first on top of it to get the deck 1, 3, 5, 7, 9, 2,
# 4, 6, 8, 10
#  Given the number of rounds (m), the number of piles in each round (ki), you need to
# write a program to find the Nth card from the top at the end of the final round.
# Input:
#  The input consists of a single line of (m+2) comma-separated integers.
#  The first number is m, the number of rounds. The next m numbers are ki which represent
# the number of piles in each round.
#  The last number in the input is N, the position in the final pile whose value is to be
# determined.
# Output: One integer representing the Nth card after all rounds have been played.
# Constraints: Number of rounds <= 10, number of piles in each round <= 13.
# Example 1
# Input: 2, 2, 2, 4
# Output: 13
# Explanation:
#  m = 2, k1 = 2, k2 = 2 and N = 4.
#  We have two rounds. The first round has two piles. At the end of the round, the deck is in
# the following order: 1, 3, 5, …, 99, 2, 4, 6, …, 100
#  The next round also has 2 piles and after the second round, the cards are in the order 1, 5,
# 9, 13, ….
#  The fourth card from the top has number 13.
# Example 2
# Input: 3, 2, 2, 3, 2
# Output: 13
# Explanation:
#  m = 3, k1 = 2, k2 = 2, k3 = 3 and N = 2.
#  After the second round, the cards are in the order 1, 5, 9, 13, …
#  The third round has 3 piles. Thus after this round the cards will be in the order 1, 13, ….
# the Second card is 25.

from itertools import chain
def fun():
    m = 3
    k = [2,2,3]
    N = 2
    # --------------------------------------------------------------
    # m = 2
    # k = [2,3]
    # N = 2
    # --------------------------------------------------------------
    # m = int(input())
    # k = []
    # for i in range(m): k.append(int(input()))
    # N = int(input())
    # --------------------------------------------------------------
    lst = [x for x in range(1,101)]
    for i in range(m):
        piles = []
        for temp in range(k[i]): piles.append([])
        for j in range(len(lst)): piles[j%k[i]].append(lst[j])
        lst = list(chain.from_iterable(piles))
    print(lst[N])
fun()