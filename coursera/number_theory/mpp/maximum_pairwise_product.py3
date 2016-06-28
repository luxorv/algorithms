import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])
nums = [int(tokens[i]) for i in range(1, n+1)]


def maximum_pairwise_fast(nums):
    index1 = -1
    n = len(nums)

    for i in range(n):
        if index1 == -1 or nums[i] > nums[index1]:
            index1 = i

    index2 = -1

    for j in range(n):
        if (j != index1) and (index2 == -1 or nums[j] > nums[index2]):
            index2 = j

    return nums[index1] * nums[index2]

print(maximum_pairwise_fast(nums))
