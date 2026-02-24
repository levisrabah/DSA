# A program that outputs the number of good pairs in a list of integers
def count_good_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count
print(count_good_pairs([1, 2, 3, 1, 1, 3]))