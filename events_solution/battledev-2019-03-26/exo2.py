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


n = _int()

som = 0
aller = 0


for _ in range(n):
    p = _int()

    if som + p > 100:
        aller += 1
        som = p
    else:
        som += p

print(aller+1)

