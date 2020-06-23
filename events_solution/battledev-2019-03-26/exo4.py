from collections import defaultdict
import math
import sys
from functools import lru_cache

__cache_input = None

def __item(num, op):
    global __cache_input
    r = []
    for _ in range(num):
        if not __cache_input:
            __cache_input = input().split(' ')
        r.append(op(__cache_input.pop(0)))
    return r[0] if num == 1 else r
def _str(num=1): return __item(num,str)
def _int(num=1): return __item(num,int)
def _float(num=1): return __item(num,float)
def _err(msg): print(msg, file=sys.stderr)

# @lru_cache(maxsize=None)

# for i in range(n):
#    pass

# for index, value in enumerate(n):
#    pass

# for key, value in dico.items():
#     pass


def bruteforce(first_word, words, found):

    best_found = found

    for i, l in enumerate(first_word):
        new_words = []
        for w in words:
            if l in w:
                new_words.append(w[w.index(l)+1:])
            else:
                new_words = None
                break

        if new_words:
            if not first_word[i+1:] or not all(new_words):
                if len(best_found) < len(found) + 1:
                    best_found = found + l
            else:
                newfound = bruteforce(first_word[i+1:], new_words, found+l)
                if len(newfound) > len(best_found):
                    best_found = newfound

    return best_found


n=_int()

words_ = []

for _ in range(n):
   words_.append(_str())

first = words_[0]
del words_[0]

r = bruteforce(first, words_, '')

if r:
    print(r)
else:
    print('KO')

