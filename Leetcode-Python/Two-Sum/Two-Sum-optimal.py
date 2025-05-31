"""Solution explanation in my own words:
So in the brute force method, you have O(n^2) operations here you have just O(n). This is because the lookups in this case only require you to perform an average of O(1) operations for each number. This can only be done because we know the target beforehand. 
Why is this? The hash map stores each number with a value under the hash function. When you enter the complement into the hash map, the hash map will check for that hash function (that was obtained through complement), and its corresponding buckets in the case of collisions, and if it finds an empty bucket, it is not in the list. Just one thing happened, get hash function check if it its there. It can go through multiple iterations as there may be multiple buckets (dependent on how many collisions with the input hash function). However, it does not scale with the size of the list so it is still on average O(1) while not necessarily always necessarily one operation. This will be much faster than checking through the list. 
It is kind of like if you tell someone a word is on page 104 of the dictionary, it might not be the first word, but you will find it a lot quicker than iterating through every single word in the dictionary and checking if it is there."""

class Solutions:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nummap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nummap:
                return [nummap[complement], i]
            nummap[num] = i

obj = Solutions()

result = obj.twoSum([2,3,5], 7)

print(result)