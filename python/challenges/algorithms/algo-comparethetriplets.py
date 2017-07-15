"""
Alice and Bob each created one problem for HackerRank. A
reviewer rates the two challenges, awarding points on a scale
from 1 to 100 for three categories: problem clarity,
originality, and difficulty.

We define the rating for Alice's challenge to be a triplet,
and the rating for Bob's challenge to be a triplet.

Your task is to find their comparison scores.

Input:
    5 6 7
    3 6 10

Output:
    1 1
"""


def comparison_scores(first, second):
    difference = list(map(lambda a, b: a - b, first, second))

    return len(list(filter(lambda x: x > 0, difference))), \
        len(list(filter(lambda x: x < 0, difference)))

alice = tuple(map(int, input().strip().split(' ')))
bob = tuple(map(int, input().strip().split(' ')))

alice_score, bob_score = comparison_scores(alice, bob)
print('{0} {1}'.format(alice_score, bob_score))

# f-strings not supported on HackerRank
# print(f'{alice_score} {bob_score}')
