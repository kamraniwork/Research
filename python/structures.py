# collections
# import collections
#
# d = collections.OrderedDict(one=1, three=3, two=2, a=0)
# for i in d:
#     print(i)
# ----------------------------------------------------------
# defaultdict
# from collections import defaultdict
#
# dd = defaultdict(list)
# dd['a'].append(1)
#
# for i in dd:
#     print(dd[i])
#
# print(dd['bb'])
# ---------------------------------------------------------
# from collections import ChainMap
#
# dict1 = {"one": 1, "two": 2}
# dict2 = {"three": 3, "four": 4}
#
# chain = ChainMap(dict1, dict2)
#
# print(chain['one'])
# chain['one'] = 11
# print(chain['one'])
# -----------------------------------------------------------
from types import MappingProxyType

writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)

print(read_only["one"])
# output: 1
read_only["one"] = 23
# output: error
