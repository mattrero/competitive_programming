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

count = 0

vals = _int(n+1)
inf = False

for i in range(n):
    if vals[i] == vals[i+1] and vals[i] == n/2:
        inf = True
    elif vals[i] == n/2:
        count += 1
    elif vals[i] < n/2 < vals[i+1] or vals[i+1] < n/2 < vals[i]:
        count += 1

if n > 0 and vals[-1] == n/2:
    count += 1

print(count if not inf else 'INF')

