def two_sum(nums, target):
    """这样写更直观，遍历列表同时查字典"""
    dct = {}
    result = []
    for i, n in enumerate(nums):
        if target - n in dct:
            result.append((dct[target - n], i))
        dct[n] = i
    return result


list = [1,2,3,3,1,4]
a = two_sum(list,4)
print(a)
