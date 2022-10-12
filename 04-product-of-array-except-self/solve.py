"""
Given an array `nums`, return an array `answer` such that `answer[i]` is equal
to the product of all the elements of `nums` except `nums[i]`.
"""


def solve_1(nums: list[int]):
    """ Solve the problem in linear time, but also linear memory.

    Idea: Utilize a prefix and postfix array to pre-compute the products of all
    values that come before and after `i`, respectively.
    >>> solve_1([1, 2, 3, 4])
    [24, 12, 8, 6]
    >>> solve_1([-1, 1, 0, -3 , 3])
    [0, 0, 9, 0, 0]
    """
    prefix_product = [1] + [None] * (len(nums) - 1)
    postfix_product = [None] * (len(nums) - 1) + [1]
    for i in range(1, len(nums)):
        prefix_product[i] = prefix_product[i - 1] * nums[i-1]
        postfix_product[len(nums) - 1 - i] = postfix_product[len(nums) - i] * nums[len(nums) - i]
    result = [a*b for a, b in zip(prefix_product, postfix_product)]
    return result


def solve_2(nums: list[int]):
    """ Solve the problem in linear time and constant memory.

    Idea: Compute the prefix product for each element and write it to the
    result array. Then, compute the postfix product element and multiply it
    with the existing prefix product in the result array.
    >>> solve_2([1, 2, 3, 4])
    [24, 12, 8, 6]
    >>> solve_2([-1, 1, 0, -3 , 3])
    [0, 0, 9, 0, 0]
    """
    result = [1] + [None] * (len(nums) - 1)
    prefix = 1
    for i in range(1, len(nums)):
        result[i] = prefix * nums[i-1]
        prefix = result[i]
    postfix = 1
    for i in reversed(range(len(nums))):
        result[i] = result[i] * postfix
        postfix *= nums[i]
    return result
