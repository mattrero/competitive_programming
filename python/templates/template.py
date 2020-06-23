from collections import defaultdict
import math
import sys

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


# for i in range(n):
#    pass

# for index, value in enumerate(n):
#    pass

# for key, value in dico.items():
#     pass






