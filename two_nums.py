

def twoSum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        print("========================================")
        print(list(enumerate(nums)))
        r = target - j
        print(r)
        if r in d:
            print(f"[d[r], i] : {[d[r], i]}")
            return [d[r], i]
        
        d[j]=i
        print(f"dictionary now has {d}")
        print(f"d : {d}")


nums = [10,6,2,5,7,11,15]
target = 9

print(twoSum(nums,target))