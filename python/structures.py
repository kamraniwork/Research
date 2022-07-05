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
# from types import MappingProxyType
#
# writable = {"one": 1, "two": 2}
# read_only = MappingProxyType(writable)
#
# print(read_only["one"])
# # output: 1
# read_only["one"] = 23
# # output: error
# ------------------------------------------------------------
# arr = ['one', 'two', 'three']
# print(arr[0])
# # output: one
# arr[1] = 'hello'
# print(arr)
# # output: ['one','hello','three']
# del arr[1]
# arr.append(23)
# print(arr)
# # output: ['one','three',23]

# ---------------------------------------------------------------
# arr = ('one', 'two', 'three')
# print(arr[0])
# # output: one
# arr[1] = 'hello'
# # output: error
# del arr[1]
# # output: error
# ----------------------------------------------------------------
# import array
# arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
# print(arr[1])
# # output: 1.5
# arr[1] = 23.0
# print(arr)
# # output: array('f', [1.0, 23.0, 2.0, 2.5])
# del arr[1]
# print(arr)
# # output: array('f', [1.0, 2.0, 2.5])
# arr.append(42.0)
# print(arr)
# # output: array('f', [1.0, 2.0, 2.5, 42.0])
# arr[1] = "hello"
# # output: error
# ------------------------------------------------------------------
arr = "abcd"
print(arr[1])
# output: 'b'
arr[1] = "e"
# output: error
del arr[1]
# output: error
