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





def bruteforce(x, y, items_plus, items_mul, path, score):

    _err(path)
    _err(score)

    if not items_plus and not items_mul:
        return path, score

    best_path, best_score = None, score

    if items_plus:
        for i in range(len(items_plus)):
            new_items = list(items_plus)
            del new_items[i]
            type, ix, iy = items_plus[i]

            if type == '*':
                new_score = score * 2
            else:
                new_score = score + 1

            new_path = path
            if x < ix:
                new_path += '>'*(ix-x)
            if x > ix:
                new_path += '<' * (x - ix)
            if y < iy:
                new_path += 'v'*(iy-y)
            if y > iy:
                new_path += '^' * (y-iy)

            return bruteforce(ix, iy, new_items, items_mul, new_path+'x', new_score)

            if newscore > best_score:
                best_path, best_score = newpath, newscore
    else:


        for i in range(len(items_mul)):
            new_items = list(items_mul)
            del new_items[i]
            type, ix, iy = items_mul[i]

            if type == '*':
                new_score = score * 2
            else:
                new_score = score + 1

            new_path = path
            if x < ix:
                new_path += '>'*(ix-x)
            if x > ix:
                new_path += '<' * (x - ix)
            if y < iy:
                new_path += 'v'*(iy-y)
            if y > iy:
                new_path += '^' * (y-iy)

            return bruteforce(ix, iy, None, new_items, new_path+'x', new_score)

            if newscore > best_score:
                best_path, best_score = newpath, newscore

    return best_path, best_score

n=_int()


items_plus = []
items_mul = []

for y in range(n):
    for x, d in enumerate(_str()):
        if d in ['*']:
            items_mul.append((d,x,y))
        if d in ['o']:
            items_plus.append((d,x,y))

p, s = bruteforce(0, 0, items_plus, items_mul, '', 0)


print(p)
