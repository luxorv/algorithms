import random

def maximum_pairwise(nums):
    maxp = 0
    for num in nums:
        for xnum in nums:
            if num is not xnum and num * xnum > maxp:
                maxp = num * xnum
    return maxp


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


def test():

    while True:
        n = random.randint(2, 10)
        nums = []

        for i in range(n):
            nums.append(random.randint(0, 100000))

        print(n)
        print(nums)

        maxp = maximum_pairwise(nums)
        maxpf = maximum_pairwise_fast(nums)

        if maxp != maxpf:
            print("Wrong answer: {} {}".format(maxp, maxpf))
            break
        else:
            print("Ok")

test()
